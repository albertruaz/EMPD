import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, num, initial_money=0):
        self.name = name
        self.money = initial_money
        self.num = num

    @abstractmethod
    def perform_action(self, agent_last_action ,opponent_last_action, round_number,opponent_player,epsilon):
        pass

class Generous(Player):
    def __init__(self, name, num):
        super().__init__(name,num)

    def perform_action(self, agent_last_action ,opponent_last_action, round_number,opponent_player,epsilon=1):
        return "Cooperate"

class Selfish(Player):
    def __init__(self, name, num):
        super().__init__(name, num)

    def perform_action(self, agent_last_action ,opponent_last_action, round_number,opponent_player,epsilon=1):
        return "Betray"


class RandomPlayer(Player):
    def __init__(self, name, num):
        super().__init__(name, num)

    def perform_action(self, agent_last_action ,opponent_last_action, round_number,opponent_player,epsilon=1):
        actions = ["Cooperate", "Betray"]
        return random.choice(actions)
    

class CopyCat(Player):
    def __init__(self, name, num):
        super().__init__(name, num)

    def perform_action(self, agent_last_action ,opponent_last_action, round_number,opponent_player,epsilon=1):
        if round_number==1:
            return "Cooperate"
        else:
            return opponent_last_action


class Grudger(Player):
    def __init__(self, name, num):
        super().__init__(name, num)
        self.actions=[]
    
    def perform_action(self, agent_last_action ,opponent_last_action, round_number,opponent_player,epsilon=1):
        if round_number==1:
            self.actions=[]
            return "Cooperate"
        if round_number==2:
            self.actions.append(opponent_last_action)
            if "Betray" in self.actions:
                return "Betray"
            else:
                return "Cooperate"
        self.actions.append(opponent_last_action)

        if "Betray" in self.actions:
            return "Betray"
        else:
            return "Cooperate"
            
    

class Detective(Player):
    def __init__(self, name, num):
        super().__init__(name, num)
        self.actions = []

    def perform_action(self, agent_last_action ,opponent_last_action, round_number,opponent_player,epsilon=1):
        
        if round_number==1:
            self.actions=[]
            return "Cooperate"
        elif round_number==2:
            return "Betray"
        elif round_number==3:
            return "Cooperate"
        elif round_number==4:
            self.actions.append(opponent_last_action)
            return "Cooperate"
        elif round_number>4:
            self.actions.append(opponent_last_action)
            if "Betray" in self.actions[:-1]:
                return opponent_last_action
            else:
                return "Betray"
            

class Simpleton(Player):
    def __init__(self, name, num):
        super().__init__(name, num)
        self.actions = []

    def perform_action(self, agent_last_action ,opponent_last_action, round_number,opponent_player,epsilon=1):
        if round_number==1:
            self.actions.append("Cooperate")
            return "Cooperate"
        elif round_number >1:
            if opponent_last_action == "Cooperate":
                self.actions.append(self.actions[-1])
                return self.actions[-1]
            elif opponent_last_action == "Betray":   
                if self.actions[-1] == "Cooperate":
                    self.actions.append("Betray")
                    return "Betray"
                elif self.actions[-1] == "Betray":
                    self.actions.append("Cooperate")
                    return "Cooperate"

        
          
class Copykitten(Player):
    def __init__(self, name, num):
        super().__init__(name, num)
        self.actions = []

    def perform_action(self, agent_last_action ,opponent_last_action, round_number,opponent_player,epsilon=1):
        if round_number==1:
            return "Cooperate"
        elif round_number==2:
            self.actions.append(opponent_last_action)
            return "Cooperate"
        elif round_number > 2:
            self.actions.append(opponent_last_action)
            if self.actions[-2:] == ["Betray", "Betray"]:
                return "Betray"
            else:
                return "Cooperate"