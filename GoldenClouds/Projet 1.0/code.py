
import pygame                    #on importe les bibliothèques
from pygame.locals import *

pygame.mixer.pre_init(44100, -16, 2, 4096)      #pre_init(frequency=22050, size=-16, channels=2, buffersize=4096)réduire le temps de latence

pygame.init()  #on initialise pygame

WIDTH = 1000   #largeur de la fenêtre
HEIGHT = 500   #hauteur de la fenêtre

#couleurs = (rouge, vert, bleu)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
Fond = (223,210,220)
 
#titre de la fenetre et image
pygame.display.set_caption("GoldenCloud")
icon_32x32 = pygame.image.load("images\\background.jpg")
pygame.display.set_icon(icon_32x32)

#sons des notes
do = pygame.mixer.Sound("sons\\1-do(c1).wav")
reb = pygame.mixer.Sound("sons\\2-do#(c1s).wav")
re = pygame.mixer.Sound("sons\\3-re(d1).wav")
mib = pygame.mixer.Sound("sons\\4-re#(d1s).wav")
mi = pygame.mixer.Sound("sons\\5-mi(e1).wav")
fa = pygame.mixer.Sound("sons\\6-fa(f1).wav")
solb = pygame.mixer.Sound("sons\\7-fa#(f1s).wav")
sol = pygame.mixer.Sound("sons\\8-sol(g1).wav")
lab = pygame.mixer.Sound("sons\\9-sol#(g1s).wav")
la = pygame.mixer.Sound("sons\\10-la(a1).wav")
sib = pygame.mixer.Sound("sons\\11-la#(a1s).wav")
si = pygame.mixer.Sound("sons\\12-si(b1).wav")
do2 = pygame.mixer.Sound("sons\\13-do2(c2).wav")

def main():
   pygame.init()
   screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
   screen.fill(Fond)
   mainloop(screen)

def mainloop(screen):
   running = True
   while running == True:
      for event in pygame.event.get() :
         if event.type == QUIT: 
            pygame.quit()
                
        #pygame.draw.rect(screen, COULEUR, (x, y, longueur, hauteur)
      pygame.draw.rect(screen, WHITE, (50, 50, 70, 200), 0)   #DO
      pygame.draw.rect(screen, WHITE, (125, 50, 70, 200), 0)  #RE
      pygame.draw.rect(screen, WHITE, (200, 50, 70, 200), 0)  #MI
      pygame.draw.rect(screen, WHITE, (275, 50, 70, 200), 0)  #FA
      pygame.draw.rect(screen, WHITE, (350, 50, 70, 200), 0)  #SOL
      pygame.draw.rect(screen, WHITE, (425, 50, 70, 200), 0)  #LA
      pygame.draw.rect(screen, WHITE, (500, 50, 70, 200), 0)  #SI
      pygame.draw.rect(screen, WHITE, (575, 50, 70, 200), 0)  #DO2
      pygame.draw.rect(screen, WHITE, (650, 50, 70, 200), 0)  #RE2
      pygame.draw.rect(screen, WHITE, (725, 50, 70, 200), 0)  #MI2
      pygame.draw.rect(screen, WHITE, (800, 50, 70, 200), 0)  #FA2
      pygame.draw.rect(screen, WHITE, (875, 50, 70, 200), 0)  #SOL2
      pygame.draw.rect(screen, BLACK, (100, 50, 40, 150), 0)  #REb
      pygame.draw.rect(screen, BLACK, (175, 50, 40, 150), 0)  #MIb
      pygame.draw.rect(screen, BLACK, (325, 50, 40, 150), 0)  #SOLb
      pygame.draw.rect(screen, BLACK, (400, 50, 40, 150), 0)  #LAb
      pygame.draw.rect(screen, BLACK, (475, 50, 40, 150), 0)  #SIb
      pygame.draw.rect(screen, BLACK, (625, 50, 40, 150), 0)  #RE2b
      pygame.draw.rect(screen, BLACK, (700, 50, 40, 150), 0)  #MgI2b
      pygame.draw.rect(screen, BLACK, (850, 50, 40, 150), 0)  #SOL2b
      pygame.display.update()

      if event.type == KEYDOWN:
         if event.key == K_q:
            do.play()
            pygame.draw.rect(screen, BLACK, (50, 50, 70, 200), 0)#DO
            pygame.display.flip()
         if event.key == K_s:
            re.play()
            pygame.draw.rect(screen, BLACK, (125, 50, 70, 200), 0)#RE
            pygame.display.flip()
         if event.key == K_d:
            mi.play()
            pygame.draw.rect(screen, BLACK, (200, 50, 70, 200), 0)#MI
            pygame.display.flip()
         if event.key == K_f:
            fa.play()
            pygame.draw.rect(screen, BLACK, (275, 50, 70, 200), 0)#FA
            pygame.display.flip()
         if event.key == K_g:
            sol.play()
            pygame.draw.rect(screen, BLACK, (350, 50, 70, 200), 0)#SOL
            pygame.display.flip()
         if event.key == K_h:
            la.play()
            pygame.draw.rect(screen, BLACK, (425, 50, 70, 200), 0)#LA
            pygame.display.flip()
         if event.key == K_j:
            si.play()
            pygame.draw.rect(screen, BLACK, (500, 50, 70, 200), 0)#SI
            pygame.display.flip()
         if event.key == K_k:
            do2.play()
            pygame.draw.rect(screen, BLACK, (575, 50, 70, 200), 0)#DO2
            pygame.display.flip()
    

main()
