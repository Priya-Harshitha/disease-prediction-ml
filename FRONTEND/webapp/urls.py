from django.urls import path # type: ignore
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('input',views.input,name='input'),
    path('output',views.output,name='output')
]
