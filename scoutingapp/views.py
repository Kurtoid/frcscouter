# from json import dumps, loads
from django.core import serializers
from django.utils.encoding import smart_str
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import (SignUpForm, LoginForm, ScoutingForm,
                    SortViewMatchForm, MatchNumberAttribs,
                    MatchViewFormMetaOptions, importTeamForm, importEventForm,
                    UserControlForm, AllianceScoutingForm, AllianceMatch, openHouseForm, CubePlaceForm)
from .models import (Match, Tournament, Team, CredentialsModel,
EndGameState, MyUser, CubePlace, CubeAcquired, CubeWhen, CubeScored, ScheduledMatch)
from django.contrib.auth import logout, login
from django.contrib import messages
from .tables import MatchTable, AllianceMatchTable, UserTable, ViewMatchTable, CubeTable, TeamTable
from scouter import settings
from django_tables2 import RequestConfig
from django.core.exceptions import ObjectDoesNotExist
import requests

# Create your views here.
import os
import httplib2
import csv

from googleapiclient.discovery import build
from django.http import HttpResponseBadRequest
from oauth2client.contrib import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from apiclient.http import MediaFileUpload
from scoutingapp.tables import CategoryTable
from scoutingapp import forms
# from itertools import zip_longest
from scoutingapp.models import Card
from scoutingapp.forms import AlliancePreForm

# CLIENT_SECRETS, name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret, which are found
# on the API Access tab on the Google APIs
# Console <http://code.google.com/apis/console>
CLIENT_SECRETS = os.path.join(os.path.dirname(__file__),
                              'client_secrets.json')

FLOW = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/drive',
    redirect_uri=settings.OAUTH_REDIR)


def index(request):
    # return HttpResponse("Hello World!")
    return render(request, 'scoutingapp/index.html')


def export_to_gdocs(request):
    qs = Match.objects.all()
    outfile_path = os.path.join(settings.DATA_DIR, 'exported_data.csv')
    model = qs.model
    writer = csv.writer(open(outfile_path, 'w'))

    headers = []
    for field in model._meta.fields:
        headers.append(field.verbose_name)
    writer.writerow(headers)

    headers = []
    for field in model._meta.fields:
        headers.append(field.name)

    for obj in qs:
        row = []
        for field in headers:
            val = getattr(obj, field)
            if callable(val):
                val = val()
            if type(val) == str:
                val = val.encode("utf-8")
            row.append(val)
        writer.writerow(row)
    del writer
    storage = DjangoORMStorage(
        CredentialsModel, 'id', request.user, 'credential')
    credential = storage.get()
    if credential is None or credential.invalid is True:
        FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
                                                       request.user)
        authorize_url = FLOW.step1_get_authorize_url()
        return HttpResponseRedirect(authorize_url)
    else:
        outfile_path = os.path.join(settings.DATA_DIR, 'exported_data.csv')
        http = httplib2.Http()
        http = credential.authorize(http)
        print('printing file at ' + outfile_path)
        with open(outfile_path, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ',
                                    quotechar='|')
            for row in spamreader:
                print(', '.join(row))
        service = build("drive", "v3", http=http)
        file_metadata = {
            'mimeType': 'application/vnd.google-apps.spreadsheet'
        }
        media = MediaFileUpload(outfile_path,
                                mimetype='text/csv',
                                resumable=True)
        uploadfile = service.files().create(body=file_metadata,
                                            media_body=media, fields='webViewLink').execute()
        return render(request, 'scoutingapp/exporttogdocs.html', {'urlLink': uploadfile['webViewLink']})
    return render(request, 'scoutingapp/exporttogdocs.html')


def auth_return(request):
    if not xsrfutil.validate_token(settings.SECRET_KEY,
                                   bytes(request.REQUEST['state'], 'utf-8'),
                                   request.user):
        return HttpResponseBadRequest()
    credential = FLOW.step2_exchange(request.REQUEST)
    storage = DjangoORMStorage(
        CredentialsModel, 'id', request.user, 'credential')
    storage.put(credential)
    return HttpResponseRedirect("/scoutingapp/exporttogdocs")


def viewrounds(request):
    tform = SortViewMatchForm()
    matchattribform = MatchNumberAttribs()
    viewoptionsform = MatchViewFormMetaOptions()
    matchlist = Match.objects.all()
    # currentTeam = request.user.team
    # matchlist = matchlist.filter(scouted_by__team=currentTeam)
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
        viewoptionsform = MatchViewFormMetaOptions(request.POST)
        if viewoptionsform.is_valid():
            pass;
        else:
            print(viewoptionsform.errors)
    matches = ViewMatchTable(matchlist, exclude=fieldstoexclude)
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
            return HttpResponseRedirect('/scoutingapp/')
    else:
        form = SignUpForm()

    return render(request, 'scoutingapp/signup.html', {'form': form})


