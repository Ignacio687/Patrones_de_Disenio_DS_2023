from . import BookBadConditionABC

class Stock(BookBadConditionABC):

    def update(self) -> None:
        print("Stock:")
        print("Se da de baja al libro y se manda a reparación o reposición...")
