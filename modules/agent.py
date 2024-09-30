
import random
import time
random.seed(37057087388379217268129464)

class Agent:
    def __init__(self):
        # Стратегия: вероятности выбора rock, paper, scissors
        # Инициализация агента с параметрами обучения и начальным состоянием
        self.learning_rate = 0.8 # Скорость обучения агента
        self.discount_factor = 0.2 # Коэффициент дисконтирования для будущих вознаграждений
        self.epsilon = 0.1 # Реализуем жадную стратегию. Вероятность выбора случайного действия (exploration)

         # Начальное состояние и действие агента выбираются случайным образом
        self.state = random.choice([0, 1, 2]) # Состояния: 0 - камень, 1 - бумага, 2 - ножницы
        self.action = random.choice([0, 1, 2]) # Действия: 0 - камень, 1 - бумага, 2 - ножницы
        
         # Таблица значений для состояний и действий (начальные вероятности равны)
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
        # Метод для обновления значений в таблице на основе полученного вознаграждения
        pass

    def __choose_action(self):
        # Метод для выбора действия на основе текущего состояния и стратегии ε-greedy
        
        if self.epsilon < random.random(): 
            # Если не выбираем случайное действие, выбираем действие с максимальным значением    
            max_value = max(self.value_table[self.state].values())  # Находим максимальное значение
            keys_with_max_value = [key for key, value in self.value_table[self.state].items() if value == max_value]
            return random.choice(keys_with_max_value) # Случайный выбор среди действий с максимальным значением
        else:
            return random.choice([0, 1, 2]) # Случайный выбор действия для исследования
        
    def act(self):
        # Метод для выполнения действия агентом
        self.action = self.__choose_action()
        return self.action
    
    def fit(self, state):
        # Метод для обновления состояния агента на основе результата игры
        if (self.action == 0 and state == 2) or \
           (self.action == 2 and state == 1) or \
           (self.action == 1 and state == 0):
            reward = 1  # Победа
        elif self.action == state:
            reward = 0  # Ничья
        else:
            reward = -1  # Поражение

        self.update_value(reward) # Обновление значений на основе вознаграждения
        self.state = state # Обновление текущего состояния агента

