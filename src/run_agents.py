from agent_no_bs.agent import LLMAgent
from agent_no_bs.environnement import Environnement

agent = LLMAgent()
env = Environnement()
env.add(agent)
print(env.objects)
print(env.agents)
#env.run()

