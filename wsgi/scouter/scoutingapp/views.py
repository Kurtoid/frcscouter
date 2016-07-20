from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import (SignUpForm, LoginForm, ScoutingForm, FieldSetupForm,
                    SortViewMatchForm, MatchNumberAttribs,
                    MatchViewFormMetaOptions, importTeamForm)
from .models import FieldSetup, Match, Tournament, Team
from django.contrib.auth import logout, login
from django.contrib import messages
from .tables import MatchTable
from django_tables2 import RequestConfig
from django.core.exceptions import ObjectDoesNotExist
import requests

# Create your views here.


def index(request):
    # return HttpResponse("Hello World!")
    return render(request, 'scoutingapp/index.html')


def fieldsetupcontrol(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = FieldSetupForm(request.POST)
            if form.is_valid():
                setup = form.save()
                print(setup.id)
                request.session['fsetup'] = setup.id
                # proccess form
                return HttpResponseRedirect('/scoutingapp/scout',
                                            {'fieldsetup': setup})
            else:
                print(form.errors)
        else:
            form = FieldSetupForm()

        return render(request,
                      'scoutingapp/fieldsetupcontrol.html',
                      {'form': form})
    else:
        return HttpResponseRedirect('/scoutingapp/userlogin/')


def viewrounds(request):
    tform = SortViewMatchForm()
    matchattribform = MatchNumberAttribs()
    viewoptionsform = MatchViewFormMetaOptions()
    matchlist = Match.objects.all()
    fieldstoexclude = (None,)
    # enables ordering
    if request.method == "POST":
        tform = SortViewMatchForm(request.POST)
        if tform.is_valid() and tform.cleaned_data['tourney_select']:
            tlist = tform.cleaned_data['tourney_select']
            matchlist = matchlist.filter(tournament__in=tlist)
        matchattribform = MatchNumberAttribs(request.POST)
        if matchattribform.is_valid():
            if matchattribform.cleaned_data['scouted_team']:
                teamlist = matchattribform.cleaned_data['scouted_team']
                matchlist = matchlist.filter(scouted_team__in=teamlist)
            if matchattribform.cleaned_data['crossed_def'] is not None:
                crossdef = matchattribform.cleaned_data['crossed_def']
                matchlist = matchlist.filter(crossed_defense_on_auto=crossdef)
            if matchattribform.cleaned_data['auto_defense_crossed'] is not None:
                crossdef = matchattribform.cleaned_data['auto_defense_crossed']
                matchlist = matchlist.filter(auto_defense_crossed=crossdef)
        viewoptionsform = MatchViewFormMetaOptions(request.POST)
        if viewoptionsform.is_valid():
            print(viewoptionsform.cleaned_data['show_defense_count'])
            if viewoptionsform.cleaned_data['show_defense_count'] is False:
                fieldstoexclude = (
                    'defense1_crossed', 'defense2_crossed', 'defense3_crossed',
                    'defense4_crossed', 'defense5_crossed'
                )
                print('exclude defenses')
        else:
            print(viewoptionsform.errors)
    matches = MatchTable(matchlist, exclude=fieldstoexclude)
    RequestConfig(request).configure(matches)

    return render(request, 'scoutingapp/viewrounds.html', {
        'rounds': matches,
        'tournaments':
        Tournament.objects.all(),
        'tform': tform,
        'matchattribform':
        matchattribform,
        'viewoptionsform':
        viewoptionsform
    })


def userlogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.getuser())
            if(request.user.is_authenticated()):
                print("auth done")
                messages.add_message(request, messages.INFO, 'You are now'
                                     ' logged in.')
            # TODO process
            return HttpResponseRedirect('/scoutingapp/')
    else:
        form = LoginForm()
    return render(request, 'scoutingapp/userlogin.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.scouted_by = request.user
            form.save()
            # proccess form
            return HttpResponseRedirect('/scoutingapp/index/')
    else:
        form = SignUpForm()

    return render(request, 'scoutingapp/signup.html', {'form': form})


def usercontrolpanel(request):
    if request.user.is_authenticated():
        return render(
            request, 'scoutingapp/usercontrolpanel.html',
            {'user': request.user})
    return HttpResponse("usercontrolpanel")


def logoutuser(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect("/scoutingapp/")


def scout(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = ScoutingForm(request.POST)
            fieldsetform = FieldSetupForm(request.POST)
            if form.is_valid() and fieldsetform.is_valid():
                match = form.save(commit=False)
                fieldset = fieldsetform.save()
                match.scouted_by = request.user
                match.field_setup = fieldset
                match.save()
                # proccess form
                return HttpResponseRedirect('/scoutingapp/')
            else:
                print(form.errors)
        else:
            form = ScoutingForm()
            fieldsetform = FieldSetupForm()

        if request.session.get('fsetup'):
            return render(
                request, 'scoutingapp/scout.html',
                {'form': form, 'fieldsetform': fieldsetform,
                 'setupkey': FieldSetup.objects.get(
                     id=request.session.get('fsetup'))})
        return render(
            request, 'scoutingapp/scout.html',
            {'form': form, 'fieldsetform': fieldsetform})
    else:
        return HttpResponseRedirect('/scoutingapp/userlogin/')


def demo_scout_page(request):
    fieldsetform = FieldSetupForm()
    form = ScoutingForm()
    return render(request, 'scoutingapp/scout.html', {'form': form,
                                                      'fieldsetform':
                                                      fieldsetform})
def import_from_TBA(request):
    importform = importTeamForm()
    if request.user.is_authenticated and request.user.is_admin:
        if(request.method == 'POST'):
            importform = importTeamForm(request.POST)
            if importform.is_valid():
                # process and return redirect
                begin = importform.cleaned_data['team_number_begin']
                end = importform.cleaned_data['team_number_end']
                for x in range(begin, end):
                    r = requests.get("http://www.thebluealliance.com/api/v2/team/frc{}".format(x),
                                     headers={'X-TBA-App-Id':
                                              'frc179:scoutingapp:v1'})
                    if r.status_code == 200:
                        print("Checking {}".format(x))
                        try:
                            Team.objects.get(team_number=x)
                        except ObjectDoesNotExist:
                            print('we dont know '
                                  '{}'.format(r.json()['nickname']))
                            team = Team(team_number=x,
                                        team_name=r.json()['nickname'])
                            team.save()
                        print('{}: {}'.format(x, r.json()['nickname']))
        return render(request, 'scoutingapp/importfromtba.html', {'form':
                                                                  importform})
    else:
        return HttpResponse("Not logged in")
