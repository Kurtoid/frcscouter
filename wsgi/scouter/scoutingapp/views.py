from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import SignUpForm, LoginForm, ScoutingForm, FieldSetupForm, SortViewMatchForm
from .models import FieldSetup, Match, Tournament
from django.contrib.auth import logout, login
from django.contrib import messages
from .tables import MatchTable
from django_tables2 import RequestConfig

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
    matches = MatchTable(Match.objects.all())
    # enables ordering
    if request.method=="POST":
        tform = SortViewMatchForm(request.POST)
        if tform.is_valid():
            tlist = tform.cleaned_data['tourney_select']
            print(type(tlist))
            print(tlist)
            matches =MatchTable(Match.objects.filter(tournament__in=tlist))
    RequestConfig(request).configure(matches)

    return render(request, 'scoutingapp/viewrounds.html', {'rounds': matches,
                                                           'tournaments':
                                                           Tournament.objects.all(),
                                                           'tform': tform})


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
            return HttpResponseRedirect('/scoutingapp/signupcomplete/')
    else:
        form = SignUpForm()

    return render(request, 'scoutingapp/signup.html', {'form': form})


def logincomplete(request):
    if request.user.is_authenticated():
        return render(request,
                      'scoutingapp/logincomplete.html',
                      {'user': request.user})
    else:
        return HttpResponse("user not logged in!")


def signupcomplete(request):
    return HttpResponse('DONE!')


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
