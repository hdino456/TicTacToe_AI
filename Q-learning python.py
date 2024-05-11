import numpy as np

#defining a set of actions agent can preform
actions = ["up", "down", "left", "right"]

#defining the enwiroment
rewards = np.full((11,11),-100) #matrix size
rewards[0,5]=100 #packaging area 
#defining enviroment for the agend to move
aisles={}
aisles[1] = [i for i in range(1, 10)]
aisles[2] = [1, 7, 9]
aisles[3] = [i for i in range(1, 8)]
aisles[3].append(9)
aisles[4] = [3, 7]
aisles[5] = [i for i in range(11)]
aisles[6] = [5]
aisles[7] = [i for i in range(1, 10)]
aisles[8] = [3, 7]
aisles[9] = [i for i in range(11)]
#embeding pathways in to the matrix
for row_index in range(1,10):
    for column_index in aisles[row_index]:
        rewards[row_index,column_index]=-1
        
#helper functions
#defining terminal state
def is_terminal_state(current_row_index, current_column_index):
    if rewards[current_row_index, current_column_index] == -1:
        return False
    else:
        return True
#chose random non terminal state as a starting point
def get_starting_location():
    current_row_index = np.random.randit(0,11)
    current_column_index = np.random.randit(0,11)
    while is_terminal_state(current_row_index, current_column_index):
        current_row_index = np.random.randit(0,11)
        current_column_index = np.random.randit(0,11)
    return current_row_index, current_column_index


#define epsilon gready alghorythm for next action
def get_next_action(current_row_index, current_column_index, epsilon):
  #if a randomly chosen value between 0 and 1 is less than epsilon, 
  #then choose the most promising value from the Q-table for this state.
  if np.random.random() < epsilon:
    return np.argmax(q_values[current_row_index, current_column_index])
  else: #choose a random action
    return np.random.randint(4)