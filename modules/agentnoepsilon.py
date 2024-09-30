#Реализуем не жадную стратегию. В таком случае Q-стратегия = SARSA стратегия

from agentq import AgentQ

class AgentNoEpsilon(AgentQ):
    def __init__(self):
        super().__init__()
        # Обнуляем эпсилон
        self.epsilon = 0

agent_no_epsilon = AgentNoEpsilon()             
def act(observation, configuration):
    if observation.step > 0:
        # После первого хода учимся
        agent_no_epsilon.fit(observation.lastOpponentAction)
    return agent_no_epsilon.act()
