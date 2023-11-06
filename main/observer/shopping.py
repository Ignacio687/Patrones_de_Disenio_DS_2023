from . import BookBadConditionABC

class Shopping(BookBadConditionABC):

    def update(self) -> None:
        print("Compras:")
        print("Solicito cotización de reparación o reposición de libro...")
