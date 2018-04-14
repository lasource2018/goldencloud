import pygame                    #on importe les bibliothèques
from pygame.locals import *

pygame.mixer.init(44100, -16, 2, 4096)  #pre_init(frequency=22050, size=-16, channels=2, buffersize=4096)réduire le temps de latence

pygame.init()  #on initialise pygame

WIDTH = 1000   #largeur de la fenêtre
HEIGHT = 500   #hauteur de la fenêtre

#couleurs = (rouge, vert, bleu)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (111, 111, 111)
LIGHTGREY = (190, 190, 190)
Fond = (223,210,220)
 
#titre de la fenetre et image
pygame.display.set_caption("GoldenCloud")
icon_32x32 = pygame.image.load("images/background.jpg")
pygame.display.set_icon(icon_32x32)

#sons des notes
do = pygame.mixer.Sound("sons/1DO_-_A.wav")
reb = pygame.mixer.Sound("sons/2Reb_-_é.wav")
re = pygame.mixer.Sound("sons/3R_-_Z.wav")
mib = pygame.mixer.Sound("sons/4Mib_-__.wav")
mi = pygame.mixer.Sound("sons/5Mi_-_E.wav")
fa = pygame.mixer.Sound("sons/6Fa_-_R.wav")
solb = pygame.mixer.Sound("sons/7solb-_).wav")
sol = pygame.mixer.Sound("sons/8Sol_-_T.wav")
lab = pygame.mixer.Sound("sons/9Lab_-_G_ou_§T.wav")
la = pygame.mixer.Sound("sons/10La-_Y.wav")
sib = pygame.mixer.Sound("sons/11Sib_-_è.wav")
si = pygame.mixer.Sound("sons/12Si_-_U.wav")
do2 = pygame.mixer.Sound("sons/13Do2_-_I.wav")
re2 = pygame.mixer.Sound("sons/14Re2-_O.wav")
re2b = pygame.mixer.Sound("sons/15Ré2b_-_ç.wav")
mi2 = pygame.mixer.Sound("sons/16Mi2_-_P.wav")
mi2b = pygame.mixer.Sound("sons/17Mi2b_-_à.wav")
fa2 = pygame.mixer.Sound("sons/18Fa2_-_¨.wav")
sol2 = pygame.mixer.Sound("sons/19Sol2-$.wav")
sol2b = pygame.mixer.Sound("sons/20Sol2b-=ou-.wav")

def creaTexteObj(texte, Police):
   texteSurface = Police.render(texte, True, WHITE)
   return texteSurface, texteSurface.get_rect()
   
def message(texte):
   #on établit les polices d'écriture
   GrosTexte = pygame.font.Font('police/BradBunR.ttf', 130)
   PetitTexte = pygame.font.Font('police/BradBunR.ttf', 20)
   TexteExplicatif = pygame.font.Font('police/BradBunR.ttf', 15)

   GrosTexteSurf, GrosTexteRect = creaTexteObj(texte, GrosTexte)
   GrosTexteRect.center = 250, 400
   screen.blit(GrosTexteSurf, GrosTexteRect)
   
   PetitTexteSurf, PetitTexteRect = creaTexteObj("Appuyez sur une touche pour découvrir votre clavier...", PetitTexte)
   PetitTexteRect.center = 250, 470
   screen.blit(PetitTexteSurf, PetitTexteRect)

   TexteExplicatifSurf, TexteExplicatifRect = creaTexteObj('instructions', TexteExplicatif)
   TexteExplicatifRect.center = 750, 350
   screen.blit(TexteExplicatifSurf, TexteExplicatifRect)
   
   pygame.display.update()

def affichageTexte():
   message('Bienvenu!')
   
def mainloop(screen):
   running = True
   
   pygame.display.update()
   while running == True:
      #pygame.draw.rect(screen, COULEUR, (x, y, longueur, hauteur)
      
      for event in pygame.event.get() :
         if event.type == QUIT: 
            pygame.quit()


      affichageTexte()

            
      #lorsqu'on appuie sur une touche
      if event.type == KEYDOWN:

