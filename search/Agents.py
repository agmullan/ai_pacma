from game import Agent
from game import Directions
from game import Configuration
import random;

class DumbAgent(Agent):
    "An agent that goes West until it can't."
    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        print("Location:", state.getPacmanPosition())
        print("Action available:", state.getLegalPacmanActions())
        if Directions.WEST in state.getLegalPacmanActions():
            print("Going West.")
            return Directions.WEST
        else:
            print("Stopping.")
            return Directions.STOP
#"The agent always goes West. "
#return Directions.WEST

class RandomAgent(Agent):
    "An agent that choices a random direction with each step"
    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        print("Location:", state.getPacmanPosition())
        print("Action available:", state.getLegalPacmanActions())

        if len(state.getLegalPacmanActions()) > 0:
            print("list full")
            secure_random = random.SystemRandom()
            randomDirection = secure_random.choice(state.getLegalPacmanActions())
            print(randomDirection)
            return randomDirection
        else:
            print("list empty")
        return Directions.STOP

class BetterRandomAgent(Agent):
    "An agent that chooses a random direction with each step excluding stop."
    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        print("Location:", state.getPacmanPosition())
        print("Action available:", state.getLegalPacmanActions())

        if len(state.getLegalPacmanActions()) > 0:
            print("list full")
            modifiedList = [];
            for x in state.getLegalPacmanActions():
                if(x != Directions.STOP):
                    modifiedList.append(x)
            print(modifiedList)
            secure_random = random.SystemRandom()
            randomDirection = secure_random.choice(modifiedList)
            print(randomDirection)
            return randomDirection
        else:
            print("list empty")
            return Directions.STOP

class ReflexAgent(Agent):
    "An agent that chooses whichever move will get it to an ajacent piece of food."
    "If there are no adjacent food pellets, it will choose a random direction."
    
    def getAction(self, state):

        if len(state.getLegalPacmanActions()) > 0:
            
            for x in state.getLegalPacmanActions():

                newX = state.getPacmanPosition()[0]
                newY = state.getPacmanPosition()[1]

                if(x == Directions.NORTH):
                    newY += 1; 
                elif(x == Directions.SOUTH):
                    newY -= 1;
                elif(x == Directions.WEST):
                    newX -= 1;
                elif(x == Directions.EAST):
                    newX += 1;
                else:
                    continue

                if(state.hasFood(newX,newY)):
                    return x
                else:
                    continue
        
            modifiedList = [];
            for x in state.getLegalPacmanActions():
                if(x != Directions.STOP):
                    modifiedList.append(x)

            secure_random = random.SystemRandom()
            randomDirection = secure_random.choice(modifiedList)

            return randomDirection

        else:
            return Directions.STOP




