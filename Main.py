from LGymClient import agentLoop
from BaseAgent import BaseAgent
from SmartAgent import SmartAgent

print("Comienza el funcionamiento del agente")
agent = SmartAgent("1","Isma")
agentLoop(agent,False)


