from django.urls import path
from .views import GetRedirect, CreateNewShort

urlpatterns = [
    path('to/<str:hash>/', GetRedirect.as_view(), name='short_url'),
    path('create/', CreateNewShort.as_view(), name='create_short')
]