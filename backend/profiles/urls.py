from django.urls import path

from .views import *

urlpatterns = [
    path("<int:pk>/", ProfileDetail.as_view()),
    path("update/<int:pk>/", ProfileUpdateView.as_view()),
    path("adverts/", UserAdvertList.as_view()),
    path("update-advert/<int:pk>/", UserAdvertUpdate.as_view()),
]
