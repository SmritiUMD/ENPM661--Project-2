import math
import numpy as np
from queue import PriorityQueue
import cv2
import time

grid_x = 200 #defining the grid width and height
grid_y = 300
img = np.zeros((grid_x, grid_y), np.uint8)
d = 0
start_time = time.time() #taking the run time start
start_pos = [5, 195]  #defining the start position as per the requirements
goal = [195,5] #defining the goal position as poer the requirements
solvable = True

for x in range(grid_y): 
    for y in range(grid_x): #writing conditions to define obstacle space in the obstacle area
        if (y>=(3/5)*x+25-d) and (y>=(-3/5)*x+295-d):
            img[y][x]=1
        if (y>=(3/5)*x+55+d) or (y>=(-3/5)*x+325+d):
            img[y][x]=0
        if (x-225)**2+(y-50)**2<=(25+d)**2:
            img[y][x]=1
        if (x-150)**2/(40+d)**2+(y-100)**2/(20+d)**2<=1:
            img[y][x]=1
        if (((x>=30.875 and x<=35.875) and (y>=((-1.71)*x+196.84-d))) or ((x>=35.875 and x<=100) and (y>=((0.53)*x+108.45-d)))):
            img[y][x]=1
        if ((x>=30.875 and x<=95) and (y>=((0.5380)*x+118.99+d))) or ((x>=95 and x<=100) and (y>=((-1.71)*x+332.45+d))):
            img[y][x]=0
        if (y>=(-7/5)*x+120 and y>=(7/5)*x-(90+d)) and (y<=(6/5)*x-10+d and y<=(-6/5)*x+170+d) :
            img[y][x]=1
        if (y<=(-7/5)*x+120) and y<=(7/5)*x-20 and y>=15-d:
            img[y][x]=1
        if y>=(7/5)*x-20 and y>=(-13)*x+340+d and y<=(-1)*x+100+d:
            img[y][x]=1
        if (y>=0 and y<=0+d):
            img[y][x]=1
        if (y<=200 and y>=(200-d)):
            img[y][x]=1
        if (x>=0 and x<=d):
            img[y][x]=1
        if (x<=300 and x>=(300-d)):
            img[y][x]=1
 #wriitng the condition for the case when start or goal node are defined in an obstacle
if img[start_pos[0],start_pos[1]]==1 or img[goal[0],goal[1]]==1:
    print("starting_node/goal_node is inside the obstacle. Please give valid nodes.")
    solvable  =False
else:
    pass



class Node:
    def __init__(self, pos, cost, parent): #creating objects for position, cost and parent information
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.cost = cost
        self.parent = parent


def explore(node): #defining the function for exploring using dijkstra
    i = node.x
    j = node.y

    paths = [(i, j + 1), (i + 1, j), (i - 1, j), (i, j - 1), (i + 1, j + 1), (i - 1, j - 1), (i - 1, j + 1),
             (i + 1, j - 1)]  #creating a list with all the 8 directions 
    valid_paths = []
    for pos, path in enumerate(paths):
        ### Checking if the value for that position is 1 and if it is 0, else we don't consider it a valid point
        if not (path[0] >= grid_y or path[0] < 0 or path[1] >= grid_x or path[1] < 0):  ##writing the condition for the path that may be out of bounds
            

            if img[path[1]][path[0]] == 0:  #checking for the obstacle space
                # print ('in 2nd if exp')
                cost = math.sqrt(2) if pos > 3 else 1
                valid_paths.append([path, cost])
    return valid_paths #returning all the valid paths that pass the conditions


q = PriorityQueue() #defining a priority queue
map = np.zeros([grid_y, grid_x])
visited = set([]) #creating visited nodes
node_objects = {}

####
distance = {}
for i in range(0, grid_y):
    for j in range(0, grid_x):
        distance[str([i, j])] = 99999999 #making the value of all the unvisited nodes as infinity
#####
distance[str(start_pos)] = 0 
visited.add(str(start_pos))
node = Node(start_pos, 0, None)
node_objects[str(node.pos)] = node
q.put([node.cost, node.pos])  # adding the cost values in a priority queue
reached = False

img_show = np.dstack([img.copy()*255, img.copy()*255, img.copy()*255]) # creating an image show function
#start.time.time()
if solvable:  #logic for Dijkstra to check if the nodes traversed is a goal else continue
	while not q.empty():
	    node_temp = q.get()
	    node = node_objects[str(node_temp[1])]
	    if node_temp[1][0] == goal[0] and node_temp[1][1] == goal[1]:
	        print("Reached")
	        node_objects[str(goal)] = Node(goal, node_temp[0], node)
	        reached = True
	        break

	    for next_node, cost in explore(node):

	        if str(next_node) in visited: #defining all the visited nodes and adding the cost values 
	            cost_temp = cost + distance[str(node.pos)]
	            if cost_temp < distance[str(next_node)]:
	                distance[str(next_node)] = cost_temp
	                node_objects[str(next_node)].parent = node
	        else:
	            visited.add(str(next_node)) #adding the next node value to the visited node
	            img_show[next_node[1], next_node[0], :] = np.array([0,0,255])
	            absolute_cost = cost + distance[str(node.pos)]
	            distance[str(next_node)] = absolute_cost
	            new_node = Node(next_node, absolute_cost, node_objects[str(node.pos)])
	            node_objects[str(next_node)] = new_node
	            q.put([absolute_cost, new_node.pos])  #using the queue to add get the least cost 
	            # print(visited)

	print("--- %s seconds ---" % (time.time() - start_time)) #printing the total time taken to run the logic
	          
	#cv2.imshow('img', img_show)
	#cv2.waitKey(10)
	goal_node = node_objects[str(goal)]
	parent_node = goal_node.parent  #adding the previous node traveled from the goal using backtracking to the parent node
	while parent_node:
	    print(parent_node.pos, parent_node.cost)
	    img_show[parent_node.pos[1], parent_node.pos[0],:] = np.array([255,0,0]) #using cv2.imshow to print the final path using backtracking
	    parent_node = parent_node.parent
	cv2.imshow('img', img_show)
	cv2.waitKey(0)
