from abc import ABC, abstractmethod
from agent_no_bs.observation import Observation

class ObservableObject(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def _observe(self, sensor) -> Observation:
        pass
    
    @abstractmethod
    def _update(self):
        pass
    
    def observe(self, sensor) -> Observation:
        observation = self._observe(sensor)
        logging.info(observation)
        return observation

class Document(ObservableObject):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def _update(self):
        pass

    def _observe(self, sensor) -> Observation:
        return sensor(self)