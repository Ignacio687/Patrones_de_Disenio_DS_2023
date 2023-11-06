from . import Book
from main.subject import AlarmBook

class Library():

    def __init__(self, alarmBook: AlarmBook) -> None:
        self.alarmBook = alarmBook

    def returnsBook(self, book: Book) -> None:
        if book.getState() == "MALO":
            self.alarmBook.notify_observer()