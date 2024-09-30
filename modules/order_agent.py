
class Order_agent():
  def __init__(self) -> None:
      '''
      Агент декйствует по порядку камень-ножницы-бумага
      '''
      self.action = 0

  def act(self):
    if self.action == 0:
      self.action = 1
      return 1
    elif self.action == 1:
      self.action = 2
      return 2
    elif self.action == 2:
      self.action = 0
      return 0

agent = Order_agent()

#Example
def order_act(observation, configuration):
    return agent.act()
