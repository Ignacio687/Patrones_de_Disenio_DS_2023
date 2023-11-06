from main.observer import BookBadConditionABC
from . import SubjetABC

class AlarmBook(SubjetABC):
    def __init__(self) -> None:
        self.observers = []

    def attach(self, observer: BookBadConditionABC) -> None:
        self.observers.append(observer)

    def detach(self, observer: BookBadConditionABC) -> None:
        self.observers.remove(observer)

    def notify_observer(self) -> None:
        for observer in self.observers:
            observer.update()
