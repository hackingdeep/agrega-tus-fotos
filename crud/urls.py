from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('',views.inicio,),
     path('registro_usuario/',views.registro_usuario,name='registro_usuario'),
     path('iniciar_sesion/',views.iniciar_sesion,name='iniciar_sesion'),
     path('cerrar_sesion/',views.cerrar_sesion,name='cerrar_sesion'),
     path('eliminar_usuario/<int:id>',views.eliminarusuario,name='eliminar'),
     path('actualizar_usuario/<int:id>',views.actualizar,name='actualizar'),
     path('cambiar_contraseña/<int:id>',views.cambiar_contraseña,name='cambiar_contraseña'),
     path('agregar_imagen/<int:id>',views.agregar_imagen,name='agregar_imagen')

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)