from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Local imports:
from forms import LoginForm
from models import AuthImapServer

def loginView(request):
if request.method == 'POST':
    form = LoginForm(request.POST)
if form.is_valid():
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    next = form.cleaned_data['next']
try:
    imap_host= AuthImapServer.objects.get(id=int(form.cleaned_data['host']))
    host = imap_host.host
    port = imap_host.port
    ssl = imap_host.is_ssl
except:
    return render_to_response('usuarios/login.html',{ 'form': form,'error_message': _('Invalid server. '\'Please try again.') })
try:
    user = authenticate(username=username, password=password, host=host, port=port, ssl=ssl)
except ValueError:
    return render_to_response('usuarios/login.html',{ 'form': form,'error_message': _('Invalid login. '\'Please try again.') })
if user is not None:
    if user.is_active:
        login(request, user)

        # Not an imap user:
        if request.session['_auth_user_backend'] == \'django.contrib.auth.backends.ModelBackend':
            return render_to_response('usuarios/login.html',{ 'form': form,'error_message': _('This is not an IMAP ' \'valid account. Please try again.') })
        request.session['username'] = username
        request.session['password'] = password
        request.session['host'] = host
        request.session['port'] = port
        request.session['ssl'] = ssl
        return HttpResponseRedirect(next)
# Disabled account:
else:
    return render_to_response('usuarios/login.html',{ 'form': form,'error_message': _('Sorry, disabled ' \'account.') })
# Invalid user:
else:
    return render_to_response('usuarios/login.html',{ 'form': form,'error_message': _('Invalid login. Please ' \'try again.') })
# Invalid form:
else:
    return render_to_response('usuarios/login.html',{ 'form': form })
# Display the empty form:
else:
try:
    next = request['next']
    if next == '': next = settings.LOGIN_SUCCESS
    except:
        next = settings.LOGIN_SUCCESS
        data = { 'next': next }
        form = LoginForm(data)
        return render_to_response('usuarios/login.html',{ 'form': form })

def logoutView(request):
    request.session.modified = True
    logout(request)
# Redirect to a success page.
return HttpResponseRedirect(settings.LOGOUT_SUCCESS)

