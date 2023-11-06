from main.model import Book
from main.model import Library
from main.subject import AlarmBook
from main.observer import Administration
from main.observer import Stock
from main.observer import Shopping


class Cliente():

    def run(self):
        alarma = AlarmBook()
        alarma.attach(Administration())
        alarma.attach(Stock())
        alarma.attach(Shopping())
        book = Book("Bueno", "Design Pattern")
        book.setState("MALO")
        library = Library(alarma)
        library.returnsBook(book)