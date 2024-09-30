#Реализуем

class AgentLambdaWatkins(Agent):
    def __init__(self):
        super().__init__()
        self.lambd = 0.9
        self.E = {0: 
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
        delta = self.learning_rate \
              * (reward + self.discount_factor \
                 * max(self.value_table[self.state], key=self.value_table[self.state].get) \
                    - self.value_table[self.state][self.action])
        
        self.E[self.state][self.action] += 1

        for s in self.value_table.keys():
            for a in self.value_table[s].keys():
                self.value_table[s][a] += self.learning_rate * delta * self.E[s][a]
                self.E[s][a] *= self.discount_factor * self.lambd

agent_lambda = AgentLambdaWatkins()             
def act_lambda(observation, configuration):
    if observation.step > 0:
        agent_lambda.fit(observation.lastOpponentAction)
    return agent_lambda.act()
