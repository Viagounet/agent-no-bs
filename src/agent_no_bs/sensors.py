from abc import ABC, abstractmethod
import logging
from agent_no_bs.objects import Document
from agent_no_bs.observation import Observation

logging.basicConfig(level=logging.INFO, filemode="w")


class Sensor:
    def __init__(self):
        pass

    @abstractmethod
    def _evaluate(self, object) -> Observation:
        pass
    
    def evaluate(self, object) -> Observation:
        observation = self._evaluate(object)
        logging.info(observation)
        return observation

class DocumentSensor(Sensor):
    def __init__(self):
        pass
    
    def _evaluate(self, document: Document) -> Observation:
        if not isinstance(document, Document):
            return Observation(infos={"sensor_failure": "DocumentSensor tried to evaluate an object that is not a document"})
        return Observation(infos={"document": document.path})