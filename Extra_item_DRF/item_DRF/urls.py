from django.urls import path, include
from item_DRF.views import Show_all_grups, Show_all_objecs, DetailGrup, Random_objecs

urlpatterns = [
    path("grups", Show_all_grups.as_view(), name='all_grups'),
    path("objecs", Show_all_objecs.as_view(), name='all_objecs'),
    path("grups/<slug:slug>", DetailGrup.as_view(), name='one_grup'),
    path("grups/<slug:slug>/<int:n>", Random_objecs.as_view(), name='random_objecs'),
]
