import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
#x1 = int (input("Enter an x1 coordinate: "))
#y1 = int (input("Enter an y1 coordinate: "))
x1,y1= 1,1
goal=120,50
#if x1 not in range(0,200) or y1 not in range(0,100):
    #print("Position not permitted")
    #exit()
#if x1 in range(90,110) or y1 in range(40,60):
    #print("Position not permitted")
    #exit()
    
height, width = 200, 300
img = np.zeros((height, width), np.uint8)
k=0
def obstacle:
	k=0
	for x in range(width):
		for y in range(height):
			if (((x>=225 and x<=250) and (y>=((3/5)*(x-225)+160))) or ((x>=200 and x<=225) and (y>=((-3/5)*(x-225)+160)))):
				img[y,x]=1
				k=1
			if ((x>=200 and x<=225) and (y>=((3/5)*(x-200)+175))) or ((x>=225 and x<=250) and (y>=((-3/5)*(x-225)+190))):
				img[y,x]=0
				k=1
			if (x-225)**2+(y-50)**2<=625:
				img[y,x]=1
				k=1
			if (x-150)**2/(40)**2+(y-100)**2/(20)**2<=1:
				img[y,x]=1
				k=1
			if (((x>=30.875 and x<=35.875) and (y>=((-1.71)*(x-35.875)+135.5))) or ((x>=35.875 and x<=100) and (y>=((0.53)*(x-100)+161.45)))):
				img[y,x]=1
				k=1
			if ((x>=30.875 and x<=95) and (y>=((0.5380)*(x-30.675)+135.5))) or ((x>=95 and x<=100) and (y>=((-1.71)*(x-95)+170))):
				img[y,x]=0
				k=1
			if ((x>=25 and x<=75) and (80>=y>=15)) or ((x>=75 and x<=100) and (80>=y>=((7/5)*(x-75)+15))) or ( (x<=20 or x<=25) and (80>=y>=((-13)*(x-20)+80))):
				img[y,x]=1
				k=1
			if ((x>=20 and x<=50) and (80>= y>=(-1)*(x-20)+80)) or ((x>=50 and x<=75) and (80>=y>=((6/5)*(x-75)+80))) or((x>=75 and x<=100) and (80>=y>=((-6/5)*(x-100)+50))): 
				img[y,x]=0
				k=1
	return k

obstacle_=[]
for i in range(0,300):
    for j in range(0,200):
        c=obstacle(i,j)
        if c==1:
            obstacle_.append([i,j])
def start(initial):
    c=obstacle(initial[0],initial[1])
    if c ==1 or initial[0]  not in range(0,251) or (initial[1] not in range(0,151)):
        print("Entry not Valid")
        exit()
    else:
        pass

def end(goal):
    c=obstacle(goal[0],goal[1])
    if c ==1 or goal[0] not in range(0,251) or goal[1] not in range(0,151):
        print("Goal point inside obstacle space or not in workspace space or not a good entry for resolution")
        exit()
    else:
        pass

			










k=2
pygame.init()
Black = [0, 0, 0]
White = [255, 255, 255]
blue=[0,255,255]
green = [0,255,0]
Size = [200,300]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Dijkstra Point Robot") 
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            done = True 
    screen.fill(BLACK)
    for i in obstacle_:
        pygame.draw.rect(screen, WHITE, [i[0],150*k-i[1],k,k])
    pygame.display.flip()
    clock.tick(20)
    for i in visited:
        pygame.time.wait(1)
        pygame.draw.rect(screen, green, [i[0],150*k-i[1],k,k])
        pygame.display.flip()
    for j in new_goal[::-1]:
        pygame.time.wait(1)
        pygame.draw.rect(screen, blue, [j[0], 150*k-j[1], k,k])
        pygame.display.flip()
    
    pygame.display.flip()

    pygame.time.wait(15000)
    done = True