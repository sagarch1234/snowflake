from django.urls import path

from advertisement.views import CreateAdvertisementView, ListAdvertisementView, EnableDisableAdvertisementView, ShowAdvertisementsView


urlpatterns = [
    path('create-advertisement/', CreateAdvertisementView.as_view()),
    path('list-advertisement/', ListAdvertisementView.as_view()),
    path('endable-disable-advertisement/', EnableDisableAdvertisementView.as_view()),
    path('show-advertisements/', ShowAdvertisementsView.as_view())
]