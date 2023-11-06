from abc import ABC, abstractmethod

class SubjetABC(ABC):

    @abstractmethod
    def attach(self, observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer) -> None:
        pass

    @abstractmethod
    def notify_observer(self) -> None:
        pass
