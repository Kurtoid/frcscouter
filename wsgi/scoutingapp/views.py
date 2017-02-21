from django.utils.encoding import smart_str
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import (SignUpForm, LoginForm, ScoutingForm,
                    SortViewMatchForm, MatchNumberAttribs,
                    MatchViewFormMetaOptions, importTeamForm, importEventForm,
                    UserControlForm, AllianceScoutingForm, AllianceMatch)
from .models import (Match, Tournament, Team, CredentialsModel,
EndGameState, MyUser)
from django.contrib.auth import logout, login
from django.contrib import messages
from .tables import MatchTable, AllianceMatchTable, UserTable, VolleyTable, GearTable
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
from scoutingapp.models import Volley, Gear

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
        if request.method == 'POST':
            form = ScoutingForm(request.POST)
            form.use_required_attribute = False
            if form.is_valid():
                match = form.save(commit=False)
                match.scouted_by = request.user
                duped = 1
                duped_matches = Match.objects.filter(match_number=match.match_number, scouted_team=match.scouted_team).exclude(scouted_by=match.scouted_by)
                if(len(duped_matches)>0):
                    duped = len(duped_matches)+1
                match.duplicate=duped
                match.save()
                hopper_data = request.POST.get('fuel', 'no data')
                split_data = hopper_data.split(" ;");

                if(len(split_data)>0):
                    print(hopper_data)
                    for i in split_data:
                        tmp = i.split(" ")
                        if(len(tmp)==3):
                            print(tmp)
                            volley = Volley()
                            volley.ball_count = tmp[0]
                            volley.goal_type = tmp[1]
                            volley.accuracy= tmp[2]
                            volley.match = match;
                            volley.duplicate=duped
                            volley.save()

                gear_data= request.POST.get('gears_scout', 'no data')
                split_data = gear_data.split(" ;");
                if(len(split_data)>0):
                    print(gear_data)
                    for i in split_data:
                        tmp = i.split(" ")
                        if(len(tmp)==2):
                            print(tmp)
                            gear = Gear()
                            gear.source = tmp[0]
                            gear.dropped = tmp[1]
                            gear.match = match
                            gear.duplicate=duped
                            gear.save()
                        
#                         volley = Volley()
#                         volley.ball_count = tmp[0]
#                         volley.goal_type = tmp[1]
#                         volley.accuracy= tmp[2]
#                         volley.match = match;
#                         volley.save()
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
        form.use_required_attribute = False
        if request.session.get('fsetup'):
            return render(
                request, 'scoutingapp/scout.html',
                {'form': form, })
        return render(
            request, 'scoutingapp/scout.html',
            {'form': form, })
    else:
        return HttpResponseRedirect('/scoutingapp/userlogin/')


def alliance_scout(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = AllianceScoutingForm(request.POST)
            if form.is_valid():
                match = form.save(commit=False)
                match.scouted_by = request.user
                match.save()
                # proccess form
                messages.add_message(request, messages.INFO, 'Alliance Match Recorded')
                return HttpResponseRedirect('/scoutingapp/')
            else:
                print(form.errors)
        else:
            form = AllianceScoutingForm()

        if request.session.get('fsetup'):
            return render(
                request, 'scoutingapp/alliancescout.html',
                {'form': form
                })
        return render(
            request, 'scoutingapp/alliancescout.html',
            {'form': form})
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
                            if(r.json()['nickname'] is not None):
                                team = Team(team_number=x,
                                            team_name=r.json()['nickname'])
                                team.save()
                        if(r.json()['nickname'] is not None):
                            print('{}: {}'.format(x, r.json()['nickname']))
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
                # process and return redirect
                event_code = importform.cleaned_data['event_code']
                r = requests.get("http://www.thebluealliance.com/api/v2/event/{}".format(event_code),
                                 headers={'X-TBA-App-Id':
                                          'frc179:scoutingapp:v1'})
                try:
                    Tournament.objects.get(name=r.json()['name'])
                except ObjectDoesNotExist:
                    newEvent = Tournament(name=r.json()['name'])
                    newEvent.save()
                r = requests.get("http://www.thebluealliance.com/api/v2/event/{}/teams".format(event_code),
                                 headers={'X-TBA-App-Id':
                                          'frc179:scoutingapp:v1'})
                if r.status_code == 200:
                    print("Checking {}".format(event_code))
                    for x in r.json():
                        try:
                            Team.objects.get(team_number=x['team_number'])
                        except ObjectDoesNotExist:
                            print('we dont know '
                                  '{}'.format(x['nickname']))
                            if(x['nickname'] is not None):
                                team = Team(team_number=x['team_number'],
                                            team_name=x['nickname'])
                                team.save()
                        if(x['nickname'] is not None):
                            print('{}: {}'.format(
                                x['team_number'], x['nickname']))
        return render(request, 'scoutingapp/importeventfromtba.html', {'form':
                                                                       importform, 'done': importform.is_valid()})
    else:
        return HttpResponse("Not logged in")



def exporthtml(request, team_number):
    matchlist = Match.objects.all()
    matchlist = matchlist.filter(scouted_by__team__team_number=team_number)
    # enables ordering
    matches = MatchTable(matchlist)
    RequestConfig(request, paginate={'per_page': 9999}).configure(matches)

    return render(request, 'scoutingapp/exporthtml.html', {
        'rounds': matches,
    })


def exportballs(request, team_number):
    volleylist = Volley.objects.all()
#     volleylist = volleylist.filter(scouted_by__team__team_number=team_number)
    # enables ordering
    volleys= VolleyTable(volleylist)
    RequestConfig(request, paginate={'per_page': 9999}).configure(volleys)

    return render(request, 'scoutingapp/exporthtml.html', {
        'rounds': volleys,
    })

def exportgears(request, team_number):
    gearlist = Gear.objects.all()
#     volleylist = volleylist.filter(scouted_by__team__team_number=team_number)
    # enables ordering
    gears= GearTable(gearlist)
    RequestConfig(request, paginate={'per_page': 9999}).configure(gears)

    return render(request, 'scoutingapp/exporthtml.html', {
        'rounds': gears,
    })

def exportusers(request):
    users = MyUser.objects.all();
    # enables ordering
    usertable = UserTable(users)
    RequestConfig(request).configure(usertable)

    return render(request, 'scoutingapp/exporthtml.html', {
        'rounds': usertable,
    })



def allianceexporthtml(request, team_number):
    matchlist = AllianceMatch.objects.all()
    matchlist = matchlist.filter(scouted_by__team__team_number=team_number)
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
