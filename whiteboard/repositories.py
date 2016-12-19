from abc import ABCMeta, abstractmethod
from uuid import uuid4

from whiteboard.models.workout import Workout


class Repository(metaclass=ABCMeta):

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def store(self, obj):
        pass

    @abstractmethod
    def get_all(self):
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

    def get_all(self):
        return self._objects


class Repositories:
    def __init__(self):
        self.workouts = WorkoutRepository()


class WorkoutRepository(InMemoryRepository):
    model = Workout
