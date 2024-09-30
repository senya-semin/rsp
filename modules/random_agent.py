#Агент, выбирающий свое решение случайным образом
import random
random.seed(112324124)

#агент принимает решение случайным образом
def random_act(observation, configuration):
    return random.choice([0,1,2])