def usercontrolpanel(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = UserControlForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                form.save()
                # proccess form
                return HttpResponseRedirect('/scoutingapp/index/')
        else:
            form = UserControlForm()

        return render(request, 'scoutingapp/usercontrolpanel.html',
                      {'user': request.user, 'form': form})
    return render(request, 'scoutingapp/index.html')


def logoutuser(request):
    if request.user.is_authenticated():
        logout(request)
        messages.add_message(request, messages.INFO, 'Logged out!')
    return HttpResponseRedirect("/scoutingapp/")


def scout(request):
    if request.user.is_authenticated():
        cubeform = CubePlaceForm()
        if request.method == 'POST':
            form = ScoutingForm(request.POST)
            form.use_required_attribute = False
            if form.is_valid():
                print(request.POST)
                match = form.save(commit=False)
                match.scouted_by = request.user
                duped = 1
                duped_matches = Match.objects.filter(match_number=match.match_number, scouted_team=match.scouted_team).exclude(scouted_by=match.scouted_by)
                if(len(duped_matches)>0):
                    duped = len(duped_matches)+1

                if(request.user.team.currently_in_event):
                    match.tournament = request.user.team.currently_in_event
                match.duplicate=duped
                match.save()
                cube_data = request.POST.get('cube_placeholder', 'no data')
                print(cube_data)
                split_data = cube_data.split(";");
                for i in split_data:
                    tmp = i.split(", ")
                    print(tmp)
                    if(len(tmp)>=3):
                        print(tmp)
                        cube = CubePlace()
                        cube.acquired = CubeAcquired.objects.filter(name=tmp[0])[0]
                        cube.scored = CubeScored.objects.filter(name=tmp[1])[0]
                        cube.when = CubeWhen.objects.filter(name=tmp[2])[0]
                        cube.match = match;
                        cube.scouted_by = request.user
                        cube.save()
                # proccess form
                messages.add_message(request, messages.INFO, 'Match Recorded')
                return HttpResponseRedirect('/scoutingapp/')
            else:
                print(form.errors)
        else:

            try:
                form = ScoutingForm(initial={'robot_end_game':
                                               EndGameState.objects.get(state="Missed Game")})
            except ObjectDoesNotExist:
                print("Missed game missing")
                form = ScoutingForm()
            form.fields['scouted_team'].queryset = Team.objects.filter(currently_in_event=request.user.team.currently_in_event)
        form.use_required_attribute = False
        return render(
            request, 'scoutingapp/scout.html',
            {'form': form, 'cubeform': cubeform })
    else:
        return HttpResponseRedirect('/scoutingapp/userlogin/')


def alliance_scout(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form_1 = AllianceScoutingForm(request.POST, prefix = "1")
            preform = AlliancePreForm(request.POST, prefix = "pre")
            if form_1.is_valid() and form_2.is_valid() and preform.is_valid():
                match_1 = form_1.save(commit=False)
                match_1.scouted_by = request.user
                match_1.scouter_number = 1
                match_1.match_number = preform.cleaned_data['match_number']
                match_1.alliance = preform.cleaned_data['alliance']
                if(request.user.team.currently_in_event):
                    match_1.tournament = request.user.team.currently_in_event
                match_1.save()
                # proccess form
                messages.add_message(request, messages.INFO, 'Alliance Match Recorded')
                return HttpResponseRedirect('/scoutingapp/')
            else:
                print(form_1.errors)
        else:
            form_1 = AllianceScoutingForm(prefix="1")
            preform = AlliancePreForm(prefix="pre")

        return render(
            request, 'scoutingapp/alliancescout.html',
            {'form1': form_1,'preform': preform})
    else:
        return HttpResponseRedirect('/scoutingapp/userlogin/')

def demo_scout_page(request):
    form = ScoutingForm()
    return render(request, 'scoutingapp/scout.html', {'form': form,
                                                      })


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
                    r = requests.get("http://www.thebluealliance.com/api/v3/team/frc{}".format(x),
                                     headers={'X-TBA-Auth-Key':
                                              'ptxL3AMaCfhTGWVX7nbTYp0wfBqYFIu2HkjSr7hu2zxqWfk3B0uCAdALaVohrrxi'})
                    if r.status_code == 200:
                        print("Checking {}".format(x))
                        try:
                            Team.objects.get(team_number=x)
                        except ObjectDoesNotExist:
                            print('we dont know '
                                  '{}'.format(r.json()['nickname']))
                            if(r.json()['nickname'] is not None):
                                team = Team(team_number=x,
                                            team_name=r.json()['nickname'])
                                team.save()
                        if(r.json()['nickname'] is not None):
                            print('{}: {}'.format(x, r.json()['nickname']))
                    else:
                        print(r.status_code)
        return render(request, 'scoutingapp/importfromtba.html', {'form':
                                                                  importform, 'done': importform.is_valid()})
    else:
        return HttpResponse("Not logged in")


def import_event_from_TBA(request):
    importform = importEventForm()
    if request.user.is_authenticated and request.user.is_admin:
        if(request.method == 'POST'):
            importform = importEventForm(request.POST)
            if importform.is_valid():
                newEvent = None
                # process and return redirect
                event_code = importform.cleaned_data['event_code']
                r = requests.get("http://www.thebluealliance.com/api/v3/event/{}".format(event_code),
                                 headers={'X-TBA-Auth-Key':
                                          'ptxL3AMaCfhTGWVX7nbTYp0wfBqYFIu2HkjSr7hu2zxqWfk3B0uCAdALaVohrrxi'})
                try:
                    newEvent = Tournament.objects.get(name=r.json()['name'])
                except ObjectDoesNotExist:
                    newEvent = Tournament(name=r.json()['name'])
                    newEvent.event_code = event_code
                    newEvent.save()
                r = requests.get("http://www.thebluealliance.com/api/v3/event/{}/teams".format(event_code),
                                     headers={'X-TBA-Auth-Key':
                                              'ptxL3AMaCfhTGWVX7nbTYp0wfBqYFIu2HkjSr7hu2zxqWfk3B0uCAdALaVohrrxi'})
                if r.status_code == 200:
                    print("Checking {}".format(event_code))
                    for x in r.json():
                        team = None
                        try:
                            team = Team.objects.get(team_number=x['team_number'])
                        except ObjectDoesNotExist:
                            print('we dont know '
                                  '{}'.format(x['nickname']))
                            if(x['nickname'] is not None):
                                team = Team(team_number=x['team_number'],
                                            team_name=x['nickname'])
                        team.currently_in_event = newEvent
                        team.save()
                        if(x['nickname'] is not None):
                            print('{}: {}'.format(
                                x['team_number'], x['nickname']))

                r = requests.get("http://www.thebluealliance.com/api/v3/event/{}/matches/simple".format(event_code),
                                     headers={'X-TBA-Auth-Key':
                                              'ptxL3AMaCfhTGWVX7nbTYp0wfBqYFIu2HkjSr7hu2zxqWfk3B0uCAdALaVohrrxi'})
                if(r.status_code == 200):
                    # print(r.json())
                    for x in r.json():
                        if x['comp_level'] != "qm":
                            continue
                        match_num = x['match_number']
                        # print(match_num)
                        team_numbers = []
                        for team in x["alliances"]["blue"]["team_keys"]:
                            team_numbers.append(team)
                        for team in x["alliances"]["red"]["team_keys"]:
                            team_numbers.append(team)
                        # print(team_numbers)
                        for team in team_numbers:
                            teamNum = int(team[3:])
                            # print(teamNum)
                            teamObject = Team.objects.filter(team_number = teamNum)[0]
                            # this might take too long
                            if len(ScheduledMatch.objects.filter(team = teamObject, match_number = match_num, event = newEvent)) < 1:
                                sMatch = ScheduledMatch()
                                sMatch.event = newEvent
                                sMatch.match_number = match_num
                                sMatch.team = teamObject
                                sMatch.save()
        return render(request, 'scoutingapp/importeventfromtba.html', {'form':
                                                                       importform, 'done': importform.is_valid()})
    else:
        return HttpResponse("Not logged in")



def exporthtml(request, event_code):
    # print(tourn)
    matchlist = Match.objects.filter(tournament__event_code=event_code).order_by("match_number")
    output = []
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['Match Number','Scouted Team', 'Auto move', 'end game', 'robot card', 'scouted by', 'duplicate'])
    for m in matchlist:
        output.append([m.match_number, m.scouted_team, m.auto_move_yn, m.robot_end_game, m.robot_card, m.scouted_by, m.duplicate])
    writer.writerows(output)
    return response

def exportcubeshtml(request, event_code, begin, end):
    tourn = Tournament.objects.filter(event_code = event_code)
    cubeList = CubePlace.objects.filter(match__tournament = tourn).order_by("match__match_number", "match__scouted_team__team_number")
    output = []
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['Match number','team', 'acquired','scored','when','scouted_by'])
    for c in cubeList[int(begin):int(end)]:
        output.append([c.match, c.match.scouted_team, c.acquired, c.scored,c.when, c.scouted_by])
    writer.writerows(output)
    return response

