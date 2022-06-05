from django.urls import path

from .views import BinaryViewWrapper
from .factories import IntSumViewFactory, IntSubViewFactory

app_name = 'api'

urlpatterns = [
    path('addition', BinaryViewWrapper.as_view(view_factory=IntSumViewFactory)),
    path('substraction', BinaryViewWrapper.as_view(view_factory=IntSubViewFactory))
]