from abc import ABCMeta, abstractmethod

class BookBadConditionABC(metaclass=ABCMeta):

    @abstractmethod
    def update(self) -> None:
        pass
