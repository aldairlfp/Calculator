from abc import ABC, abstractmethod


class Operation(ABC):
    def __init__(self, *args) -> None:
        self._operands = []
        for i in args:
            self._operands.append(i)

    @abstractmethod
    def execute(self):
        pass


class BinaryOperation(Operation, ABC):
    def __init__(self, operand1, operand2) -> None:
        super().__init__(operand1, operand2)

    def get_operand1(self):
        return self._operands[0]

    def get_operand2(self):
        return self._operands[1]


class IntBinaryOperation(BinaryOperation, ABC):
    def __init__(self, operand1, operand2) -> None:
        try:
            _operand1 = int(operand1)
            _operand2 = int(operand2)
        except ValueError:
            raise ValueError('The operands must be integers')
        super().__init__(_operand1, _operand2)


class IntSum(IntBinaryOperation):
    def execute(self):
        return self.get_operand1() + self.get_operand2()


class IntSub(IntBinaryOperation):
    def execute(self):
        return self.get_operand1() - self.get_operand2()