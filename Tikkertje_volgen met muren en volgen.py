import pygame
import sys
import random

pygame.init() #pygame opstarten

Scherm_breedte=590
Scherm_lengte=470
scherm = pygame.display.set_mode((Scherm_breedte, Scherm_lengte))
boundary = pygame.Rect(0, 0, Scherm_breedte, Scherm_lengte-33)  # Maakt een vlak even groot als het speelveld
lettertype1=pygame.font.SysFont("arial",36)
lettertype2=pygame.font.SysFont("arial",20)

pygame.display.set_caption("Tikkertje") #naam van systeem

#Kleuren bepaald met rbg (rood, groen, blauw) met schaal van 0-255
ZWART = (0,0,0)
GROEN = (0, 255, 0)
ROOD = (255,0,0)
BLAUW = (0, 0, 255)
WIT =  (255,255,255)
ACHTERGROND_KLEUR = (50, 150, 255)

klok = pygame.time.Clock() #snelheid van spel (fps)

renner=pygame.Rect(random.randint(10, 560),random.randint(10, 430),20,20)
jager=pygame.Rect(random.randint(10, 560),random.randint(10, 430),20,20)
#muur=pygame.Rect(150, 350, 300, 20)
score=0
snelheid_r=3
snelheid_j=2
#juur=pygame.Rect(150, 50, 10, 70)
ruur=0

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Als je op het kruisje klikt
            running=False

    renner_x_oud = renner.x
    renner_y_oud = renner.y
    d=jager.x-renner.x
    if d==0: d=0.0001
    e=jager.y-renner.y
    if e==0: e=0.0001
    f=abs(d/e)
    #if f>1 and d>0:
    #    renner.x+=snelheid_r
    #elif f>1 and d<0:
    #    renner.x-=snelheid_r
    #elif f<1 and e>0:
    #    renner.y+=snelheid_r
    #elif f<1 and e<0:
    #    renner.y-=snelheid_r
    #elif f==1 and e<0:
    #    renner.y-=snelheid_r
    #elif f==1 and e>0:
    #    renner.y+=snelheid_r

    a=renner.x-jager.x
    if a==0: a=0.0001
    b=renner.y-jager.y
    if b==0: b=0.0001
    c=abs(a/b)
    g=a/b

    if g>1:
        if renner.y>jager.y:
            renner.y-=snelheid_r
        else:
            renner.y+=snelheid_r
    if 1>g>0:
        if renner.y>jager.y:
            renner.x-=snelheid_r
        else:
            renner.x+=snelheid_r
    if 0>g>(-1):
        if renner.y>jager.y:
            renner.x+=snelheid_r
        else:
            renner.x-=snelheid_r
    if (-1)>g:
        if renner.y>jager.y:
            renner.y+=snelheid_r
        else:
            renner.y-=snelheid_r


    #renner_x_oud = renner.x
    #renner_y_oud = renner.y
    #keys=pygame.key.get_pressed()
    #if keys[pygame.K_LEFT] and renner.x!=0:
    #    renner.x-=snelheid_r
    #elif keys[pygame.K_RIGHT] and renner.x!=Scherm_breedte-20:
    #    renner.x+=snelheid_r
    #elif keys[pygame.K_UP] and renner.y!=0:
    #    renner.y-=snelheid_r
    #elif keys[pygame.K_DOWN] and renner.y!=Scherm_lengte-50:
    #    renner.y+=snelheid_r
    #if renner.colliderect(muur):
    #    renner.y = renner_y_oud
    #if renner.colliderect(muur):
    #    renner.x = renner_x_oud

    #if renner.colliderect(muur):
    #    if renner.y!=renner_y_oud and renner.x+jager.x-2*muur.x<2*(muur.x+muur.width)-renner.x-jager.x:
    #        renner.x-=snelheid_r
    #        renner.y=renner_y_oud
    #    elif renner.y!=renner_y_oud and renner.x+jager.x-muur.x*2>2*(muur.x+muur.width)-renner.x-jager.x:
    #        renner.x+=snelheid_r
    #        renner.y=renner_y_oud
    #    elif renner.y!=renner_y_oud and renner.x+jager.x-muur.x*2==2*(muur.x+muur.width)-renner.x-jager.x:
    #        renner.x+=snelheid_r
    #        renner.y=renner_y_oud
    #        
    #    elif renner.x!=renner_x_oud and renner.y+jager.y-2*muur.y<2*(muur.y+muur.height)-renner.y-jager.y:
    #        renner.y-=snelheid_r
    #        renner.x=renner_x_oud
    #    elif renner.x!=renner_x_oud and renner.y+jager.y-2*muur.y>2*(muur.y+muur.height)-renner.y-jager.y:
    #        renner.y+=snelheid_r
    #        renner.x=renner_x_oud
    #    elif renner.x!=renner_x_oud and renner.y+jager.y-2*muur.y==2*(muur.y+muur.height)-renner.y-jager.y:
    #        renner.y+=snelheid_r
    #        renner.x=renner_x_oud

    jager_x_oud = jager.x
    jager_y_oud = jager.y

    if c>1 and a>0:
        jager.x+=snelheid_j
    elif c>1 and a<0:
        jager.x-=snelheid_j
    elif c<1 and b>0:
        jager.y+=snelheid_j
    elif c<1 and b<0:
        jager.y-=snelheid_j
    elif c==1 and b<0:
        jager.y-=snelheid_j
    elif c==1 and b>0:
        jager.y+=snelheid_j
    
    #if jager.colliderect(muur):
    #    if jager.y!=jager_y_oud and jager.x+renner.x-2*muur.x<2*(muur.x+muur.width)-jager.x-renner.x:
    #        jager.x-=snelheid_j
    #        jager.y=jager_y_oud
    #    elif jager.y!=jager_y_oud and jager.x+renner.x-muur.x*2>2*(muur.x+muur.width)-jager.x-renner.x:
    #        jager.x+=snelheid_j
    #        jager.y=jager_y_oud
    #    elif jager.y!=jager_y_oud and jager.x+renner.x-muur.x*2==2*(muur.x+muur.width)-jager.x-renner.x:
    #        jager.x+=snelheid_j
    #        jager.y=jager_y_oud
    #        
    #    elif jager.x!=jager_x_oud and jager.y+renner.y-2*muur.y<2*(muur.y+muur.height)-jager.y-renner.y:
    #        jager.y-=snelheid_j
    #        jager.x=jager_x_oud
    #    elif jager.x!=jager_x_oud and jager.y+renner.y-2*muur.y>2*(muur.y+muur.height)-jager.y-renner.y:
    #        jager.y+=snelheid_j
    #        jager.x=jager_x_oud
    #    elif jager.x!=jager_x_oud and jager.y+renner.y-2*muur.y==2*(muur.y+muur.height)-jager.y-renner.y:
    #        jager.y+=snelheid_j
    #        jager.x=jager_x_oud

    score+=1/60
    scherm.fill(ACHTERGROND_KLEUR)
    pygame.draw.rect(scherm, ZWART, (0,Scherm_lengte-30,Scherm_breedte,30))
    pygame.draw.rect(scherm, GROEN, renner)
    pygame.draw.rect(scherm, ROOD, jager)
    #pygame.draw.rect(scherm, BLAUW, muur)
    scherm.blit(lettertype2.render(str(round(score,2)),True,WIT),(10,Scherm_lengte-30))
    pygame.display.flip() #Laat scherm nieuwst aanpassingen zien
    
    renner.clamp_ip(boundary)   # Houdt renner binnen het vlak

    if jager.colliderect(renner):
        scherm.fill(ACHTERGROND_KLEUR)
        scherm.blit(lettertype1.render("Jager wint",True,ZWART),(130,100))
        scherm.blit(lettertype1.render(str(round(score,2)),True,ZWART),(130,200))
        pygame.display.flip()
        klok.tick(2)
        running=False
    
    klok.tick(60) #spel draait op 60 fps

    


pygame.quit()
sys.exit()
