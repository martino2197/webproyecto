from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = 'padmex'

urlpatterns = [
    # /padmex/
    path('', views.IndexView.as_view(), name='index'),
    path('olimpicas', views.VerOlimpicas.as_view(), name="olimpicas"),
    path('residenciales', views.VerResidenciales.as_view(), name="residenciales"),
    path('productos', views.VerProductos.as_view(), name="productos"),
    re_path(r'^productos/(?P<pk>[0-9]+)/$', views.DetailViews.as_view(), name='detail'),
    #path(r'productos/add/$', views.UserCreate.as_view(), name='cliente-add'),
]
