import pygame                    #on importe les bibliothèques
from pygame.locals import *

pygame.mixer.init(44100, -16, 2, 4096)
#pre_init(frequency=22050, size=-16, channels=2, buffersize=4096)réduire le temps de latence

pygame.init()  #on initialise pygame

WIDTH = 1300   #largeur de la fenêtre
HEIGHT = 600   #hauteur de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#images de fond
fond1 = pygame.image.load("images/fond1.jpg")
fond2 = pygame.image.load("images/fond2.jpg")
screen.blit(fond1, (0,0))
onglet = pygame.image.load("images/onglet.jpg")
screen.blit(onglet, (1000, 0))
logo = pygame.image.load("images/logo.jpg")
screen.blit(logo, (1000,0))
iconpiano = pygame.image.load("images/iconpiano.jpg")
screen.blit(iconpiano, (1040, 160))
iconsaxo = pygame.image.load("images/iconsaxo.jpg")
screen.blit(iconsaxo, (1180, 160))
iconwood = pygame.image.load("images/iconwood.jpg")
iconnature = pygame.image.load("images/iconnature.jpg")
screen.blit(iconwood, (1050, 510))
screen.blit(iconnature, (1200, 510))
icondrum = pygame.image.load("images/icondrum.jpg")
screen.blit(icondrum, (1050, 320))
screen.blit(icondrum, (1120, 320))
screen.blit(icondrum, (1190, 320))
pygame.display.flip()

#couleurs = (rouge, vert, bleu)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (111, 111, 111)
LIGHTGREY = (190, 190, 190)
Fond = (223,210,220)

#pygame.draw.rect(screen, COULEUR, (x, y, longueur, hauteur)
 
#titre de la fenetre et image
pygame.display.set_caption("GoldenCloud")
icon_32x32 = pygame.image.load("images/background.jpg")
pygame.display.set_icon(icon_32x32)

#sons des notes du piano
instrument = 0

      #lorsqu'on appuie sur une touche
def keydown():
   if event.type == KEYDOWN:

      

#changer de fond
      if event.key == K_n :
         screen.blit(fond2, (0,0))
         pygame.display.flip()
      if event.key == K_b :
         screen.blit(fond1, (0,0))
         pygame.display.flip()


#notes blanches
      if event.key == K_q: #on met “q” car pygame code en qwerty, cela équivaut donc à “a” sur notre clavier
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
         pygame.draw.rect(screen, LIGHTGREY, (215, 50, 55, 150), 0)#MI
         pygame.draw.rect(screen, LIGHTGREY, (200, 200, 70, 50), 0)#MI
         pygame.display.flip()
      if event.key == K_r:
         fa.play()
         pygame.draw.rect(screen, LIGHTGREY, (275, 50, 50, 150), 0)#FA
         pygame.draw.rect(screen, LIGHTGREY, (275, 200, 70, 50), 0)#FA
         pygame.display.flip()
      if event.key == K_t:
         sol.play()
         pygame.draw.rect(screen, LIGHTGREY, (365, 50, 35, 150), 0)#SOL
         pygame.draw.rect(screen, LIGHTGREY, (350, 200, 70, 50), 0)#SOL
         pygame.display.flip()
      if event.key == K_y:
         la.play()
         pygame.draw.rect(screen, LIGHTGREY, (440, 50, 35, 150), 0)#LA
         pygame.draw.rect(screen, LIGHTGREY, (425, 200, 70, 50), 0)#LA
         pygame.display.flip()
      if event.key == K_u:
         si.play()
         pygame.draw.rect(screen, LIGHTGREY, (515, 50, 55, 150), 0)#SI
         pygame.draw.rect(screen, LIGHTGREY, (500, 200, 70, 50), 0)#SI
         pygame.display.flip()
      if event.key == K_i:
         do2.play()
         pygame.draw.rect(screen, LIGHTGREY, (575, 50, 50, 150), 0)#DO2
         pygame.draw.rect(screen, LIGHTGREY, (575, 200, 70, 50), 0)#DO2
         pygame.display.flip()
      if event.key == K_o:
         re2.play()
         pygame.draw.rect(screen, LIGHTGREY, (665, 50, 35, 150), 0)#RE2
         pygame.draw.rect(screen, LIGHTGREY, (650, 200, 70, 50), 0)#RE2
         pygame.display.flip()
      if event.key == K_p:
         mi2.play()
         pygame.draw.rect(screen, LIGHTGREY, (740, 50, 55, 150), 0)#MI2
         pygame.draw.rect(screen, LIGHTGREY, (725, 200, 70, 50), 0)#MI2
         pygame.display.flip()
      if event.key == K_LEFTBRACKET:	#LEFTBRACKET = [
         fa2.play()
         pygame.draw.rect(screen, LIGHTGREY, (800, 50, 50, 150), 0)#FA2
         pygame.draw.rect(screen, LIGHTGREY, (800, 200, 70, 50), 0)#FA2
         pygame.display.flip()
      if event.key == K_RIGHTBRACKET: #RIGHTBRACKET = ]
         sol2.play()
         pygame.draw.rect(screen, LIGHTGREY, (890, 50, 55, 150), 0)#SOL2
         pygame.draw.rect(screen, LIGHTGREY, (875, 200, 70, 50), 0)#SOL2
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
         pygame.draw.rect(screen, WHITE, (215, 50, 55, 150), 0)#MI
         pygame.draw.rect(screen, WHITE, (200, 200, 70, 50), 0)#MI
         pygame.display.flip()
      if event.key == K_r:
         fa.stop()
         pygame.draw.rect(screen, WHITE, (275, 50, 50, 150), 0)#FA
         pygame.draw.rect(screen, WHITE, (275, 200, 70, 50), 0)#FA
         pygame.display.flip()
      if event.key == K_t:
         sol.stop()
         pygame.draw.rect(screen, WHITE, (365, 50, 35, 150), 0)#SOL
         pygame.draw.rect(screen, WHITE, (350, 200, 70, 50), 0)#SOL
         pygame.display.flip()
      if event.key == K_y:
         la.stop()
         pygame.draw.rect(screen, WHITE, (440, 50, 35, 150), 0)#LA
         pygame.draw.rect(screen, WHITE, (425, 200, 70, 50), 0)#LA
         pygame.display.flip()
      if event.key == K_u:
         si.stop()
         pygame.draw.rect(screen, WHITE, (515, 50, 55, 150), 0)#SI
         pygame.draw.rect(screen, WHITE, (500, 200, 70, 50), 0)#SI
         pygame.display.flip()
      if event.key == K_i:
         do2.stop()
         pygame.draw.rect(screen, WHITE, (575, 50, 50, 150), 0)#DO2
         pygame.draw.rect(screen, WHITE, (575, 200, 70, 50), 0)#DO2
         pygame.display.flip()
      if event.key == K_o:
         re2.stop()
         pygame.draw.rect(screen, WHITE, (665, 50, 35, 150), 0)#RE2
         pygame.draw.rect(screen, WHITE, (650, 200, 70, 50), 0)#RE2
         pygame.display.flip()
      if event.key == K_p:
         mi2.stop()
         pygame.draw.rect(screen, WHITE, (740, 50, 55, 150), 0)#MI2
         pygame.draw.rect(screen, WHITE, (725, 200, 70, 50), 0)#MI2
         pygame.display.flip()
      if event.key == K_LEFTBRACKET:
         fa2.stop()
         pygame.draw.rect(screen, WHITE, (800, 50, 50, 150), 0)#FA2
         pygame.draw.rect(screen, WHITE, (800, 200, 70, 50), 0)#FA2
         pygame.display.flip()
      if event.key == K_RIGHTBRACKET:
         sol2.stop()
         pygame.draw.rect(screen, WHITE, (890, 50, 55, 150), 0)#SOL2
         pygame.draw.rect(screen, WHITE, (875, 200, 70, 50), 0)#SOL2
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



