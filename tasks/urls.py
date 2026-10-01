from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/plot-data/", views.get_plot_data, name="plot_data"),
]