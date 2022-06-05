from django.views import View
from django.http import HttpResponse

import json

from .entities import IntSum, IntSub


class ViewWrapper(View):
    view_factory = None

    def get(self, request):
        body, status = self.view_factory.create().get(request.GET)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')