def exportteam(request):
    teamlist = Team.objects.all().order_by("team_number")
    teams = TeamTable(teamlist)
    RequestConfig(request, paginate={'per_page': 9999}).configure(teams)
    return render(request, 'scoutingapp/exporthtml.html', {
        'rounds': teams
    })


def exportteambyevent(request, event_code):
    teamlist = Team.objects.filter(currently_in_event__event_code = event_code).order_by("team_number")
    teams = TeamTable(teamlist)
    RequestConfig(request, paginate={'per_page': 9999}).configure(teams)
    return render(request, 'scoutingapp/exporthtml.html', {
        'rounds': teams
    })

def exportusers(request):
    users = MyUser.objects.all();
    # enables ordering
    usertable = UserTable(users)
    RequestConfig(request).configure(usertable)

    return render(request, 'scoutingapp/exporthtml.html', {
        'rounds': usertable,
    })



def allianceexporthtml(request, event_code):
    matchlist = AllianceMatch.objects.all()
    matchlist = matchlist.filter(tournament__event_code=event_code)
    # enables ordering
    matches = AllianceMatchTable(matchlist)
    RequestConfig(request, paginate={'per_page': 9999}).configure(matches)

    return render(request, 'scoutingapp/exporthtml.html', {
        'rounds': matches,
    })
