from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import SignUpForm, LoginForm, ScoutingForm, FieldSetupForm
from .models import FieldSetup
from django.contrib.auth import logout, login
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

        return render(request, 'scoutingapp/fieldsetupcontrol.html', {'form': form})
    else:
        return HttpResponseRedirect('/scoutingapp/userlogin')


def userlogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.getuser())
            if(request.user.is_authenticated()):
                print("auth done")
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
            form.scouted_by=request.user
            form.save()
            # proccess form
            return HttpResponseRedirect('/scoutingapp/signupcomplete/')
    else:
        form = SignUpForm()

    return render(request, 'scoutingapp/signup.html', {'form': form})


def logincomplete(request):
    if request.user.is_authenticated():
        return render(request, 'scoutingapp/logincomplete.html', {'user': request.user})
    else:
        return HttpResponse("user not logged in!")


def signupcomplete(request):
    return HttpResponse('DONE!')


def usercontrolpanel(request):
    if request.user.is_authenticated():
        return render(request, 'scoutingapp/usercontrolpanel.html', {'user':
                                                                      request.user})
    return HttpResponse("usercontrolpanel")


def logoutuser(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect("/scoutingapp/")


def scout(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = ScoutingForm(request.POST)
            if form.is_valid():
                match = form.save(commit=False)
                match.scouted_by = request.user
                if request.session.get('fsetup'):
                    print(request.session.get('fsetup'))
                    match.field_setup = FieldSetup.objects.get(id=request.session['fsetup'])
                match.save()
                # proccess form
                return HttpResponseRedirect('/scoutingapp/')
            else:
                print(form.errors)
        else:
            form = ScoutingForm()

        if request.session.get('fsetup'):
            return render(request, 'scoutingapp/scout.html', {'form': form,
                                                              'setupkey':
                                                              FieldSetup.objects.get(id=request.session.get('fsetup'))})
        return render(request, 'scoutingapp/scout.html', {'form': form})
    else:
        return HttpResponseRedirect('/scoutingapp/userlogin')
