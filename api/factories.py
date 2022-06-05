from .presenters import IntSumView, IntSubView

class IntSumViewFactory():

    @staticmethod
    def create():
        return IntSumView()

class IntSubViewFactory():

    @staticmethod
    def create():
        return IntSubView()