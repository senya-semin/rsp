#Реализуем стратегию Q-обучения

#Импортируем класс, от которого наследуемся
from agent import Agent
class AgentQ(Agent):
    def __init__(self):
        super().__init__()

    def update_value(self, reward):
        # Обновляем значение классическим для Q-обучения через функцию Беллмана
        self.value_table[self.state][self.action] += self.learning_rate \
              * (reward + self.discount_factor \
                 * max(self.value_table[self.state], key=self.value_table[self.state].get) \
                    - self.value_table[self.state][self.action])

agentq = AgentQ()             
def act(observation, configuration):
    if observation.step > 0:
        # После первого хода учимся
        agentq.fit(observation.lastOpponentAction)
    return agentq.act()
