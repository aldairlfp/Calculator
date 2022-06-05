from abc import ABC, abstractmethod

from .entities import IntSum, IntSub


class IntBinaryOperationView(ABC):
    def get(self, operand1, operand2):
        try:
            operation = self.operation(operand1, operand2)
        except ValueError as e:
            body = {'error': e.args[0]}
            status = 400
        else:
            body = {'result': operation}
            status = 200

        return body, status

    def operation(self, operand1, operand2):
        pass


class IntSumView(IntBinaryOperationView):
    def operation(self, operand1, operand2):
        return IntSum(operand1, operand2).execute()


class IntSubView(IntBinaryOperationView):
    def operation(self, operand1, operand2):
        return IntSub(operand1, operand2).execute()
