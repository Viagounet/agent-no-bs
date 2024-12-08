from abc import ABC, abstractmethod
from agent_no_bs.sensors import Sensor

class Agent(ABC):
    def __init__(self, sensors: list[Sensor]):
        self.sensors = sensors

class LLMAgent(Agent):
    def __init__(self, sensors: list[Sensor]):
        super().__init__(sensors)

    def observe(self, objects):
        for sensor in self.sensors:
            for object in objects:
                sensor.evaluate(object)

