from abc import ABCMeta, abstractmethod
from uuid import uuid4


class Repository(metaclass=ABCMeta):

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def create(self, obj):
        pass

    @abstractmethod
    def delete(self, obj):
        pass


class InMemoryRepository(Repository):

    def __init__(self):
        self._objects = []

    def get(self, id):
        return next((obj for obj in self._objects if obj.id == id), None)

    def store(self, obj):
        assert getattr(obj, 'id', None) is None
        assert isinstance(obj, self.model)

        obj.id = str(uuid4())
        self._objects.append(obj)
