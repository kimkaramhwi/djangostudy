from django.urls import path

from owners.views import OwnersView, DogsView, OwnersDogsView

urlpatterns = [
    path('owners', OwnersView.as_view()),
    path('dogs', DogsView.as_view()),
    path('ownersdogs', OwnersDogsView.as_view())
]