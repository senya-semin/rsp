#Реализуем стратегию SARSA

#Импортируем класс, от которого наследуемся
from agent import Agent

class AgentSARSA(Agent):
    def __init__(self):
        super().__init__()

    def update_value(self, reward):
        # Обновляем значение классическим для Q-обучения через функцию SARSA
        self.value_table[self.state][self.action] += self.learning_rate \
              * (reward + self.discount_factor \
                 * self.value_table[self.state][self.action] \
                    - self.value_table[self.state][self.action])

agent_sarsa = AgentSARSA()             
def act(observation, configuration):
    if observation.step > 0:
        # После первого хода учимся
        agent_sarsa.fit(observation.lastOpponentAction)
    return agent_sarsa.act()