#notes blanches

         if event.key == K_q: #on met “z” car pygame code en qwerty, cela équivaut donc à “a” sur notre clavier
            do.play()
            pygame.draw.rect(screen, LIGHTGREY, (50, 50, 50, 150), 0)#DO
            pygame.draw.rect(screen, LIGHTGREY, (50, 200, 70, 50), 0)#DO
            pygame.display.flip()
         if event.key == K_w:
            re.play()
            pygame.draw.rect(screen, LIGHTGREY, (140, 50, 35, 150), 0)#RE
            pygame.draw.rect(screen, LIGHTGREY, (125, 200, 70,50),0)#RE
            pygame.display.flip()
         if event.key == K_e:
            mi.play()
            pygame.draw.rect(screen, LIGHTGREY, (200, 50, 70, 200), 0)#MI
            pygame.display.flip()
         if event.key == K_r:
            fa.play()
            pygame.draw.rect(screen, LIGHTGREY, (275, 50, 70, 200), 0)#FA
            pygame.display.flip()
         if event.key == K_t:
            sol.play()
            pygame.draw.rect(screen, LIGHTGREY, (350, 50, 70, 200), 0)#SOL
            pygame.display.flip()
         if event.key == K_y:
            la.play()
            pygame.draw.rect(screen, LIGHTGREY, (425, 50, 70, 200), 0)#LA
            pygame.display.flip()
         if event.key == K_u:
            si.play()
            pygame.draw.rect(screen, LIGHTGREY, (500, 50, 70, 200), 0)#SI
            pygame.display.flip()
         if event.key == K_i:
            do2.play()
            pygame.draw.rect(screen, LIGHTGREY, (575, 50, 70, 200), 0)#DO2
            pygame.display.flip()
         if event.key == K_o:
            re2.play()
            pygame.draw.rect(screen, LIGHTGREY, (650, 50, 70, 200), 0)#RE2
            pygame.display.flip()
         if event.key == K_p:
            mi2.play()
            pygame.draw.rect(screen, LIGHTGREY, (725, 50, 70, 200), 0)#MI2
            pygame.display.flip()
         if event.key == K_LEFTBRACKET:	#LEFTBRACKET = [
            fa2.play()
            pygame.draw.rect(screen, LIGHTGREY, (800, 50, 70, 200), 0)#FA2
            pygame.display.flip()
         if event.key == K_RIGHTBRACKET: #RIGHTBRACKET = ]
            sol2.play()
            pygame.draw.rect(screen, LIGHTGREY, (875, 50, 70, 200), 0)#SOL2
            pygame.display.flip()

#notes noires
         if event.key == K_2:
            reb.play()
            pygame.draw.rect(screen, DARKGREY, (100, 50, 40, 150), 0)#REb
            pygame.display.flip()
         if event.key == K_3: 
            mib.play()
            pygame.draw.rect(screen, DARKGREY, (175, 50, 40, 150), 0)  #MIb
            pygame.display.flip()
         if event.key == K_5:		
            solb.play()
            pygame.draw.rect(screen, DARKGREY, (325, 50, 40, 150), 0)  #SOLb
            pygame.display.flip()
         if event.key == K_6:
            lab.play()
            pygame.draw.rect(screen, DARKGREY, (400, 50, 40, 150), 0)  #LAb
            pygame.display.flip()
         if event.key == K_7:
            sib.play()
            pygame.draw.rect(screen, DARKGREY, (475, 50, 40, 150), 0)  #SIb
            pygame.display.flip()
         if event.key == K_9:
            re2b.play()
            pygame.draw.rect(screen, DARKGREY, (625, 50, 40, 150), 0)  #RE2b
            pygame.display.flip()
         if event.key == K_0:
            mi2b.play()
            pygame.draw.rect(screen, DARKGREY, (700, 50, 40, 150), 0)  #MI2b
            pygame.display.flip()
         if event.key == K_EQUALS:	#EQUALS = “=”
            sol2b.play()
            pygame.draw.rect(screen, DARKGREY, (850, 50, 40, 150), 0)  #SOL2b
            pygame.display.flip()

      #lorque la pression sur la touche est relachée
      if event.type == KEYUP:

