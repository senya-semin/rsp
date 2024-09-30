
import random

class Agent:
    def __init__(self):
        # Стратегия: вероятности выбора rock, paper, scissors
        self.learning_rate = 0.8
        self.discount_factor = 0.2
        self.greedy = True
        self.epsilon = 0.1
        self.state = random.choice([0, 1, 2])
        self.action = random.choice([0, 1, 2])
        self.value_table = {0: 
                                {0: 1/3,
                                 1: 1/3,
                                 2: 1/3},
                            1: 
                                {0: 1/3,
                                 1: 1/3,
                                 2: 1/3},
                            2: 
                                {0: 1/3,
                                 1: 1/3,
                                 2: 1/3}}

    def update_value(self, reward):
        pass

    def __choose_action(self):
        #Выбираем действие
        if self.epsilon < random.random() and self.greedy:      
            max_value = max(self.value_table[self.state].values())  # Находим максимальное значение
            keys_with_max_value = [key for key, value in self.value_table[self.state].items() if value == max_value]
            return random.choice(keys_with_max_value)
        else:
            return random.choice([0, 1, 2])
        
    def act(self):
        self.action = self.__choose_action()
        return self.action
    
    def fit(self, state):
        if (self.action == 0 and state == 2) or \
           (self.action == 2 and state == 1) or \
           (self.action == 1 and state == 0):
            reward = 1  # Победа
        elif self.action == state:
            reward = 0  # Ничья
        else:
            reward = -1  # Поражение

        self.update_value(reward)
        self.state = state

