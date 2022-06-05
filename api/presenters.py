from .entities import IntSum

class IntSumView():
    def get(self, data):
        try:
            operand1 = data['operand1']
            operand2 = data['operand2']
            sum = IntSum(operand1, operand2)
        except ValueError as e:
            body = e.args[0]
            status = 400
        else:
            body = sum.execute()
            status = 200

        return body, status