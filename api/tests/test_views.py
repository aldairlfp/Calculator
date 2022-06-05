from django.test import SimpleTestCase
from django.urls import reverse

import random


class IntSumViewTest(SimpleTestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/addition?operand1=1&operand2=1')
        self.assertEqual(response.status_code, 200)

    def test_intsum(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        good_result = True
        for i in range(100):
            operand1 = str(random.randint(-100, 100))
            operand2 = str(random.randint(-100, 100))
            url = '/addition?operand1={}&operand2={}'.format(operand1, operand2)
            response = self.client.get(url)
            if response.json()['result'] != int(operand1) + int(operand2):
                good_result = False
                break
        self.assertTrue(good_result)

class IntSumViewTest(SimpleTestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/addition?operand1=1&operand2=1')
        self.assertEqual(response.status_code, 200)

    def test_intsum(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        good_result = True
        for i in range(100):
            operand1 = str(random.randint(-100, 100))
            operand2 = str(random.randint(-100, 100))
            url = '/substraction?operand1={}&operand2={}'.format(operand1, operand2)
            response = self.client.get(url)
            if response.json()['result'] != int(operand1) - int(operand2):
                good_result = False
                break
        self.assertTrue(good_result)