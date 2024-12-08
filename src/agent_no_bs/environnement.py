import logging

from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from agent_no_bs.agent import Agent

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")

class Observation:
    def __init__(self):
        pass
    def __str__(self) -> str:
        return "Observation content"

class ObservableObject:
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
        logging.debug(observation)
        return observation
    
@dataclass
class Environnement:
    objects: list[ObservableObject] = field(default_factory=list)
    agents: list[Agent] = field(default_factory=list)

    def run(self, max_turns: int):
        for turn in range(max_turns):
            for observable in self.objects:
                observable.update()

    def add(self, new_object: ObservableObject) -> None:
        if isinstance(new_object, ObservableObject):
            self.objects.append(new_object)
        elif isinstance(new_object, Agent):
            self.agents.append(new_object)
        else:
            raise KeyError(f"{new_object} couldn't be added to the environnement.")
