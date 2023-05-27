from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.main, name='main'),
    #path('secuencial/<str:texto_1>&<str:texto_2>', views.secuencial),
    path('secuencial',views.secuencial, name='secuencial')
]