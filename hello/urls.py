from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("Jacob/", views.Jacob, name="Jacob"),
    path("Dorcas/", views.Dorcas, name="Dorcas"),
    path("isChristmas/", views.is_christmas, name="is_christmas"),
    # path("<str:name>/", views.welcome, name="welcome"),
]
