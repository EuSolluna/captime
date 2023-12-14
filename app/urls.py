from django.urls import path
from .views import login_view
from .views import MinhaViewDeInicio

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', login_view.as_view(), name='login'),
    # Adicione outras URLs conforme necessário
]