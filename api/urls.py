from django.urls import path

from .views import ViewWrapper
from .factories import IntSumViewFactory

app_name = 'api'

urlpatterns = [
    path('addition', ViewWrapper.as_view(view_factory=IntSumViewFactory))
]