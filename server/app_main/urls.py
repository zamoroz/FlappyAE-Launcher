from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import latest_version, NewsListView, SocialsListView, UpdateView

urlpatterns = [
    path("latest_version/<str:locale>/", latest_version),
    path("news/<str:locale>/", NewsListView.as_view()),
    path("socials/", SocialsListView.as_view()),
    path("update/<str:locale>/<str:version>/", UpdateView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
