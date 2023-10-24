from django.urls import path
# Views
from fastapp import views

urlpatterns = [

    path(
        route='', 
        view=views.FastAppView.as_view(),
        name='test'
    ),

]