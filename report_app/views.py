from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import relatorios
from django.contrib.auth.forms import UserChangeForm


# Create your views here.
@login_required
def home(request):
    template = loader.get_template('index.html')
    myrelat = relatorios.objects.all()
    contexto = {
        'myrelat' : myrelat,
    }
    return HttpResponse(template.render(contexto, request))


@login_required
def exibe_relatorio(request, id):
    temaplate = loader.get_template('relatorio.html')
    myrelat = relatorios.objects.get(id=id)
    contexto = {
        'myrelat' : myrelat,
    }
    return HttpResponse(temaplate.render(contexto, request))

