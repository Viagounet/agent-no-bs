from agent_no_bs.agent import LLMAgent
from agent_no_bs.environnement import Environnement
from agent_no_bs.objects import Document
from agent_no_bs.sensors import DocumentSensor

agent = LLMAgent(sensors=[DocumentSensor()])
env = Environnement()
env.add(agent)
env.add(Document("my_path"))
env.run(max_turns=1)