from django.urls import path

from .views import ViewWrapper
from .factories import IntSumViewFactory, IntSubViewFactory

app_name = 'api'

urlpatterns = [
    path('addition', ViewWrapper.as_view(view_factory=IntSumViewFactory)),
    path('substraction', ViewWrapper.as_view(view_factory=IntSubViewFactory))
]