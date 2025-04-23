from django.urls import path
from .views import yu_gi_oh_calculator


urlpatterns = [
    path('', yu_gi_oh_calculator, name='yu_gi_oh_calculator')
]
