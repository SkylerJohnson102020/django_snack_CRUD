from django.urls import path
from .views import AboutView, GearCreateView, GearDeleteView, GearDetailView, GearListView, GearUpdateView

urlpatterns = [
    path("", GearListView.as_view(), name='gear_list'),
    path("<int:pk>/", GearDetailView.as_view(), name='gear_detail'),
    path("create/", GearCreateView.as_view(), name='gear_create'),
    path("<int:pk>/update/", GearUpdateView.as_view(), name='gear_update'),
    path("<int:pk>/delete/", GearDeleteView.as_view(), name='gear_delete'),
    path("about/", AboutView.as_view(), name='about'),
]