from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.show_all_objec),
    path("grups", views.Show_all_grups.as_view(), name='all_grups'),
    path("grups/<slug:slug>", views.DetailGrup.as_view(), name='one_grup'),
    path("grups/<slug:slug>/<int:n>", views.random_objecs, name='random_objecs'),
    path('__debug__/', include('debug_toolbar.urls')),
]

