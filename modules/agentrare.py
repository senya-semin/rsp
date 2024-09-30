#Стратегия выбора либо успешного хода, либо самого редкого

import random
random.seed(21498397587320590390394382)

class AgentRare():
    def __init__(self) -> None:
        self.action = random.choice([0, 1, 2]) # Случайный выбор начального действия (0, 1 или 2)
        self.action_history = {0: 0,
                                1: 0,
                                2: 0}
        
    def act(self, state):
        # Метод для выполнения действия на основе текущего состояния
        self.action_history[self.action] += 1 # Увеличиваем счетчик для текущего действия

        # Определение вознаграждения на основе текущего действия и состояния
        if (self.action == 0 and state == 2) or \
           (self.action == 2 and state == 1) or \
           (self.action == 1 and state == 0):
            reward = 1  # Победа
        elif self.action == state:
            reward = 0  # Ничья
        else:
            reward = -1  # Поражение

        # Если агент выиграл, возвращаем текущее действие
        if reward == 1:
            return self.action
        
        else:
            # Находим минимальное количество выполнений среди всех действий
            min_value = min(self.action_history.values())  # Находим максимальное значение
            # Находим все действия с минимальным количеством выполнений
            keys_with_max_value = [key for key, value in self.action_history.items() if value == min_value]
            # Случайным образом выбираем одно из действий с минимальным количеством выполнений
            self.action = random.choice(keys_with_max_value)
            return self.action

agent_rare = AgentRare()             
def act_rare(observation, configuration):
    if observation.step > 0:
        return agent_rare.act(observation.lastOpponentAction)
    return agent_rare.action