def gethoppertypes(request):
    path = os.path.join(settings.DJ_PROJECT_DIR, "hoppertypes.txt")
    print(path)
    val = ""
    with  open(path) as f:
        for line in f:
            print (line)
            val += line
    return HttpResponse(val, content_type='text/plain')

def getshottypes(request):
    path = os.path.join(settings.DJ_PROJECT_DIR, "goaltypes.txt")
    print(path)
    val = ""
    with  open(path) as f:
        for line in f:
            print (line)
            val += line
    return HttpResponse(val, content_type='text/plain')


def getveff(request):
    path = os.path.join(settings.DJ_PROJECT_DIR, "ballEfficiencies.txt")
    print(path)
    val = ""
    with  open(path) as f:
        for line in f:
            print (line)
            val += line
    return HttpResponse(val, content_type='text/plain')

def gearsource(request):
    path = os.path.join(settings.DJ_PROJECT_DIR, "gearSource.txt")
    print(path)
    val = ""
    with  open(path) as f:
        for line in f:
            print (line)
            val += line
    return HttpResponse(val, content_type='text/plain')


def geardropped(request):
    path = os.path.join(settings.DJ_PROJECT_DIR, "gearDropped.txt")
    print(path)
    val = ""
    with  open(path) as f:
        for line in f:
            print (line)
            val += line
    return HttpResponse(val, content_type='text/plain')


# def getcategories(request):
#     data = []
#     gear_choices = forms.auto_gear_choices
#     source_choices = forms.gear_c
#     end_games = EndGameState.objects.all()
#     cards = Card.objects.all()
#     for g,s,e,c in zip_longest(gear_choices, source_choices, end_games, cards):
#         values = {'gearpositions': (s or ["",])[0], 'gearsources':(g or ["",])[0], 'endgames' : (e or ""), 'cards' : (c or "")}
#         data.append(values)
#     print(type(data))
#     print(data)
#     table = CategoryTable(data)
#     return render(request, "scoutingapp/exportcategories.html", {"categories" : table})


def openhousepage(request):
    if request.method == 'POST':
        form = openHouseForm(request.POST)
        if form.is_valid():
            form.save()
            # proccess form
            messages.add_message(request, messages.INFO, 'Thank You. You will be contacted soon')
            return HttpResponseRedirect('/scoutingapp/openhouse')
        else:
            print(form.errors)
    else:
        form = openHouseForm()

    return render(
        request, 'scoutingapp/openhouse.html',
        {'form': form})

def api_teambyevent(request, event_code, match_id):
    teams = []
    print(match_id)
    print(event_code)
    if(int(match_id) < 1):
        teams = (Team.objects.filter(currently_in_event__event_code = event_code))
    else:
        matches = ScheduledMatch.objects.filter(match_number = match_id, event__event_code = event_code)
        teams = []
        for match in matches:
            teams.append(match.team)
    print(teams)
    data = serializers.serialize('json', teams)
    print(data)
    return HttpResponse(data, content_type="application/json")
