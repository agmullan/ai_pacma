# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""
import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).

  You do not need to change anything in this class, ever.
  """

def getStartState(self):
  """
  Returns the start state for the search problem
  """
  util.raiseNotDefined()

def isGoalState(self, state):
  """
  state: Search state

  Returns True if and only if the state is a valid goal state
  """
  util.raiseNotDefined()

def getSuccessors(self, state):
  """
  state: Search state

  For a given state, this should return a list of triples,
  (successor, action, stepCost), where 'successor' is a
  successor to the current state, 'action' is the action
  required to get there, and 'stepCost' is the incremental
  cost of expanding to that successor
  """
  util.raiseNotDefined()

def getCostOfActions(self, actions):
  """
  actions: A list of actions to take

  This method returns the total cost of a particular sequence of actions.  The sequence must
  be composed of legal moves
  """
  util.raiseNotDefined()


def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 74].

  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.18].

  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:

  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  from util import Stack
  from searchAgents import node

  #initialize frontier
  frontier = Stack()
  initialState = problem.getStartState()
  currentNode = node(initialState, None ,0,0,0) #create the root node and add it to the frontier
  frontier.push(currentNode)

  #initialize the explored set
  explored = dict()

  #run the solution search
  while True:

    #no solution
    if(frontier.isEmpty()):
      return []

    current = frontier.pop() #keep track of the current node

    #solution found
    if (problem.isGoalState(current.getCurrentState())):
      solution = list()
      step = current

      while(step.getParentNode() != None):
          solution.append(step.getLastAction())
          step = step.getParentNode()

      solution.reverse()

      return solution #return list of actions from start state to goal state

    #add current node to the explored set
    explored[current.getCurrentState()] = "True"

    #expand the current node
    for successor in problem.getSuccessors(current.getCurrentState()):
      s = node(successor[0], current, successor[1], successor[2], 1)

      if(s.getCurrentState() in explored):
        print("") #do nothing
      else:
        frontier.push(s)

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 74]"
  "*** YOUR CODE HERE ***"
  from util import Queue
  from searchAgents import node

  # initialize the frontier using the initial state of the problem
  frontier = Queue()
  initialState = problem.getStartState()
  root_node = node(initialState, None ,0,0,0)
  frontier.push(root_node)

  # initialize explored to empty
  explored = dict()

  # path of solution
  path = list()
  while True:
    #No solution found return empty set
    if frontier.isEmpty():
      return []

    #Dequeue first node in frontier
    cur_node = frontier.pop()

    #Solution found
    if problem.isGoalState(cur_node.getCurrentState()):
      node = cur_node

      while(node.getParentNode() != None):
        path.append(node.getLastAction())
        node = node.getParentNode()

      path.reverse()
      return path

    #put cur_node in explored
    explored[cur_node.getCurrentState()] = "True"

    # for every child of cur_node Enqueue to frontier
    for successor in problem.getSuccessors(cur_node.getCurrentState()):
      child = node(successor[0], cur_node, successor[1], successor[2], 1)
      # if the child has not been visited
      if(child.getCurrentState() not in explored):
        # add children to frontier
        frontier.push(child)

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  from util import PriorityQueue
  from searchAgents import node
  # initialize the frontier using the initial state of the problem
  frontier = PriorityQueue()
  initialState = problem.getStartState()
  root_node = node(initialState, None ,0,0,0)
  frontier.push(root_node, root_node.getTotalPathCost())

  # initialize explored to empty
  explored = dict()

  # path of solution
  path = list()
  while True:
      #No solution found return empty set
      if frontier.isEmpty():
          return []

      #Dequeue first node in frontier
      cur_node = frontier.pop()

      #Solution found
      if problem.isGoalState(cur_node.getCurrentState()):
          node = cur_node

          while(node.getParentNode() != None):
              path.append(node.getLastAction())
              node = node.getParentNode()
          # path.append(cur_node.getLastAction())
          path.reverse()
          return path

      #put cur_node in explored
      explored[cur_node.getCurrentState()] = "True"

      # for every child of cur_node Enqueue to frontier
      for successor in problem.getSuccessors(cur_node.getCurrentState()):
          #calculate step cost and total path cost
          stepCost = successor[2]
          totalPathCost = cur_node.getTotalPathCost() + stepCost
          child = node(successor[0], cur_node, successor[1], stepCost, totalPathCost)
          # if the child has not been visited
          if(child.getCurrentState() not in explored):
              frontier.push(child, child.getTotalPathCost())
  #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):

    "Search the node that has the lowest combined cost and heuristic first."

    from util import PriorityQueue
    from searchAgents import node

    #initialize frontier
    frontier = PriorityQueue()
    initialState = problem.getStartState()
    currentNode = node(initialState, None, 0, 0, 0) #create the root node and add it to the frontier

    frontier.push(currentNode, currentNode.getTotalPathCost())

    #initialize the explored set
    explored = dict()

    while True:
        #no solution
        if(frontier.isEmpty()):
            return []

        #choose the lowest cost (path + heuristic) node in the frontier
        current = frontier.pop()

        #solution found
        if (problem.isGoalState(current.getCurrentState())):
            solution = list()
            step = current

            #collect the path
            while(step.getParentNode() != None):
                solution.append(step.getLastAction())
                step = step.getParentNode()

            solution.reverse()

            return solution #return list of actions from start state to goal state

        #add node to explored
        explored[current.getCurrentState()] = "True"

        for successor in problem.getSuccessors(current.getCurrentState()):

            #calculate step cost and total path cost
            myStepCost = successor[2]
            myTotalPathCost = current.getTotalPathCost() + myStepCost
            child = node(successor[0], current, successor[1], myStepCost, myTotalPathCost)

            #add the current node's child to the frontier
            if(child.getCurrentState() not in explored):
                frontier.push(child, child.getTotalPathCost() + heuristic(child.getCurrentState(), problem))

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
