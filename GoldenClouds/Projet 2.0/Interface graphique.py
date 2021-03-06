
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
do = pygame.mixer.Sound("sons\\1DO_-_A.wav")
reb = pygame.mixer.Sound("sons\\2Reb_-_é.wav")
re = pygame.mixer.Sound("sons\\3R_-_Z.wav")
mib = pygame.mixer.Sound("sons\\4Mib_-__.wav")
mi = pygame.mixer.Sound("sons\\5Mi_-_E.wav")
fa = pygame.mixer.Sound("sons\\6Fa_-_R.wav")
solb = pygame.mixer.Sound("sons\\7solb-_).wav")
sol = pygame.mixer.Sound("sons\\8Sol_-_T.wav")
lab = pygame.mixer.Sound("sons\\9Lab_-_G_ou_§T.wav")
la = pygame.mixer.Sound("sons\\10La-_Y.wav")
sib = pygame.mixer.Sound("sons\\11Sib_-_è.wav")
si = pygame.mixer.Sound("sons\\12Si_-_U.wav")
do2 = pygame.mixer.Sound("sons\\13Do2_-_I.wav")
re2 = pygame.mixer.Sound("sons\\14Re2-_O.wav")
re2b = pygame.mixer.Sound("sons\\15Ré2b_-_ç.wav")
mi2 = pygame.mixer.Sound("sons\\16Mi2_-_P.wav")
mi2b = pygame.mixer.Sound("sons\\17Mi2b_-_à.wav")
fa2 = pygame.mixer.Sound("sons\\18Fa2_-_¨.wav")
sol2 = pygame.mixer.Sound("sons\\19Sol2-$.wav")
sol2b = pygame.mixer.Sound("sons\\20Sol2b-=ou-.wav")

def main():
   pygame.init()
   screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
   screen.fill(Fond)
   mainloop(screen)

def mainloop(screen):
   running = True
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
   pygame.draw.rect(screen, BLACK, (700, 50, 40, 150), 0)  #MI2b
   pygame.draw.rect(screen, BLACK, (850, 50, 40, 150), 0)  #SOL2b
   pygame.display.update()
   while running == True:
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
      pygame.draw.rect(screen, BLACK, (700, 50, 40, 150), 0)  #MI2b
      pygame.draw.rect(screen, BLACK, (850, 50, 40, 150), 0)  #SOL2b
      pygame.display.update()
      
      for event in pygame.event.get() :
         if event.type == QUIT: 
            pygame.quit()
                


      if event.type == KEYDOWN:

#notes blanches

         if event.key == K_q: #on met “z” car pygame code en qwerty, cela équivaut donc à “a” sur notre clavier
            do.play()
            pygame.draw.rect(screen, BLACK, (50, 50, 70, 200), 0)#DO
            pygame.display.flip()
         if event.key == K_w:
            re.play()
            pygame.draw.rect(screen, BLACK, (125, 50, 70, 200), 0)#RE
            pygame.display.flip()
         if event.key == K_e:
            mi.play()
            pygame.draw.rect(screen, BLACK, (200, 50, 70, 200), 0)#MI
            pygame.display.flip()
         if event.key == K_r:
            fa.play()
            pygame.draw.rect(screen, BLACK, (275, 50, 70, 200), 0)#FA
            pygame.display.flip()
         if event.key == K_t:
            sol.play()
            pygame.draw.rect(screen, BLACK, (350, 50, 70, 200), 0)#SOL
            pygame.display.flip()
         if event.key == K_y:
            la.play()
            pygame.draw.rect(screen, BLACK, (425, 50, 70, 200), 0)#LA
            pygame.display.flip()
         if event.key == K_u:
            si.play()
            pygame.draw.rect(screen, BLACK, (500, 50, 70, 200), 0)#SI
            pygame.display.flip()
         if event.key == K_i:
            do2.play()
            pygame.draw.rect(screen, BLACK, (575, 50, 70, 200), 0)#DO2
            pygame.display.flip()
         if event.key == K_o:
            re2.play()
            pygame.draw.rect(screen, BLACK, (650, 50, 70, 200), 0)#RE2
            pygame.display.flip()
         if event.key == K_p:
            mi2.play()
            pygame.draw.rect(screen, BLACK, (725, 50, 70, 200), 0)#MI2
            pygame.display.flip()
         if event.key == K_LEFTBRACKET:	#LEFTBRACKET = [
            fa2.play()
            pygame.draw.rect(screen, BLACK, (800, 50, 70, 200), 0)#FA2
            pygame.display.flip()
         if event.key == K_RIGHTBRACKET: #RIGHTBRACKET = ]
            sol2.play()
            pygame.draw.rect(screen, BLACK, (875, 50, 70, 200), 0)#SOL2
            pygame.display.flip()

#notes noires
         if event.key == K_2:
            reb.play()
            pygame.draw.rect(screen, WHITE, (100, 50, 40, 150), 0)#REb
            pygame.display.flip()
         if event.key == K_3: 
            mib.play()
            pygame.draw.rect(screen, WHITE, (175, 50, 40, 150), 0)  #MIb
            pygame.display.flip()
         if event.key == K_5:		
            solb.play()
            pygame.draw.rect(screen, WHITE, (325, 50, 40, 150), 0)  #SOLb
            pygame.display.flip()
         if event.key == K_6:
            lab.play()
            pygame.draw.rect(screen, WHITE, (400, 50, 40, 150), 0)  #LAb
            pygame.display.flip()
         if event.key == K_7:
            sib.play()
            pygame.draw.rect(screen, WHITE, (475, 50, 40, 150), 0)  #SIb
            pygame.display.flip()
         if event.key == K_9:
            re2b.play()
            pygame.draw.rect(screen, WHITE, (625, 50, 40, 150), 0)  #RE2b
            pygame.display.flip()
         if event.key == K_0:
            mi2b.play()
            pygame.draw.rect(screen, WHITE, (700, 50, 40, 150), 0)  #MI2b
            pygame.display.flip()
         if event.key == K_EQUALS:	#EQUALS = “=”
            sol2b.play()
            pygame.draw.rect(screen, WHITE, (850, 50, 40, 150), 0)  #SOL2b
            pygame.display.flip()

main()