def creaTexteObj(texte, Police):
   texteSurface = Police.render(texte, True, WHITE)
   return texteSurface, texteSurface.get_rect()
   
def message(texte):
   #on établit les polices d'écriture
   Titre = pygame.font.Font('police/TitilliumWeb-SemiBold.ttf', 40)
   GrosTexte = pygame.font.Font('police/TitilliumWeb-SemiBold.ttf', 130)
   PetitTexte = pygame.font.Font('police/TitilliumWeb-ExtraLight.ttf', 25)
   TexteExplicatif = pygame.font.Font('police/TitilliumWeb-ExtraLight.ttf', 20)


   GrosTexteSurf, GrosTexteRect = creaTexteObj(texte, GrosTexte)
   GrosTexteRect.center = 500, 350
   screen.blit(GrosTexteSurf, GrosTexteRect)

   
   PetitTexteSurf, PetitTexteRect = creaTexteObj("Appuyez sur une touche pour découvrir votre clavier...", PetitTexte)
   PetitTexteRect.center = 500, 480
   screen.blit(PetitTexteSurf, PetitTexteRect)


   InstructionInstrument = "Choisissez votre instrument :" 
   ComInstrument = "C                                  V"
   InstructionSon = "Plus fort :          Moins Fort : " 
   ComSon = "W                                  X"
   InstructionFond = "Changez le fond :"  
   ComFond = "B                                 N"
   
   TexteExplicatifSurf, TexteExplicatifRect = creaTexteObj(InstructionInstrument, TexteExplicatif)
   TexteExplicatifRect.center = 1150, 100
   screen.blit(TexteExplicatifSurf, TexteExplicatifRect)
   
   TexteExplicatifSurf, TexteExplicatifRect = creaTexteObj(ComInstrument, TexteExplicatif)
   TexteExplicatifRect.center = 1150, 130
   screen.blit(TexteExplicatifSurf, TexteExplicatifRect)
   
   TexteExplicatifSurf, TexteExplicatifRect = creaTexteObj(InstructionSon, TexteExplicatif)
   TexteExplicatifRect.center = 1150, 325
   screen.blit(TexteExplicatifSurf, TexteExplicatifRect)
   
   TexteExplicatifSurf, TexteExplicatifRect = creaTexteObj(ComSon, TexteExplicatif)
   TexteExplicatifRect.center = 1150, 355
   screen.blit(TexteExplicatifSurf, TexteExplicatifRect)
   
   TexteExplicatifSurf, TexteExplicatifRect = creaTexteObj(InstructionFond, TexteExplicatif)
   TexteExplicatifRect.center = 1150, 460
   screen.blit(TexteExplicatifSurf, TexteExplicatifRect)
   
   TexteExplicatifSurf, TexteExplicatifRect = creaTexteObj(ComFond, TexteExplicatif)
   TexteExplicatifRect.center = 1150, 490
   screen.blit(TexteExplicatifSurf, TexteExplicatifRect)
   
   pygame.display.update()

