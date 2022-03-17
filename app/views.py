
from cgi import print_arguments
from datetime import datetime
from pyexpat import model
from typing import ContextManager
from urllib import request
from venv import create
from django.conf import settings
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login,get_user_model
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.db.models import Q
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView
from .models import *
from .forms import *

User = get_user_model()
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
    context["habilidades"] = Habilidades.objects.filter(user_id=request.user.id).select_related('tipoTrabajo')
    return render(request,"app/myaccount.html", context)

@login_required
def upload_image_User_view(request):

    foto= User.objects.get(user_id=request.user.id)
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

# Update
class User_edit(LoginRequiredMixin,BSModalUpdateView):
    model=User
    template_name = 'app/User_Edit.html'
    form_class = UserEditForm
    success_message = '¡Se Modifico correctamente!'
    success_url = reverse_lazy('myaccount')

    def get_object(self):
        return User.objects.get(id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(User_edit, self).get_context_data(**kwargs)
        if 'form' not in context: context['form'] = self.form_class(self.request.GET,instance=self.request.user)
        return context

    def form_valid(self, form):
        if not self.request.is_ajax():
            form.save(commit=True)
        return super().form_valid(form)

class Create_habili(LoginRequiredMixin,BSModalCreateView):
    template_name = 'app/Create-Habilidad.html'
    form_class = habilidadesFullForm
    success_message = '¡Se agrego correctamente!'
    success_url = reverse_lazy('myaccount')

    def form_valid(self, form):
        files = self.request.FILES.getlist('images')
        if not self.request.is_ajax():
            form.instance.user_id = self.request.user.id
            obj = form.save(commit=True)
            for f in files:
                FotoTrabajo.objects.create(habilidad=obj,fotoTrabajo=f)
        return super().form_valid(form)

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

def Busquedaanunciofuncion(id):
    context ={}
    habilidades = Habilidades.objects.select_related('tipoTrabajo','user').get(id=id)
    context["habilidades"] = habilidades
    context["favorito"] = Favoritos.objects.filter(habilidad__id=id).count()
    context["clasifiacion"] = Clasifiacion.objects.select_related('user').filter(habilidad_id=id)
    return context

def Busquedaanuncio(request, id):
    return render(request,"app/Perfilanuncio.html", Busquedaanunciofuncion(id))

@login_required
def Favorito(request):
    idhabi= request.POST['txtCodigo']
    try:
        favo = Favoritos.objects.get(user_id=request.user.id,habilidad_id=idhabi)
        favo.delete()
        messages.info(request, 'Se elimino de tu favorito')
    except Favoritos.DoesNotExist:
        Favoritos.objects.create(fecha=datetime.now(),user_id=request.user.id,habilidad_id=idhabi)
        messages.success(request, 'Se agrego en tu favorito')

    return redirect ('Perfil_list',idhabi)

@login_required
def Realizar_Pedido(request):
    idhabi= request.POST['id']
    Pedido.objects.create(fecha=datetime.now(),user_id=request.user.id,habilidad_id=idhabi,estado='Pendiente')
    messages.success(request, 'Solicitastes los servicios')
    return redirect ('Perfil_list',idhabi)

class Pedidos(LoginRequiredMixin,ListView):
    template_name = 'app/Pedidos.html'
    context_object_name = 'Pedido'

    def get_context_data(self, **kwargs):
        context = super(Pedidos, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        queryset = Pedido.objects.select_related('habilidad','user').filter(Q(habilidad__user__id=self.request.user.id) | Q(user_id=self.request.user.id) )
        return queryset

def obtenerpedido(estado,id):
    return Pedido.objects.filter(id=id).update(estado=estado)

@login_required
def AceptarSolicitud(request):
    idpedido= request.POST['IdCodigo']
    if "cancel" in request.POST:
        obtenerpedido('Cancelado',idpedido)
    else: 
        obtenerpedido('Aceptado',idpedido)

    return redirect ('Pedidos')

@login_required
def CancelarSolicitud(request):
    idpedido= request.POST['IdCodigo']
    obtenerpedido('Cancelado',idpedido)

    return redirect ('Pedidos')

@login_required
def Detalle_Pedido(request, id):
    context ={}
    context["Pedido"] = Pedido.objects.select_related('habilidad','user').get(id=id)
    return render(request,"app/DetallePedido.html", context)   

@login_required
def Valorizacion_Pedido(request, id):
    context ={}
    habilid = Pedido.objects.select_related('habilidad','user').get(id=id)

    if request.method == "POST":
        formClasificacion = ValoracionFullForm(request.POST,request.FILES,instance=Clasifiacion(user=request.user,habilidad=habilid.habilidad))
        files = request.FILES.getlist('fotoValoracion')
        if formClasificacion.is_valid():
            Valora=formClasificacion.save(commit=True)
            obtenerpedido("Finalizado",id)
            for f in files:
                FotoValoracion.objects.create(clasifiacion=Valora,fotoValoracion=f)
            messages.success(request, '¡Se agrego correctamente!')
            return redirect ('Pedidos')
    else :
        formClasificacion = ValoracionFullForm(request.FILES,instance=Clasifiacion(user=request.user,habilidad=habilid.habilidad))

    context["formClasificacion"] = formClasificacion
    context["pedido"] = id
    return render(request,"app/ValoracionPedido.html", context)    
	