#notes blanches
         
         if event.key == K_q:
            do.stop()
            pygame.draw.rect(screen, WHITE, (50, 50, 50, 150), 0)#DO
            pygame.draw.rect(screen, WHITE, (50, 200, 70, 50), 0)#DO
            pygame.display.flip()
         if event.key == K_w:
            re.stop()
            pygame.draw.rect(screen, WHITE, (140, 50, 35, 150), 0)#RE
            pygame.draw.rect(screen, WHITE, (125, 200, 70,50),0)#RE
            pygame.display.flip()
         if event.key == K_e:
            mi.stop()
            pygame.draw.rect(screen, WHITE, (200, 50, 70, 200), 0)  #MI
            pygame.display.flip()
         if event.key == K_r:
            fa.stop()
            pygame.draw.rect(screen, WHITE, (275, 50, 70, 200), 0)  #FA
            pygame.display.flip()
         if event.key == K_t:
            sol.stop()
            pygame.draw.rect(screen, WHITE, (350, 50, 70, 200), 0)  #SOL
            pygame.display.flip()
         if event.key == K_y:
            la.stop()
            pygame.draw.rect(screen, WHITE, (425, 50, 70, 200), 0)  #LA
            pygame.display.flip()
         if event.key == K_u:
            si.stop()
            pygame.draw.rect(screen, WHITE, (500, 50, 70, 200), 0)  #SI
            pygame.display.flip()
         if event.key == K_i:
            do2.stop()
            pygame.draw.rect(screen, WHITE, (575, 50, 70, 200), 0)  #DO2
            pygame.display.flip()
         if event.key == K_o:
            re2.stop()
            pygame.draw.rect(screen, WHITE, (650, 50, 70, 200), 0)  #RE2
            pygame.display.flip()
         if event.key == K_p:
            mi2.stop()
            pygame.draw.rect(screen, WHITE, (725, 50, 70, 200), 0)  #MI2
            pygame.display.flip()
         if event.key == K_LEFTBRACKET:
            fa2.stop()
            pygame.draw.rect(screen, WHITE, (800, 50, 70, 200), 0)  #FA2
            pygame.display.flip()
         if event.key == K_RIGHTBRACKET:
            sol2.stop()
            pygame.draw.rect(screen, WHITE, (875, 50, 70, 200), 0)  #SOL2
            pygame.display.flip()

#notes noires
            
         if event.key == K_2:
            reb.stop()
            pygame.draw.rect(screen, BLACK, (100, 50, 40, 150), 0)  #REb
            pygame.display.update()
         if event.key == K_3:
            mib.stop()
            pygame.draw.rect(screen, BLACK, (175, 50, 40, 150), 0)  #MIb
            pygame.display.flip()
         if event.key == K_5:
            solb.stop()
            pygame.draw.rect(screen, BLACK, (325, 50, 40, 150), 0)  #SOLb
            pygame.display.flip()
         if event.key == K_6:
            lab.stop()
            pygame.draw.rect(screen, BLACK, (400, 50, 40, 150), 0)  #LAb
            pygame.display.flip()
         if event.key == K_7:
            sib.stop()
            pygame.draw.rect(screen, BLACK, (475, 50, 40, 150), 0)  #SIb
            pygame.display.flip()
         if event.key == K_9:
            re2b.stop()
            pygame.draw.rect(screen, BLACK, (625, 50, 40, 150), 0)  #RE2b
            pygame.display.flip()
         if event.key == K_0:
            mi2b.stop()
            pygame.draw.rect(screen, BLACK, (700, 50, 40, 150), 0)  #MI2b
            pygame.display.flip()
         if event.key == K_EQUALS:
            sol2b.stop()
            pygame.draw.rect(screen, BLACK, (850, 50, 40, 150), 0)  #SOL2b
            pygame.display.flip()
            

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(Fond)
mainloop(screen)


