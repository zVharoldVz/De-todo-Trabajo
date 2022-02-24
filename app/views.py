
from typing import ContextManager
from django.conf import settings
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from .models import *
from .forms import *

# Create your views here.
def app(request):
    return render(request,"app/index.html")

class Login(LoginView):
    authentication_form = CustomAuthenticationForm
    form_class = CustomAuthenticationForm
    template_name = 'app/login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        login(self.request, form.get_user())
        if remember_me:
            self.request.session.set_expiry(1209600)
        return super(LoginView, self).form_valid(form)

def usuario_new(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect ('app')

    else :
        form = UserRegisterForm()

    context = {'form_user': form}
    return render(request,"app/UserNew.html",context)

@login_required
def myaccount(request):
    context ={}
    context["ExtraDato"] = ExtraDato.objects.get(user_id=request.user.id)
    context["Foto_perfil"] = Foto_perfil.objects.get(user_id=request.user.id)
    context["habilidades"] = Habilidades.objects.filter(user_id=request.user.id).select_related('tipoTrabajo')

    return render(request,"app/myaccount.html", context)

@login_required
def upload_image_User_view(request):

    foto= Foto_perfil.objects.get(user_id=request.user.id)
    if request.method == "POST":
        form = UploadImageusaerForm(request.POST, request.FILES,instance=foto)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, '¡Se agrego correctamente!')
            return redirect ('myaccount')
        else:
            messages.error(request, '¡Error !')
            return redirect ('myaccount')
    else :
        form = UploadImageusaerForm(request.FILES,instance=foto)

    context = {'form_user_upload': form}

    return render(request,"app/UploadImageusaer.html",context)

@login_required
def User_edit(request):
    context ={}
    extra = ExtraDato.objects.get(user_id=request.user.id)
    form = UserEditForm(request.POST,instance = request.user)
    formExtra  = ExtraEditForm(request.POST,instance = extra)
    if request.method == 'POST':
        #if form.is_valid():
        if form.is_valid() and formExtra.is_valid():
            form.save(commit=True)
            formExtra.save(commit=True)
            messages.success(request, '¡Se Modifico correctamente!')
            return redirect ('myaccount')
    else :
        form = UserEditForm(instance = request.user)
        formExtra = ExtraEditForm(instance = extra)

    context["form"] = form
    context["formExtra"] = formExtra 
    return render(request,"app/User_Edit.html", context) 

@login_required
def Create_habili(request):
    context ={}
    if request.method == "POST":
        formhabilidades = habilidadesFullForm(request.POST,request.FILES,instance=Habilidades(user=request.user))
        files = request.FILES.getlist('images')
        if formhabilidades.is_valid():
            habili=formhabilidades.save(commit=True)
            for f in files:
                FotoTrabajo.objects.create(habilidad=habili,fotoTrabajo=f)
            messages.success(request, '¡Se agrego correctamente!')
            return redirect ('myaccount')
    else :
        formhabildades = habilidadesFullForm(request.FILES,instance=Habilidades(user=request.user))


    context["formhabildades"] = formhabildades
    return render(request,"app/Create-Habilidad.html", context)

@login_required
def Habili_delete(request, id):
    Habilidades.objects.get(id=id,user_id=request.user.id).delete()
    messages.warning(request, 'Se elimino correctamente')
    return redirect ('myaccount')

@login_required
def Habili_edit(request, id):
    context ={}
    Habili = Habilidades.objects.get(id=id,user_id=request.user.id)


    files = request.FILES.getlist('images')
    if request.method == 'POST':
        formhabilidadesEdi = habilidadesFullForm(request.POST,request.FILES or None,instance=Habili)
        if formhabilidadesEdi.is_valid():
            formhabilidadesEdi.save(commit=True)
            FotoTrabajo.objects.filter(habilidad_id = Habili.id).delete()

            for f in files:
                FotoTrabajo.objects.create(habilidad=Habili,fotoTrabajo=f)

            messages.success(request, '¡Se Modifico correctamente!')
            return redirect ('myaccount')
    else :
        formhabilidadesEdi = habilidadesFullForm(request.FILES or None,instance=Habili)

    context["idhabilidad"] = Habili.id
    context["formhabilidadesEdi"] = formhabilidadesEdi
    return render(request,"app/Edit-Habilidad.html", context)   

class Busqueda(ListView):
    template_name = 'app/Busqueda.html'
    context_object_name = 'habilidades'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(Busqueda, self).get_context_data(**kwargs)
        context['valor'] = self.request.GET.get("busqueda")
        return context

    def get_queryset(self):
        Valor = self.request.GET.get("busqueda")
        queryset = Habilidades.objects.filter(nombrehabilidad__contains=(Valor)).select_related('tipoTrabajo','user')
        if self.request.GET.get("browse"):
            selection = self.request.GET.get("browse")
            if selection == "0":
                queryset =  Habilidades.objects.filter(nombrehabilidad__contains=("Asdasd")).select_related('tipoTrabajo','user')
            elif selection == "1":
                queryset =  Habilidades.objects.filter(nombrehabilidad__contains=("251")).select_related('tipoTrabajo','user')
            elif selection == "2":
                queryset = Habilidades.objects.filter(nombrehabilidad__contains=("harold")).select_related('tipoTrabajo','user')
        return queryset


def Busquedaanuncio(request, id):
    context ={}
    habilidades = Habilidades.objects.select_related('tipoTrabajo','user').get(id=id)
    context["habilidades"] = habilidades
    context["Foto_perfil"] = Foto_perfil.objects.get(user_id=habilidades.user.id)
    return render(request,"app/Perfilanuncio.html", context)



def prueba(request):
    context ={}
    if request.method == "POST":
        form = habilidadesfrom(request.POST,instance=Habilidades(user=request.user))
        if form.is_valid():
            form.save(commit=False)

            return redirect ('prueba')
    else :
        form = habilidadesfrom(instance=Habilidades(user=request.user))
    context["form_prueba"] = form

    return render(request,"app/prueba.html",context)