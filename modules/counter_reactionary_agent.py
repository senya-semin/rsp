#Агент всегда опирающийся на последний ход соперника
import random
random.seed(112324124)

def get_score(agent_action, opponent_action):
    '''
    Функция для расчета счета
    '''
    if (agent_action == 0 and opponent_action == 2) or \
        (agent_action == 2 and opponent_action == 1) or \
        (agent_action == 1 and opponent_action == 0):
        reward = 1  # Победа
    elif agent_action == opponent_action:
        reward = 0  # Ничья
    else:
        reward = -1  # Поражение
    return reward

last_counter_action = None

def counter_reactionary(observation, configuration):
    global last_counter_action
    if observation.step == 0:
        last_counter_action = random.randrange(0, configuration.signs)
    elif get_score(last_counter_action, observation.lastOpponentAction) == 1:
        last_counter_action = (last_counter_action + 2) % configuration.signs
    else:
        last_counter_action = (observation.lastOpponentAction + 1) % configuration.signs

    return last_counter_action
