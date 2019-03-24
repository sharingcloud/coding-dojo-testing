from django.urls import re_path
from django.views.generic.base import RedirectView

from . import api, views

urlpatterns = [
    re_path(r"^login$", views.login, name="login"),
    re_path(r"^logout$", views.logout, name="logout"),
    re_path(r"^home$", views.home, name="home"),

    re_path(r"^api/clickme$", api.clickme, name="api-clickme"),

    re_path(r"", RedirectView.as_view(url='home'), name="home-redirect"),
]
