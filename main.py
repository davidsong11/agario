import pygame
from random import randint
import time

# beginning = time.time()

pygame.init()
win = pygame.display.set_mode((600,600))


x = randint(0,600)
y = randint(0,600)
r = 20
s = 5

x2 = randint(0,600)
y2 = randint(0,600)
r2 = 20
s2 = 5


NUMBER_OF_FOODS = 12

foods = []
for _ in range(NUMBER_OF_FOODS):
  newfood = (randint(0,600),randint(0,600))
  foods.append(newfood)

# initialization of the model
##############################################
# inside the while: when the game is in progress.

# while r<420:
while True:
  win.fill((0,0,0))
  pygame.time.delay(20)

  s = 5-r/100

  pygame.event.pump()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP]:
    y -= s
  if keys[pygame.K_DOWN]:
    y += s
  if keys[pygame.K_LEFT]:
    x -= s
  if keys[pygame.K_RIGHT]:
    x += s

  if keys[pygame.K_w]:
    y2 -= s2
  if keys[pygame.K_s]:
    y2 += s2
  if keys[pygame.K_a]:
    x2 -= s2
  if keys[pygame.K_d]:
    x2 += s2

  # draw the player
  pygame.draw.circle(win, (255,0,0), (int(x),int(y)), r)
  

  pygame.draw.circle(win, (255,0,255), (int(x2),int(y2)), r2)

  for food in foods:
    xfood, yfood = food
    pygame.draw.circle(win, (255,255,255), (xfood, yfood), 5)

    # is food within the radius of the character?
    if ((x-xfood)**2 + (y-yfood)**2)**0.5 < r:
      # eat this food
      try:
        foods.remove(food)
      except:
        print('Something went wrong; eating same food')
      r += 5
      newfood = (randint(0,600),randint(0,600))
      foods.append(newfood)
      
    if ((x2-xfood)**2 + (y2-yfood)**2)**0.5 < r2:
      # eat this food
      try:
        foods.remove(food)
      except:
        print('Something went wrong; eating same food')
      r2 += 5
      newfood = (randint(0,600),randint(0,600))
      foods.append(newfood)
    
  if ((x-x2)**2 + (y-y2)**2)**0.5 < r:
    r2 = 0
  if ((x-x2)**2 + (y-y2)**2)**0.5 < r2:
    r = 0
    
  pygame.display.update()

# end_time = time.time()
# print("This game took", end_time-beginning, "seconds")