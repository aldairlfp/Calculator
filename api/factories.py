from .presenters import IntSumView

class IntSumViewFactory():

    @staticmethod
    def create():
        return IntSumView()