def affichageTexte():
   message('Bienvenue !')     
   

pygame.init()
running = True
pygame.display.update()
while running == True:
   while instrument == 0 :
      affichageTexte()
      for event in pygame.event.get() :
         if event.type == QUIT: 
            instrument = 3
         if event.type == KEYDOWN :
            if event.key == K_v :
               instrument = 1
         if event.type == MOUSEBUTTONDOWN and event.button == 1 :
            if 1220<event.pos[0]<1250 and 510<event.pos[1]<560:
               pygame.draw.rect(screen, WHITE, (850, 250, 40, 150), 0)
               pygame.display.flip()
            if 1200<event.pos[0]<1220 and 510<event.pos[1]<560:
               pygame.draw.rect(screen, BLACK, (850, 250, 40, 150), 0)
               pygame.display.flip()
         keydown()
         
      do = pygame.mixer.Sound("sons/Piano/1Do.wav")
      reb = pygame.mixer.Sound("sons/Piano/2Reb.wav")
      re = pygame.mixer.Sound("sons/Piano/3Re.wav")
      mib = pygame.mixer.Sound("sons/Piano/4Mib.wav")
      mi = pygame.mixer.Sound("sons/Piano/5Mi.wav")
      fa = pygame.mixer.Sound("sons/Piano/6Fa.wav")
      solb = pygame.mixer.Sound("sons/Piano/7Solb.wav")
      sol = pygame.mixer.Sound("sons/Piano/8Sol.wav")
      lab = pygame.mixer.Sound("sons/Piano/9Lab.wav")
      la = pygame.mixer.Sound("sons/Piano/10La.wav")
      sib = pygame.mixer.Sound("sons/Piano/11Sib.wav")
      si = pygame.mixer.Sound("sons/Piano/12Si.wav")
      do2 = pygame.mixer.Sound("sons/Piano/13Do2.wav")
      re2 = pygame.mixer.Sound("sons/Piano/14Re2.wav")
      re2b = pygame.mixer.Sound("sons/Piano/15Reb2.wav")
      mi2 = pygame.mixer.Sound("sons/Piano/16Mi2.wav")
      mi2b = pygame.mixer.Sound("sons/Piano/17Mib2.wav")
      fa2 = pygame.mixer.Sound("sons/Piano/18Fa2.wav")
      sol2 = pygame.mixer.Sound("sons/Piano/19Sol2.wav")
      sol2b = pygame.mixer.Sound("sons/Piano/20Solb2.wav")

   while instrument == 1 :

      affichageTexte()
      for event in pygame.event.get() :
         if event.type == QUIT: 
            instrument = 3
         if event.type == KEYDOWN :
            if event.key == K_c :
               instrument = 0
         keydown()
         
      do = pygame.mixer.Sound("sons/Saxo/1Do.wav")
      reb = pygame.mixer.Sound("sons/Saxo/2Reb.wav")
      re = pygame.mixer.Sound("sons/Saxo/3Re.wav")
      mib = pygame.mixer.Sound("sons/Saxo/4Mib.wav")
      mi = pygame.mixer.Sound("sons/Saxo/5Mi.wav")
      fa = pygame.mixer.Sound("sons/Saxo/6Fa.wav")
      solb = pygame.mixer.Sound("sons/Saxo/7Solb.wav")
      sol = pygame.mixer.Sound("sons/Saxo/8Sol.wav")
      lab = pygame.mixer.Sound("sons/Saxo/9Lab.wav")
      la = pygame.mixer.Sound("sons/Saxo/10La.wav")
      sib = pygame.mixer.Sound("sons/Saxo/11Sib.wav")
      si = pygame.mixer.Sound("sons/Saxo/12Si.wav")
      do2 = pygame.mixer.Sound("sons/Saxo/13Do2.wav")
      re2 = pygame.mixer.Sound("sons/Saxo/14Re2.wav")
      re2b = pygame.mixer.Sound("sons/Saxo/15Reb2.wav")
      mi2 = pygame.mixer.Sound("sons/Saxo/16Mi2.wav")
      mi2b = pygame.mixer.Sound("sons/Saxo/17Mib2.wav")
      fa2 = pygame.mixer.Sound("sons/Saxo/18Fa2.wav")
      sol2 = pygame.mixer.Sound("sons/Saxo/19Sol2.wav")
      sol2b = pygame.mixer.Sound("sons/Saxo/20Solb2.wav")

   if instrument == 3:
      running = False
      pygame.quit()
