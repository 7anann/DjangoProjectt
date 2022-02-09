from django.urls import path
from .views import *
app_name = "projects"
urlpatterns = [
    path('', index),
    path("home", index, name="home"),
    path("categorie/<int:cid>", view, name="show"),
    path("search", search, name="search"),
    path("details/<int:pid>", details, name="detail"),

]
