import pygame
import sys
import random

pygame.init()

Surf_Width=800
Surf_Height=600

#colors
green=(0, 255, 0)
red=(225,0,0)
black=(0,0,0)
blue=0,0,255
white=(255,255,255)
bg_color=black

#player block
p_size=50
playery=Surf_Height-p_size
playerx=Surf_Width*1/2 - p_size
score=0

#enemy block
e_size=50
enemy_y=0
enemy_x=random.randint(0,Surf_Width-p_size)
enemy_list=[[enemy_x,enemy_y]]
SPEED=5

Surface=pygame.display.set_mode((Surf_Width,Surf_Height))
pygame.display.set_caption("NIGGBLO")
clock=pygame.time.Clock()
fps=30
myfont=pygame.font.SysFont("monospace",30)

def drop_enemies(enemy_list):
    enemy_y = 0
    enemy_x = random.randint(0, Surf_Width - p_size)
    delay=random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        enemy_list.append([enemy_x,enemy_y])

def draw_enemies(enemy_list):
    for enemy in enemy_list:
        pygame.draw.rect(Surface, green, [enemy[0], enemy[1], e_size, e_size])

def update_enemies(enemy_list,score,SPEED):
    for enemy in enemy_list:
        if enemy[1] >= 0 and enemy[1] <= Surf_Height:
            enemy[1]+=SPEED
        else:
            enemy_list.remove(enemy)
            score+=1
    return score

def difficulty(score,speed):
    if score > 20:
        speed=10
    if score > 40:
        speed=15
    if score > 60:
        speed=20
    if score > 80:
        speed=30
    if score > 100:
        speed=40
    return speed

def detct_collision(enemy_list):
    for enemy in enemy_list:
        if enemy[0] >= playerx and enemy[0] < playerx+p_size or enemy[0]+e_size >= playerx and enemy[0]+e_size< playerx+p_size:
            if enemy[1]+e_size > playery:
                return True

gameover = False
while not gameover:
    clock.tick(fps)
    Surface.fill(bg_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerx+=p_size
            elif event.key == pygame.K_LEFT:
                playerx-=p_size

    if detct_collision(enemy_list):
        pygame.quit()
        sys.exit()

    if playerx >= Surf_Width-p_size:
        playerx=Surf_Width-p_size
    elif playerx <=0:
        playerx=0

    drop_enemies(enemy_list)
    draw_enemies(enemy_list)
    SPEED=difficulty(score, SPEED)
    score=update_enemies(enemy_list,score,SPEED)
    text="Score: "+str(score)
    ft=myfont.render(text,True,(blue))
    Surface.blit(ft,(0,0))


    pygame.draw.rect(Surface,red,[playerx,playery,p_size,p_size])
    pygame.display.update()