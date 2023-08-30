from django.urls import path
from .views import WineListView, WineCreateView, WineUpdateView, WineDeleteView

app_name = "vinventory"

urlpatterns = [
    path("wine_list/", WineListView.as_view(), name="wine_list"),
    path("wine/add/", WineCreateView.as_view(), name="wine_add"),
    path("wine/<int:pk>/update/", WineUpdateView.as_view(), name="wine_update"),
    path("wine/<int:pk>/delete/", WineDeleteView.as_view(), name="wine_delete"),
    # Add more URL patterns for other views
]
