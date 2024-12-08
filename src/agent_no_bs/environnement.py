import logging

from dataclasses import dataclass, field
from typing import Any

from agent_no_bs.agent import Agent
from agent_no_bs.objects import ObservableObject

@dataclass
class Environnement:
    objects: list[ObservableObject] = field(default_factory=list)
    agents: list[Agent] = field(default_factory=list)

    def run(self, max_turns: int):
        for turn in range(max_turns):
            for observable in self.objects:
                observable._update()
            for agent in self.agents:
                agent.observe(self.objects)

    def add(self, new_object: ObservableObject) -> None:
        if isinstance(new_object, ObservableObject):
            self.objects.append(new_object)
        elif isinstance(new_object, Agent):
            self.agents.append(new_object)
        else:
            raise KeyError(f"{new_object} couldn't be added to the environnement.")
