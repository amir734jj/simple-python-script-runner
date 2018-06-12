from abc import ABC, abstractmethod


class AbstractTask(ABC):
    @abstractmethod
    def run(self):
        pass


class Amir(AbstractTask):
    def run(self):
        pass

    def __init__(self):
        pass