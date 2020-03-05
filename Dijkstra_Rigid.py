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
r=10
c=10
d=25

def obstacle(x,y):
	for x in range(width):
		for y in range(height):
			if (y>=(3/5)*x+25-d) and  (y>=(-3/5)*x+295-d):
				img[y,x]=1
			if (y>=(3/5)*x+55+d) or (y>=(-3/5)*x+325+d):
				img[y,x]=0
			if (x-225)**2+(y-50)**2<=(25+d)**2:
				img[y,x]=1
			if (x-150)**2/(40+d)**2+(y-100)**2/(20+d)**2<=1:
				img[y,x]=1
			if (((x>=30.875 and x<=35.875) and (y>=((-1.71)*x+196.84-d))) or ((x>=35.875 and x<=100) and (y>=((0.53)*x+108.45-d)))):
				img[y,x]=1
			if ((x>=30.875 and x<=95) and (y>=((0.5380)*x+118.99+d))) or ((x>=95 and x<=100) and (y>=((-1.71)*x+332.45+d))):
				img[y,x]=0
			if (y>=(-7/5)*x+120 and y>=(7/5)*x-(90+d)) and (y<=(6/5)*x-10+d and y<=(-6/5)*x+170+d) :
				img[y,x]=1
			if (y<=(-7/5)*x+120) and y<=(7/5)*x-20 and y>=15-d:
				img[y,x]=1
			if y>=(7/5)*x-20 and y>=(-13)*x+340+d and y<=(-1)*x+100+d:
				img[y,x]=1
	        
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
			
plt.imshow(img, cmap="gray")
plt.show()  






























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