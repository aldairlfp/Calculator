from django.views import View
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

import json

from .entities import IntSum, IntSub


class BinaryViewWrapper(View):
    view_factory = None

    def get(self, request):
        try:
            operand1 = request.GET['operand1']
            operand2 = request.GET['operand2']
        except MultiValueDictKeyError:
            body = {'error': 'The parameters operand1 and operand2 must exist.'}
            status = 400
        else:
            body, status = self.view_factory.create().get(operand1, operand2)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')
