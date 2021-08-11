from django.urls import path, include
from .views import *
from  django.conf.urls import url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'django'

urlpatterns = [
    path('', index, name="home"),
    path('create/', Create.as_view(template_name="card_form.html"), name="create"),
    path('update/<int:pk>/', UpdateViews.as_view(template_name="card_form.html"), name="update"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
