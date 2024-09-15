from django.urls import path
from .views import UsuarioListView, UsuarioDetailView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView
from .views import ClaseListView, ClaseDetailView, ClaseCreateView, ClaseUpdateView, ClaseDeleteView

urlpatterns = [
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),
    path('usuarios/nuevo/', UsuarioCreateView.as_view(), name='usuario-create'),
    path('usuarios/<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario-update'),
    path('usuarios/<int:pk>/eliminar/', UsuarioDeleteView.as_view(), name='usuario-delete'),
    
    # CRUD para Clase
    path('clases/', ClaseListView.as_view(), name='clase-list'),
    path('clases/<int:pk>/', ClaseDetailView.as_view(), name='clase-detail'),
    path('clases/nueva/', ClaseCreateView.as_view(), name='clase-create'),
    path('clases/<int:pk>/editar/', ClaseUpdateView.as_view(), name='clase-update'),
    path('clases/<int:pk>/eliminar/', ClaseDeleteView.as_view(), name='clase-delete')
]