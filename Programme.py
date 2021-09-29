#Importer la librairie pygame
import pygame
from pygame.locals import *
import pygame.mixer
pygame.init()
pygame.display.set_caption("Bataille Navale")

# Ouvrir une fenêtre Pygame
taille = largeur, hauteur = 1024,768
ecran = pygame.display.set_mode((taille))

#Initialiser les variables
Continuer = 0 # Créer la variable Continuer
placement = 1
joueur = 1
abstouchej1self = []
ordtouchej1self = []
abstouchej2self = []
ordtouchej2self = []
absmissj1self = []
ordmissj1self = []
absmissj2self = []
ordmissj2self = []
abstouchej1ennemi = []
ordtouchej1ennemi = []
abstouchej2ennemi = []
ordtouchej2ennemi = []
absmissj1ennemi = []
ordmissj1ennemi = []
absmissj2ennemi = []
ordmissj2ennemi = []
absbateauxj1 = [593,593,593,593,593]
ordbateauxj1 = [336,336,336,336,336]
absbateauxj2 = [593,593,593,593,593]
ordbateauxj2 = [336,336,336,336,336]
j1pret = 0
j2pret = 0
choisi = 0
Collisions = 0
clicutilise = 0
PVj1 = [5,4,3,3,2]
PVj2 = [5,4,3,3,2]
Verticalj1 = [0,0,0,0,0]
Verticalj2 = [0,0,0,0,0]
Son = True

# Création des images et "Rects" associés
Menu = pygame.image.load("images/menu/Menu.png")
sonon = pygame.image.load("images/menu/sonon.png")
sonoff = pygame.image.load("images/menu/sonoff.png")
Partie = pygame.image.load("images/Partie.png")
grille = pygame.image.load("images/grille.png")
grillesmall = pygame.image.load("images/grillesmall.png")
preparation = pygame.image.load("images/preparation.png")
attaque = pygame.image.load("images/attaque.png")
defense = pygame.image.load("images/defense.png")
termine = pygame.image.load("images/termine.png")
retourner = pygame.image.load("images/retourner.png")
tirer = pygame.image.load("images/tirer.png")
joueur1 = pygame.image.load("images/joueur1.png")
joueur2 = pygame.image.load("images/joueur2.png")
changementj1 = pygame.image.load("images/changementj1.png")
changementj2 = pygame.image.load("images/changementj2.png")
bateauxaplacer = pygame.image.load("images/bateauxaplacer.png")
choixtir = pygame.image.load("images/choixtir.png")
miss = pygame.image.load("images/miss.png")
misssmall = pygame.image.load("images/misssmall.png")
tir_rect = misssmall.get_rect()
touche = pygame.image.load("images/touche.png")
touchesmall = pygame.image.load("images/touchesmall.png")
porteavion = pygame.image.load("images/bateaux/live/porteavion.png")
porteavion_rect = porteavion.get_rect()
porteavionVertical = pygame.image.load("images/bateaux/live/porteavionVertical.png")
porteavionVertical_rect = porteavionVertical.get_rect()
porteavionj1_rect = porteavion_rect
porteavionj2_rect = porteavion_rect
croiseur = pygame.image.load("images/bateaux/live/croiseur.png")
croiseur_rect = croiseur.get_rect()
croiseurVertical = pygame.image.load("images/bateaux/live/croiseurVertical.png")
croiseurVertical_rect = croiseurVertical.get_rect()
croiseurj1_rect = croiseur_rect
croiseurj2_rect = croiseur_rect
smct = pygame.image.load("images/bateaux/live/smct.png")
smct_rect = smct.get_rect()
smctVertical = pygame.image.load("images/bateaux/live/smctVertical.png")
smctVertical_rect = smctVertical.get_rect()
sousmarinj1_rect = smct_rect
sousmarinj2_rect = smct_rect
contretorpij1_rect = smct_rect
contretorpij2_rect = smct_rect
torpilleur = pygame.image.load("images/bateaux/live/torpilleur.png")
torpilleur_rect = torpilleur.get_rect()
torpilleurVertical = pygame.image.load("images/bateaux/live/torpilleurVertical.png")
torpilleurVertical_rect = torpilleurVertical.get_rect()
torpilleurj1_rect = torpilleur_rect
torpilleurj2_rect = torpilleur_rect
padead = pygame.image.load("images/bateaux/dead/big/padead.png")
pavdead = pygame.image.load("images/bateaux/dead/big/pavdead.png")
cdead = pygame.image.load("images/bateaux/dead/big/cdead.png")
cvdead = pygame.image.load("images/bateaux/dead/big/cvdead.png")
smctdead = pygame.image.load("images/bateaux/dead/big/smctdead.png")
smctvdead = pygame.image.load("images/bateaux/dead/big/smctvdead.png")
tdead = pygame.image.load("images/bateaux/dead/big/tdead.png")
tvdead = pygame.image.load("images/bateaux/dead/big/tvdead.png")
padeadsmall = pygame.image.load("images/bateaux/dead/small/padead.png")
pavdeadsmall = pygame.image.load("images/bateaux/dead/small/pavdead.png")
cdeadsmall = pygame.image.load("images/bateaux/dead/small/cdead.png")
cvdeadsmall = pygame.image.load("images/bateaux/dead/small/cvdead.png")
smctdeadsmall = pygame.image.load("images/bateaux/dead/small/smctdead.png")
smctvdeadsmall = pygame.image.load("images/bateaux/dead/small/smctvdead.png")
tdeadsmall = pygame.image.load("images/bateaux/dead/small/tdead.png")
tvdeadsmall = pygame.image.load("images/bateaux/dead/small/tvdead.png")
PlacementPA = pygame.image.load("images/PlacementPA.png")
PlacementC = pygame.image.load("images/PlacementC.png")
PlacementSM = pygame.image.load("images/PlacementSM.png")
PlacementCT = pygame.image.load("images/PlacementCT.png")
PlacementT = pygame.image.load("images/PlacementT.png")
Collision = pygame.image.load("images/Collision.png")
porteavionj1_rect = porteavionj1_rect.move(593,336)
croiseurj1_rect = croiseurj1_rect.move(580,221)
contretorpij1_rect = contretorpij1_rect.move(580,267)
sousmarinj1_rect = sousmarinj1_rect.move(708,267)
torpilleurj1_rect = torpilleurj1_rect.move(749,221)
porteavionj2_rect = porteavionj2_rect.move(593,336)
croiseurj2_rect = croiseurj2_rect.move(580,221)
contretorpij2_rect = contretorpij2_rect.move(580,267)
sousmarinj2_rect = sousmarinj2_rect.move(708,267)
torpilleurj2_rect = torpilleurj2_rect.move(749,221)
Mode = Partie
actuel = preparation
action = termine
pygame.key.set_repeat(1,125)
pygame.time.Clock().tick(50) # Limiter le nombre de boucles à 50 par seconde

# Ajout des Sons
Explosion = pygame.mixer.Sound("Sons/Explosion.wav")
Intro = pygame.mixer.Sound("Sons/Intro.wav")

#Menu
while Continuer==0 :
    Intro.play()
    for event in pygame.event.get():
        if event.type == QUIT:
            Continuer = 2
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE :
                Continuer = 2
        if event.type == MOUSEBUTTONUP and event.button == 1 :
            clicutilise=0
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and clicutilise==0 :
            if event.pos[0]>=339 and event.pos[0]<=638 and event.pos[1]>=260 and event.pos[1]<=359 :
                Continuer=1
            if event.pos[0]>=700 and event.pos[0]<=854 and event.pos[1]>=350 and event.pos[1]<=508 :
                if Son==True and clicutilise==0 :
                    Son=False
                    Intro.stop()
                    clicutilise=1
                if Son==False and clicutilise==0 :
                    Son=True
                    Intro.play()
                    clicutilise=1
            if event.pos[0]>=341 and event.pos[0]<=640 and event.pos[1]>=401 and event.pos[1]<=500 :
                print("Programme par Alistair Lewin")
                print("Graphismes et Textures par Jordan Ouvrard")
                print("Logo et Audio par Florentin Heuzé")
            if event.pos[0]>=341 and event.pos[0]<=640 and event.pos[1]>=541 and event.pos[1]<=640 :
                Continuer=2
                Intro.stop()
    ecran.blit(Menu,(0,0))
    if Son==True :
        ecran.blit(sonon,(700,350))
    else :
        ecran.blit(sonoff,(700,350))
    pygame.display.flip() #Rafraîchissement de la fenêtre


#Boucle principale
while Continuer==1 and PVj1[0]+PVj1[1]+PVj1[2]+PVj1[3]+PVj1[4]>0 and PVj2[0]+PVj2[1]+PVj2[2]+PVj2[3]+PVj2[4]>0 :
        if joueur==1 :
            if actuel==preparation and j1pret==0 :
                for event in pygame.event.get():
                    if event.type == QUIT:
                        Continuer=0
                    if event.type == KEYDOWN:
                        if Verticalj1[placement-1]==0 :
                            if placement==1 :
                                if event.key == K_LEFT:
                                    if absbateauxj1[0]>593 :
                                        absbateauxj1[0]=absbateauxj1[0]-41
                                        porteavionj1_rect = porteavionj1_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj1[0]<798 :
                                        absbateauxj1[0]=absbateauxj1[0]+41
                                        porteavionj1_rect = porteavionj1_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj1[0]>337 :
                                        ordbateauxj1[0]=ordbateauxj1[0]-41
                                        porteavionj1_rect = porteavionj1_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj1[0]<666 :
                                        ordbateauxj1[0]=ordbateauxj1[0]+41
                                        porteavionj1_rect = porteavionj1_rect.move(0,41)
                            if placement==2 :
                                if event.key == K_LEFT:
                                    if absbateauxj1[1]>593 :
                                        absbateauxj1[1]=absbateauxj1[1]-41
                                        croiseurj1_rect = croiseurj1_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj1[1]<839 :
                                        absbateauxj1[1]=absbateauxj1[1]+41
                                        croiseurj1_rect = croiseurj1_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj1[1]>337 :
                                        ordbateauxj1[1]=ordbateauxj1[1]-41
                                        croiseurj1_rect = croiseurj1_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj1[1]<666 :
                                        ordbateauxj1[1]=ordbateauxj1[1]+41
                                        croiseurj1_rect = croiseurj1_rect.move(0,41)
                            if placement==3 :
                                if event.key == K_LEFT:
                                    if absbateauxj1[2]>593 :
                                            absbateauxj1[2]=absbateauxj1[2]-41
                                            sousmarinj1_rect = sousmarinj1_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj1[2]<880 :
                                        absbateauxj1[2]=absbateauxj1[2]+41
                                        sousmarinj1_rect = sousmarinj1_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj1[2]>337 :
                                        ordbateauxj1[2]=ordbateauxj1[2]-41
                                        sousmarinj1_rect = sousmarinj1_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj1[2]<666 :
                                        ordbateauxj1[2]=ordbateauxj1[2]+41
                                        sousmarinj1_rect = sousmarinj1_rect.move(0,41)
                            if placement==4 :
                                if event.key == K_LEFT:
                                    if absbateauxj1[3]>593 :
                                        absbateauxj1[3]=absbateauxj1[3]-41
                                        contretorpij1_rect = contretorpij1_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj1[3]<880 :
                                        absbateauxj1[3]=absbateauxj1[3]+41
                                        contretorpij1_rect = contretorpij1_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj1[3]>337 :
                                        ordbateauxj1[3]=ordbateauxj1[3]-41
                                        contretorpij1_rect = contretorpij1_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj1[3]<666 :
                                        ordbateauxj1[3]=ordbateauxj1[3]+41
                                        contretorpij1_rect = contretorpij1_rect.move(0,41)
                            if placement==5 :
                                if event.key == K_LEFT:
                                    if absbateauxj1[4]>593 :
                                        absbateauxj1[4]=absbateauxj1[4]-41
                                        torpilleurj1_rect = torpilleurj1_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj1[4]<921 :
                                        absbateauxj1[4]=absbateauxj1[4]+41
                                        torpilleurj1_rect = torpilleurj1_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj1[4]>337 :
                                        ordbateauxj1[4]=ordbateauxj1[4]-41
                                        torpilleurj1_rect = torpilleurj1_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj1[4]<666 :
                                        ordbateauxj1[4]=ordbateauxj1[4]+41
                                        torpilleurj1_rect = torpilleurj1_rect.move(0,41)
                        if Verticalj1[placement-1]==1 :
                            if placement==1 :
                                if event.key == K_LEFT:
                                    if absbateauxj1[0]>593 :
                                        absbateauxj1[0]=absbateauxj1[0]-41
                                        porteavionj1_rect = porteavionj1_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj1[0]<962 :
                                        absbateauxj1[0]=absbateauxj1[0]+41
                                        porteavionj1_rect = porteavionj1_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj1[0]>337 :
                                        ordbateauxj1[0]=ordbateauxj1[0]-41
                                        porteavionj1_rect = porteavionj1_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj1[0]<502 :
                                        ordbateauxj1[0]=ordbateauxj1[0]+41
                                        porteavionj1_rect = porteavionj1_rect.move(0,41)
                            if placement==2 :
                                if event.key == K_LEFT:
                                    if absbateauxj1[1]>593 :
                                        absbateauxj1[1]=absbateauxj1[1]-41
                                        croiseurj1_rect = croiseurj1_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj1[1]<962 :
                                        absbateauxj1[1]=absbateauxj1[1]+41
                                        croiseurj1_rect = croiseurj1_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj1[1]>337 :
                                        ordbateauxj1[1]=ordbateauxj1[1]-41
                                        croiseurj1_rect = croiseurj1_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj1[1]<543 :
                                        ordbateauxj1[1]=ordbateauxj1[1]+41
                                        croiseurj1_rect = croiseurj1_rect.move(0,41)
                            if placement==3 :
                                if event.key == K_LEFT:
                                    if absbateauxj1[2]>593 :
                                            absbateauxj1[2]=absbateauxj1[2]-41
                                            sousmarinj1_rect = sousmarinj1_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj1[2]<962 :
                                        absbateauxj1[2]=absbateauxj1[2]+41
                                        sousmarinj1_rect = sousmarinj1_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj1[2]>337 :
                                        ordbateauxj1[2]=ordbateauxj1[2]-41
                                        sousmarinj1_rect = sousmarinj1_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj1[2]<584 :
                                        ordbateauxj1[2]=ordbateauxj1[2]+41
                                        sousmarinj1_rect = sousmarinj1_rect.move(0,41)
                            if placement==4 :
                                if event.key == K_LEFT:
                                    if absbateauxj1[3]>593 :
                                        absbateauxj1[3]=absbateauxj1[3]-41
                                        contretorpij1_rect = contretorpij1_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj1[3]<962 :
                                        absbateauxj1[3]=absbateauxj1[3]+41
                                        contretorpij1_rect = contretorpij1_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj1[3]>337 :
                                        ordbateauxj1[3]=ordbateauxj1[3]-41
                                        contretorpij1_rect = contretorpij1_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj1[3]<584 :
                                        ordbateauxj1[3]=ordbateauxj1[3]+41
                                        contretorpij1_rect = contretorpij1_rect.move(0,41)
                            if placement==5 :
                                if event.key == K_LEFT:
                                    if absbateauxj1[4]>593 :
                                        absbateauxj1[4]=absbateauxj1[4]-41
                                        torpilleurj1_rect = torpilleurj1_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj1[4]<962 :
                                        absbateauxj1[4]=absbateauxj1[4]+41
                                        torpilleurj1_rect = torpilleurj1_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj1[4]>337 :
                                        ordbateauxj1[4]=ordbateauxj1[4]-41
                                        torpilleurj1_rect = torpilleurj1_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj1[4]<625 :
                                        ordbateauxj1[4]=ordbateauxj1[4]+41
                                        torpilleurj1_rect = torpilleurj1_rect.move(0,41)
                        if event.key == K_ESCAPE:
                            Continuer=0
                    if event.type == MOUSEBUTTONUP and event.button == 1 :
                        clicutilise=0
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and clicutilise==0 :
                        if event.pos[0]>=824 and event.pos[0]<=1004 and event.pos[1]>=85 and event.pos[1]<=135 and Collisions==0 :
                            if placement==5 :
                                actuel = changementj2
                                placement=0
                                joueur = 0
                                j1pret = 1
                            if placement==4 :
                                placement=5
                                torpilleurj1_rect=torpilleurj1_rect.move(-156,115)
                            if placement==3 :
                                placement=4
                                contretorpij1_rect=contretorpij1_rect.move(13,69)
                            if placement==2 :
                                placement=3
                                sousmarinj1_rect=sousmarinj1_rect.move(-115,69)
                            if placement==1 :
                                placement=2
                                croiseurj1_rect=croiseurj1_rect.move(13,115)
                        if event.pos[0]>=824 and event.pos[0]<=1004 and event.pos[1]>=145 and event.pos[1]<=195 :
                            if Verticalj1[placement-1]==0 and clicutilise==0:
                                if placement==1 :
                                    porteavionj1_rect = porteavionVertical_rect
                                    if ordbateauxj1[0]>541 :
                                        ordbateauxj1[0]=541
                                    porteavionj1_rect = porteavionj1_rect.move(absbateauxj1[0],ordbateauxj1[0])
                                if placement==2 :
                                    croiseurj1_rect = croiseurVertical_rect
                                    if ordbateauxj1[1]>582 :
                                        ordbateauxj1[1]=582
                                    croiseurj1_rect = croiseurj1_rect.move(absbateauxj1[1],ordbateauxj1[1])
                                if placement==3 :
                                    sousmarinj1_rect = smctVertical_rect
                                    if ordbateauxj1[2]>623 :
                                        ordbateauxj1[2]=623
                                    sousmarinj1_rect = sousmarinj1_rect.move(absbateauxj1[2],ordbateauxj1[2])
                                if placement==4 :
                                    contretorpij1_rect = smctVertical_rect
                                    if ordbateauxj1[3]>623 :
                                        ordbateauxj1[3]=623
                                    contretorpij1_rect = contretorpij1_rect.move(absbateauxj1[3],ordbateauxj1[3])
                                if placement==5 :
                                    torpilleurj1_rect = torpilleurVertical_rect
                                    if ordbateauxj1[4]>664 :
                                        ordbateauxj1[4]=664
                                    torpilleurj1_rect = torpilleurj1_rect.move(absbateauxj1[4],ordbateauxj1[4])
                                Verticalj1[placement-1]=1
                                clicutilise=1
                            if Verticalj1[placement-1]==1 and clicutilise==0:
                                if placement==1 :
                                    porteavionj1_rect = porteavion_rect
                                    if absbateauxj1[0]>798 :
                                        absbateauxj1[0]=798
                                    porteavionj1_rect = porteavionj1_rect.move(absbateauxj1[0],ordbateauxj1[0])
                                if placement==2 :
                                    croiseurj1_rect = croiseur_rect
                                    if absbateauxj1[1]>839 :
                                        absbateauxj1[1]=839
                                    croiseurj1_rect = croiseurj1_rect.move(absbateauxj1[1],ordbateauxj1[1])
                                if placement==3 :
                                    sousmarinj1_rect = smct_rect
                                    if absbateauxj1[2]>880 :
                                        absbateauxj1[2]=880
                                    sousmarinj1_rect = sousmarinj1_rect.move(absbateauxj1[2],ordbateauxj1[2])
                                if placement==4 :
                                    contretorpij1_rect = smct_rect
                                    if absbateauxj1[3]>880 :
                                        absbateauxj1[3]=880
                                    contretorpij1_rect = contretorpij1_rect.move(absbateauxj1[3],ordbateauxj1[3])
                                if placement==5 :
                                    torpilleurj1_rect = torpilleur_rect
                                    if absbateauxj1[4]>921 :
                                        absbateauxj1[4]=921
                                    torpilleurj1_rect = torpilleurj1_rect.move(absbateauxj1[4],ordbateauxj1[4])
                                Verticalj1[placement-1]=0
                                clicutilise=1
                    if porteavionj1_rect.colliderect(croiseurj1_rect)==1 or porteavionj1_rect.colliderect(sousmarinj1_rect)==1 or porteavionj1_rect.colliderect(contretorpij1_rect)==1 or porteavionj1_rect.colliderect(torpilleurj1_rect)==1 or croiseurj1_rect.colliderect(sousmarinj1_rect)==1 or croiseurj1_rect.colliderect(contretorpij1_rect)==1 or croiseurj1_rect.colliderect(torpilleurj1_rect)==1 or sousmarinj1_rect.colliderect(contretorpij1_rect)==1 or sousmarinj1_rect.colliderect(torpilleurj1_rect)==1 or contretorpij1_rect.colliderect(torpilleurj1_rect)==1 :
                        Collisions=1
                    else :
                        Collisions=0
            if actuel==attaque :
                for event in pygame.event.get():
                    if event.type == QUIT:
                        Continuer=0
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            Continuer=0
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                        if event.pos[0]>=824 and event.pos[0]<=1004 and event.pos[1]>=85 and event.pos[1]<=135 and choisi==1 :
                            actuel = changementj2
                            choisi = 0
                            abscissetir=(((saveabstir-20)/51)*41)+593
                            ordonneetir=(((saveordtir-236)/51)*41)+336
                            tir_rect = tir_rect.move(abscissetir,ordonneetir)
                            if tir_rect.colliderect(porteavionj2_rect)==1 or tir_rect.colliderect(croiseurj2_rect)==1 or tir_rect.colliderect(sousmarinj2_rect)==1 or tir_rect.colliderect(contretorpij2_rect)==1 or tir_rect.colliderect(torpilleurj2_rect)==1 :
                                if Son==True :
                                    Explosion.play()
                                abstouchej1self.append(saveabstir)
                                ordtouchej1self.append(saveordtir)
                                abstouchej2ennemi.append(abscissetir)
                                ordtouchej2ennemi.append(ordonneetir)
                                if tir_rect.colliderect(porteavionj2_rect)==1 :
                                    PVj2[0]=PVj2[0]-1
                                if tir_rect.colliderect(croiseurj2_rect)==1 :
                                    PVj2[1]=PVj2[1]-1
                                if tir_rect.colliderect(sousmarinj2_rect)==1 :
                                    PVj2[2]=PVj2[2]-1
                                if tir_rect.colliderect(contretorpij2_rect)==1 :
                                    PVj2[3]=PVj2[3]-1
                                if tir_rect.colliderect(torpilleurj2_rect)==1 :
                                    PVj2[4]=PVj2[4]-1
                            else :
                                absmissj1self.append(saveabstir)
                                ordmissj1self.append(saveordtir)
                                absmissj2ennemi.append(abscissetir)
                                ordmissj2ennemi.append(ordonneetir)
                            tir_rect = tir_rect.move(-abscissetir,-ordonneetir)
                        if event.pos[0]>20 and event.pos[0]<531 and event.pos[1]>237 and event.pos[1]<747 :
                            choisi=0
                            dejatire=0
                            compteur=0
                            abscissetir=0
                            ordonneetir=0
                            saveabstir=event.pos[0]-20
                            saveordtir=event.pos[1]-236
                            while saveabstir-51>0 :
                                abscissetir=abscissetir+1
                                saveabstir=saveabstir-51
                            while saveordtir-51>0 :
                                ordonneetir=ordonneetir+1
                                saveordtir=saveordtir-51
                            saveabstir=(abscissetir*51)+20
                            saveordtir=(ordonneetir*51)+236
                            choixtir_rect=[saveabstir,saveordtir,51,51]
                            while compteur<len(absmissj1self) :
                                if saveordtir==absmissj1self[compteur] and saveordtir==ordmissj1self[compteur] :
                                    dejatire=dejatire+1
                                compteur=compteur+1
                            compteur=0
                            while compteur<len(abstouchej1self) :
                                if saveabstir==abstouchej1self[compteur] and saveordtir==ordtouchej1self[compteur] :
                                    dejatire=dejatire+1
                                compteur=compteur+1
                            if dejatire==0 :
                                choisi = 1
            if actuel==defense :
                for event in pygame.event.get():
                    if event.type == QUIT:
                        Continuer = 0
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            Continuer = 0
        if joueur==2 :
            if actuel==preparation and j2pret==0 :
                for event in pygame.event.get():
                    if event.type == QUIT:
                        Continuer=0
                    if event.type == KEYDOWN:
                        if Verticalj2[placement-1]==0 :
                            if placement==1 :
                                if event.key == K_LEFT:
                                    if absbateauxj2[0]>593 :
                                        absbateauxj2[0]=absbateauxj2[0]-41
                                        porteavionj2_rect = porteavionj2_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj2[0]<798 :
                                        absbateauxj2[0]=absbateauxj2[0]+41
                                        porteavionj2_rect = porteavionj2_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj2[0]>337 :
                                        ordbateauxj2[0]=ordbateauxj2[0]-41
                                        porteavionj2_rect = porteavionj2_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj2[0]<666 :
                                        ordbateauxj2[0]=ordbateauxj2[0]+41
                                        porteavionj2_rect = porteavionj2_rect.move(0,41)
                            if placement==2 :
                                if event.key == K_LEFT:
                                    if absbateauxj2[1]>593 :
                                        absbateauxj2[1]=absbateauxj2[1]-41
                                        croiseurj2_rect = croiseurj2_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj2[1]<839 :
                                        absbateauxj2[1]=absbateauxj2[1]+41
                                        croiseurj2_rect = croiseurj2_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj2[1]>337 :
                                        ordbateauxj2[1]=ordbateauxj2[1]-41
                                        croiseurj2_rect = croiseurj2_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj2[1]<666 :
                                        ordbateauxj2[1]=ordbateauxj2[1]+41
                                        croiseurj2_rect = croiseurj2_rect.move(0,41)
                            if placement==3 :
                                if event.key == K_LEFT:
                                    if absbateauxj2[2]>593 :
                                            absbateauxj2[2]=absbateauxj2[2]-41
                                            sousmarinj2_rect = sousmarinj2_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj2[2]<880 :
                                        absbateauxj2[2]=absbateauxj2[2]+41
                                        sousmarinj2_rect = sousmarinj2_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj2[2]>337 :
                                        ordbateauxj2[2]=ordbateauxj2[2]-41
                                        sousmarinj2_rect = sousmarinj2_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj2[2]<666 :
                                        ordbateauxj2[2]=ordbateauxj2[2]+41
                                        sousmarinj2_rect = sousmarinj2_rect.move(0,41)
                            if placement==4 :
                                if event.key == K_LEFT:
                                    if absbateauxj2[3]>593 :
                                        absbateauxj2[3]=absbateauxj2[3]-41
                                        contretorpij2_rect = contretorpij2_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj2[3]<880 :
                                        absbateauxj2[3]=absbateauxj2[3]+41
                                        contretorpij2_rect = contretorpij2_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj2[3]>337 :
                                        ordbateauxj2[3]=ordbateauxj2[3]-41
                                        contretorpij2_rect = contretorpij2_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj2[3]<666 :
                                        ordbateauxj2[3]=ordbateauxj2[3]+41
                                        contretorpij2_rect = contretorpij2_rect.move(0,41)
                            if placement==5 :
                                if event.key == K_LEFT:
                                    if absbateauxj2[4]>593 :
                                        absbateauxj2[4]=absbateauxj2[4]-41
                                        torpilleurj2_rect = torpilleurj2_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj2[4]<921 :
                                        absbateauxj2[4]=absbateauxj2[4]+41
                                        torpilleurj2_rect = torpilleurj2_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj2[4]>337 :
                                        ordbateauxj2[4]=ordbateauxj2[4]-41
                                        torpilleurj2_rect = torpilleurj2_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj2[4]<666 :
                                        ordbateauxj2[4]=ordbateauxj2[4]+41
                                        torpilleurj2_rect = torpilleurj2_rect.move(0,41)
                        if Verticalj2[placement-1]==1 :
                            if placement==1 :
                                if event.key == K_LEFT:
                                    if absbateauxj2[0]>593 :
                                        absbateauxj2[0]=absbateauxj2[0]-41
                                        porteavionj2_rect = porteavionj2_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj2[0]<962 :
                                        absbateauxj2[0]=absbateauxj2[0]+41
                                        porteavionj2_rect = porteavionj2_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj2[0]>337 :
                                        ordbateauxj2[0]=ordbateauxj2[0]-41
                                        porteavionj2_rect = porteavionj2_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj2[0]<502 :
                                        ordbateauxj2[0]=ordbateauxj2[0]+41
                                        porteavionj2_rect = porteavionj2_rect.move(0,41)
                            if placement==2 :
                                if event.key == K_LEFT:
                                    if absbateauxj2[1]>593 :
                                        absbateauxj2[1]=absbateauxj2[1]-41
                                        croiseurj2_rect = croiseurj2_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj2[1]<962 :
                                        absbateauxj2[1]=absbateauxj2[1]+41
                                        croiseurj2_rect = croiseurj2_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj2[1]>337 :
                                        ordbateauxj2[1]=ordbateauxj2[1]-41
                                        croiseurj2_rect = croiseurj2_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj2[1]<543 :
                                        ordbateauxj2[1]=ordbateauxj2[1]+41
                                        croiseurj2_rect = croiseurj2_rect.move(0,41)
                            if placement==3 :
                                if event.key == K_LEFT:
                                    if absbateauxj2[2]>593 :
                                            absbateauxj2[2]=absbateauxj2[2]-41
                                            sousmarinj2_rect = sousmarinj2_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj2[2]<962 :
                                        absbateauxj2[2]=absbateauxj2[2]+41
                                        sousmarinj2_rect = sousmarinj2_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj2[2]>337 :
                                        ordbateauxj2[2]=ordbateauxj2[2]-41
                                        sousmarinj2_rect = sousmarinj2_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj2[2]<584 :
                                        ordbateauxj2[2]=ordbateauxj2[2]+41
                                        sousmarinj2_rect = sousmarinj2_rect.move(0,41)
                            if placement==4 :
                                if event.key == K_LEFT:
                                    if absbateauxj2[3]>593 :
                                        absbateauxj2[3]=absbateauxj2[3]-41
                                        contretorpij2_rect = contretorpij2_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj2[3]<962 :
                                        absbateauxj2[3]=absbateauxj2[3]+41
                                        contretorpij2_rect = contretorpij2_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj2[3]>337 :
                                        ordbateauxj2[3]=ordbateauxj2[3]-41
                                        contretorpij2_rect = contretorpij2_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj2[3]<584 :
                                        ordbateauxj2[3]=ordbateauxj2[3]+41
                                        contretorpij2_rect = contretorpij2_rect.move(0,41)
                            if placement==5 :
                                if event.key == K_LEFT:
                                    if absbateauxj2[4]>593 :
                                        absbateauxj2[4]=absbateauxj2[4]-41
                                        torpilleurj2_rect = torpilleurj2_rect.move(-41,0)
                                if event.key == K_RIGHT:
                                    if absbateauxj2[4]<962 :
                                        absbateauxj2[4]=absbateauxj2[4]+41
                                        torpilleurj2_rect = torpilleurj2_rect.move(41,0)
                                if event.key == K_UP:
                                    if ordbateauxj2[4]>337 :
                                        ordbateauxj2[4]=ordbateauxj2[4]-41
                                        torpilleurj2_rect = torpilleurj2_rect.move(0,-41)
                                if event.key == K_DOWN:
                                    if ordbateauxj2[4]<625 :
                                        ordbateauxj2[4]=ordbateauxj2[4]+41
                                        torpilleurj2_rect = torpilleurj2_rect.move(0,41)
                        if event.key == K_ESCAPE:
                            Continuer=0
                    if event.type == MOUSEBUTTONUP and event.button == 1 :
                        clicutilise=0
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and clicutilise==0 :
                        if event.pos[0]>=824 and event.pos[0]<=1004 and event.pos[1]>=85 and event.pos[1]<=135 and Collisions==0 :
                            if placement==5 :
                                actuel = changementj1
                                placement=0
                                joueur = 0
                                j2pret = 1
                            if placement==4 :
                                placement=5
                                torpilleurj2_rect=torpilleurj2_rect.move(-156,115)
                            if placement==3 :
                                placement=4
                                contretorpij2_rect=contretorpij2_rect.move(13,69)
                            if placement==2 :
                                placement=3
                                sousmarinj2_rect=sousmarinj2_rect.move(-115,69)
                            if placement==1 :
                                placement=2
                                croiseurj2_rect=croiseurj2_rect.move(13,115)
                        if event.pos[0]>=824 and event.pos[0]<=1004 and event.pos[1]>=145 and event.pos[1]<=195 :
                            if Verticalj2[placement-1]==0 and clicutilise==0:
                                if placement==1 :
                                    porteavionj2_rect = porteavionVertical_rect
                                    if ordbateauxj2[0]>541 :
                                        ordbateauxj2[0]=541
                                    porteavionj2_rect = porteavionj2_rect.move(absbateauxj2[0],ordbateauxj2[0])
                                if placement==2 :
                                    croiseurj2_rect = croiseurVertical_rect
                                    if ordbateauxj2[1]>582 :
                                        ordbateauxj2[1]=582
                                    croiseurj2_rect = croiseurj2_rect.move(absbateauxj2[1],ordbateauxj2[1])
                                if placement==3 :
                                    sousmarinj2_rect = smctVertical_rect
                                    if ordbateauxj2[2]>623 :
                                        ordbateauxj2[2]=623
                                    sousmarinj2_rect = sousmarinj2_rect.move(absbateauxj2[2],ordbateauxj2[2])
                                if placement==4 :
                                    contretorpij2_rect = smctVertical_rect
                                    if ordbateauxj2[3]>623 :
                                        ordbateauxj2[3]=623
                                    contretorpij2_rect = contretorpij2_rect.move(absbateauxj2[3],ordbateauxj2[3])
                                if placement==5 :
                                    torpilleurj2_rect = torpilleurVertical_rect
                                    if ordbateauxj2[4]>664 :
                                        ordbateauxj2[4]=664
                                    torpilleurj2_rect = torpilleurj2_rect.move(absbateauxj2[4],ordbateauxj2[4])
                                Verticalj2[placement-1]=1
                                clicutilise=1
                            if Verticalj2[placement-1]==1 and clicutilise==0:
                                if placement==1 :
                                    porteavionj2_rect = porteavion_rect
                                    if absbateauxj2[0]>798 :
                                        absbateauxj2[0]=798
                                    porteavionj2_rect = porteavionj2_rect.move(absbateauxj2[0],ordbateauxj2[0])
                                if placement==2 :
                                    croiseurj2_rect = croiseur_rect
                                    if absbateauxj2[1]>839 :
                                        absbateauxj2[1]=839
                                    croiseurj2_rect = croiseurj2_rect.move(absbateauxj2[1],ordbateauxj2[1])
                                if placement==3 :
                                    sousmarinj2_rect = smct_rect
                                    if absbateauxj2[2]>880 :
                                        absbateauxj2[2]=880
                                    sousmarinj2_rect = sousmarinj2_rect.move(absbateauxj2[2],ordbateauxj2[2])
                                if placement==4 :
                                    contretorpij2_rect = smct_rect
                                    if absbateauxj2[3]>880 :
                                        absbateauxj2[3]=880
                                    contretorpij2_rect = contretorpij2_rect.move(absbateauxj2[3],ordbateauxj2[3])
                                if placement==5 :
                                    torpilleurj2_rect = torpilleur_rect
                                    if absbateauxj2[4]>921 :
                                        absbateauxj2[4]=921
                                    torpilleurj2_rect = torpilleurj2_rect.move(absbateauxj2[4],ordbateauxj2[4])
                                Verticalj2[placement-1]=0
                                clicutilise=1
                    if porteavionj2_rect.colliderect(croiseurj2_rect)==1 or porteavionj2_rect.colliderect(sousmarinj2_rect)==1 or porteavionj2_rect.colliderect(contretorpij2_rect)==1 or porteavionj2_rect.colliderect(torpilleurj2_rect)==1 or croiseurj2_rect.colliderect(sousmarinj2_rect)==1 or croiseurj2_rect.colliderect(contretorpij2_rect)==1 or croiseurj2_rect.colliderect(torpilleurj2_rect)==1 or sousmarinj2_rect.colliderect(contretorpij2_rect)==1 or sousmarinj2_rect.colliderect(torpilleurj2_rect)==1 or contretorpij2_rect.colliderect(torpilleurj2_rect)==1 :
                        Collisions=1
                    else :
                        Collisions=0
            if actuel==attaque :
                for event in pygame.event.get():
                    if event.type == QUIT:
                        Continuer=0
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE :
                            Continuer=0
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                        if event.pos[0]>=824 and event.pos[0]<=1004 and event.pos[1]>=85 and event.pos[1]<=135 and choisi==1 :
                            actuel = changementj1
                            choisi = 0
                            abscissetir=(((saveabstir-20)/51)*41)+593
                            ordonneetir=(((saveordtir-236)/51)*41)+336
                            tir_rect = tir_rect.move(abscissetir,ordonneetir)
                            if tir_rect.colliderect(porteavionj1_rect)==1 or tir_rect.colliderect(croiseurj1_rect)==1 or tir_rect.colliderect(sousmarinj1_rect)==1 or tir_rect.colliderect(contretorpij1_rect)==1 or tir_rect.colliderect(torpilleurj1_rect)==1 :
                                if Son==True :
                                    Explosion.play()
                                abstouchej2self.append(saveabstir)
                                ordtouchej2self.append(saveordtir)
                                abstouchej1ennemi.append(abscissetir)
                                ordtouchej1ennemi.append(ordonneetir)
                                if tir_rect.colliderect(porteavionj1_rect)==1 :
                                    PVj1[0]=PVj1[0]-1
                                if tir_rect.colliderect(croiseurj1_rect)==1 :
                                    PVj1[1]=PVj1[1]-1
                                if tir_rect.colliderect(sousmarinj1_rect)==1 :
                                    PVj1[2]=PVj1[2]-1
                                if tir_rect.colliderect(contretorpij1_rect)==1 :
                                    PVj1[3]=PVj1[3]-1
                                if tir_rect.colliderect(torpilleurj1_rect)==1 :
                                    PVj1[4]=PVj1[4]-1
                            else :
                                absmissj2self.append(saveabstir)
                                ordmissj2self.append(saveordtir)
                                absmissj1ennemi.append(abscissetir)
                                ordmissj1ennemi.append(ordonneetir)
                            tir_rect = tir_rect.move(-abscissetir,-ordonneetir)
                        if event.pos[0]>20 and event.pos[0]<531 and event.pos[1]>237 and event.pos[1]<747 :
                            choisi=0
                            dejatire=0
                            compteur=0
                            abscissetir=0
                            ordonneetir=0
                            saveabstir=event.pos[0]-20
                            saveordtir=event.pos[1]-236
                            while saveabstir-51>0 :
                                abscissetir=abscissetir+1
                                saveabstir=saveabstir-51
                            while saveordtir-51>0 :
                                ordonneetir=ordonneetir+1
                                saveordtir=saveordtir-51
                            saveabstir=(abscissetir*51)+20
                            saveordtir=(ordonneetir*51)+236
                            choixtir_rect=[saveabstir,saveordtir,51,51]
                            while compteur<len(absmissj2self) :
                                if saveordtir==absmissj2self[compteur] and saveordtir==ordmissj2self[compteur] :
                                    dejatire=dejatire+1
                                compteur=compteur+1
                            compteur=0
                            while compteur<len(abstouchej2self) :
                                if saveabstir==abstouchej2self[compteur] and saveordtir==ordtouchej2self[compteur] :
                                    dejatire=dejatire+1
                                compteur=compteur+1
                            if dejatire==0 :
                                choisi = 1
            if actuel==defense :
                for event in pygame.event.get():
                    if event.type == QUIT:
                        Continuer = 0
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            Continuer = 0
        if actuel==changementj2 :
            for event in pygame.event.get():
                if event.type == QUIT:
                    Continuer = 0
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        Continuer = 0
                if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                    joueur = 2
                    if j2pret==0 :
                        actuel = preparation
                        placement=1
                    if j2pret==1 :
                        actuel = attaque
        if actuel==changementj1 :
            for event in pygame.event.get():
                if event.type == QUIT:
                    Continuer = 0
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        Continuer = 0
                if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                    joueur = 1
                    if j1pret==0 :
                        actuel = preparation
                    if j1pret==1 :
                        actuel = attaque
        if actuel!=changementj1 and actuel!=changementj2 :
            ecran.blit(Partie,(0,0))
            ecran.blit(actuel,(754,0))
            if actuel==preparation :
                ecran.blit(bateauxaplacer,(580,175))
                ecran.blit(termine,(824,85))
                ecran.blit(retourner,(824,145))
                if placement==1 :
                    ecran.blit(PlacementPA,(535,0))
                if placement==2 :
                    ecran.blit(PlacementC,(535,0))
                if placement==3 :
                    ecran.blit(PlacementSM,(535,0))
                if placement==4 :
                    ecran.blit(PlacementCT,(535,0))
                if placement==5 :
                    ecran.blit(PlacementT,(535,0))
            if actuel==attaque :
                ecran.blit(tirer,(824,85))
            ecran.blit(grille,(20,236))
            ecran.blit(grillesmall,(593,336))
            if choisi==1 :
                ecran.blit(choixtir,choixtir_rect)
            if joueur==1 :
                if PVj1[0]>0 :
                    if Verticalj1[0]==1 :
                        ecran.blit(porteavionVertical,porteavionj1_rect)
                    else :
                        ecran.blit(porteavion,porteavionj1_rect)
                if PVj1[1]>0 :
                    if Verticalj1[1]==1 :
                        ecran.blit(croiseurVertical,croiseurj1_rect)
                    else :
                        ecran.blit(croiseur,croiseurj1_rect)
                if PVj1[2]>0 :
                    if Verticalj1[2]==1 :
                        ecran.blit(smctVertical,sousmarinj1_rect)
                    else :
                        ecran.blit(smct,sousmarinj1_rect)
                if PVj1[3]>0 :
                    if Verticalj1[3]==1 :
                        ecran.blit(smctVertical,contretorpij1_rect)
                    else :
                        ecran.blit(smct,contretorpij1_rect)
                if PVj1[4]>0 :
                    if Verticalj1[4]==1 :
                        ecran.blit(torpilleurVertical,torpilleurj1_rect)
                    else :
                        ecran.blit(torpilleur,torpilleurj1_rect)
                ecran.blit(joueur1,(0,0))
                compteur=0
                while compteur<len(absmissj1self) :
                    ecran.blit(miss,(absmissj1self[compteur],ordmissj1self[compteur]))
                    compteur=compteur+1
                compteur=0
                while compteur<len(abstouchej1self) :
                    ecran.blit(touche,(abstouchej1self[compteur],ordtouchej1self[compteur]))
                    compteur=compteur+1
                compteur=0
                while compteur<len(absmissj1ennemi) :
                    ecran.blit(misssmall,(absmissj1ennemi[compteur],ordmissj1ennemi[compteur]))
                    compteur=compteur+1
                compteur=0
                while compteur<len(abstouchej1ennemi) :
                    ecran.blit(touchesmall,(abstouchej1ennemi[compteur],ordtouchej1ennemi[compteur]))
                    compteur=compteur+1
            if joueur==2 :
                if PVj2[0]>0 :
                    if Verticalj2[0]==1 :
                        ecran.blit(porteavionVertical,porteavionj2_rect)
                    else :
                        ecran.blit(porteavion,porteavionj2_rect)
                if PVj2[1]>0 :
                    if Verticalj2[1]==1 :
                        ecran.blit(croiseurVertical,croiseurj2_rect)
                    else :
                        ecran.blit(croiseur,croiseurj2_rect)
                if PVj2[2]>0 :
                    if Verticalj2[2]==1 :
                        ecran.blit(smctVertical,sousmarinj2_rect)
                    else :
                        ecran.blit(smct,sousmarinj2_rect)
                if PVj2[3]>0 :
                    if Verticalj2[3]==1 :
                        ecran.blit(smctVertical,contretorpij2_rect)
                    else :
                        ecran.blit(smct,contretorpij2_rect)
                if PVj2[4]>0 :
                    if Verticalj2[4]==1 :
                        ecran.blit(torpilleurVertical,torpilleurj2_rect)
                    else :
                        ecran.blit(torpilleur,torpilleurj2_rect)
                ecran.blit(joueur2,(0,0))
                compteur=0
                while compteur<len(absmissj2self) :
                    ecran.blit(miss,(absmissj2self[compteur],ordmissj2self[compteur]))
                    compteur=compteur+1
                compteur=0
                while compteur<len(abstouchej2self) :
                    ecran.blit(touche,(abstouchej2self[compteur],ordtouchej2self[compteur]))
                    compteur=compteur+1
                compteur=0
                while compteur<len(absmissj2ennemi) :
                    ecran.blit(misssmall,(absmissj2ennemi[compteur],ordmissj2ennemi[compteur]))
                    compteur=compteur+1
                compteur=0
                while compteur<len(abstouchej2ennemi) :
                    ecran.blit(touchesmall,(abstouchej2ennemi[compteur],ordtouchej2ennemi[compteur]))
                    compteur=compteur+1
            if joueur==1 :
                if PVj1[0]==0 :
                    if Verticalj1[0]==1 :
                        ecran.blit(pavdeadsmall,porteavionj1_rect)
                    else :
                        ecran.blit(padeadsmall,porteavionj1_rect)
                if PVj1[1]==0 :
                    if Verticalj1[1]==1 :
                        ecran.blit(cvdeadsmall,croiseurj1_rect)
                    else :
                        ecran.blit(cdeadsmall,croiseurj1_rect)
                if PVj1[2]==0 :
                    if Verticalj1[2]==1 :
                        ecran.blit(smctvdeadsmall,sousmarinj1_rect)
                    else :
                        ecran.blit(smctdeadsmall,sousmarinj1_rect)
                if PVj1[3]==0 :
                    if Verticalj1[3]==1 :
                        ecran.blit(smctvdeadsmall,contretorpij1_rect)
                    else :
                        ecran.blit(smctdeadsmall,contretorpij1_rect)
                if PVj1[4]==0 :
                    if Verticalj1[4]==1 :
                        ecran.blit(tvdeadsmall,torpilleurj1_rect)
                    else :
                        ecran.blit(tdeadsmall,torpilleurj1_rect)
                if PVj2[0]==0 :
                    if Verticalj2[0]==1 :
                        ecran.blit(pavdead,(((((porteavionj2_rect.left)-593)/41)*51)+20,((((porteavionj2_rect.top)-336)/41)*51)+236))
                    else :
                        ecran.blit(padead,(((((porteavionj2_rect.left)-593)/41)*51)+20,((((porteavionj2_rect.top)-336)/41)*51)+236))
                if PVj2[1]==0 :
                    if Verticalj2[1]==1 :
                        ecran.blit(cvdead,(((((croiseurj2_rect.left)-593)/41)*51)+20,((((croiseurj2_rect.top)-336)/41)*51)+236))
                    else :
                        ecran.blit(cdead,(((((croiseurj2_rect.left)-593)/41)*51)+20,((((croiseurj2_rect.top)-336)/41)*51)+236))
                if PVj2[2]==0 :
                    if Verticalj2[2]==1 :
                        ecran.blit(smctvdead,(((((sousmarinj2_rect.left)-593)/41)*51)+20,((((sousmarinj2_rect.top)-336)/41)*51)+236))
                    else :
                        ecran.blit(smctdead,(((((sousmarinj2_rect.left)-593)/41)*51)+20,((((sousmarinj2_rect.top)-336)/41)*51)+236))
                if PVj2[3]==0 :
                    if Verticalj2[3]==1 :
                        ecran.blit(smctvdead,(((((contretorpij2_rect.left)-593)/41)*51)+20,((((contretorpij2_rect.top)-336)/41)*51)+236))
                    else :
                        ecran.blit(smctdead,(((((contretorpij2_rect.left)-593)/41)*51)+20,((((contretorpij2_rect.top)-336)/41)*51)+236))
                if PVj2[4]==0 :
                    if Verticalj2[4]==1 :
                        ecran.blit(tvdead,(((((torpilleurj2_rect.left)-593)/41)*51)+20,((((torpilleurj2_rect.top)-336)/41)*51)+236))
                    else :
                        ecran.blit(tdead,(((((torpilleurj2_rect.left)-593)/41)*51)+20,((((torpilleurj2_rect.top)-336)/41)*51)+236))
            if joueur==2 :
                if PVj2[0]==0 :
                    if Verticalj2[0]==1 :
                        ecran.blit(pavdeadsmall,porteavionj2_rect)
                    else :
                        ecran.blit(padeadsmall,porteavionj2_rect)
                if PVj2[1]==0 :
                    if Verticalj2[1]==1 :
                        ecran.blit(cvdeadsmall,croiseurj2_rect)
                    else :
                        ecran.blit(cdeadsmall,croiseurj2_rect)
                if PVj2[2]==0 :
                    if Verticalj2[2]==1 :
                        ecran.blit(smctvdeadsmall,sousmarinj2_rect)
                    else :
                        ecran.blit(smctdeadsmall,sousmarinj2_rect)
                if PVj2[3]==0 :
                    if Verticalj2[3]==1 :
                        ecran.blit(smctvdeadsmall,contretorpij2_rect)
                    else :
                        ecran.blit(smctdeadsmall,contretorpij2_rect)
                if PVj2[4]==0 :
                    if Verticalj2[4]==1 :
                        ecran.blit(tvdeadsmall,torpilleurj2_rect)
                    else :
                        ecran.blit(tdeadsmall,torpilleurj2_rect)
                if PVj1[0]==0 :
                    if Verticalj1[0]==1 :
                        ecran.blit(pavdead,(((((porteavionj1_rect.left)-593)/41)*51)+20,((((porteavionj1_rect.top)-336)/41)*51)+236))
                    else :
                        ecran.blit(padead,(((((porteavionj1_rect.left)-593)/41)*51)+20,((((porteavionj1_rect.top)-336)/41)*51)+236))
                if PVj1[1]==0 :
                    if Verticalj1[1]==1 :
                        ecran.blit(cvdead,(((((croiseurj1_rect.left)-593)/41)*51)+20,((((croiseurj1_rect.top)-336)/41)*51)+236))
                    else :
                        ecran.blit(cdead,(((((croiseurj1_rect.left)-593)/41)*51)+20,((((croiseurj1_rect.top)-336)/41)*51)+236))
                if PVj1[2]==0 :
                    if Verticalj1[2]==1 :
                        ecran.blit(smctvdead,(((((sousmarinj1_rect.left)-593)/41)*51)+20,((((sousmarinj1_rect.top)-336)/41)*51)+236))
                    else :
                        ecran.blit(smctdead,(((((sousmarinj1_rect.left)-593)/41)*51)+20,((((sousmarinj1_rect.top)-336)/41)*51)+236))
                if PVj1[3]==0 :
                    if Verticalj1[3]==1 :
                        ecran.blit(smctvdead,(((((contretorpij1_rect.left)-593)/41)*51)+20,((((contretorpij1_rect.top)-336)/41)*51)+236))
                    else :
                        ecran.blit(smctdead,(((((contretorpij1_rect.left)-593)/41)*51)+20,((((contretorpij1_rect.top)-336)/41)*51)+236))
                if PVj1[4]==0 :
                    if Verticalj1[4]==1 :
                        ecran.blit(tvdead,(((((torpilleurj1_rect.left)-593)/41)*51)+20,((((torpilleurj1_rect.top)-336)/41)*51)+236))
                    else :
                        ecran.blit(tdead,(((((torpilleurj1_rect.left)-593)/41)*51)+20,((((torpilleurj1_rect.top)-336)/41)*51)+236))
        if Collisions==1 :
            ecran.blit(Collision,(535,50))
        if actuel==changementj1 :
            ecran.blit(changementj1,(0,0))
        if actuel==changementj2 :
            ecran.blit(changementj2,(0,0))
        pygame.display.flip() #Rafraîchissement de la fenêtre

if PVj1[0]+PVj1[1]+PVj1[2]+PVj1[3]+PVj1[4]==0 or PVj2[0]+PVj2[1]+PVj2[2]+PVj2[3]+PVj2[4]==0 :
    if PVj1[0]+PVj1[1]+PVj1[2]+PVj1[3]+PVj1[4]>0 :
        print("Joueur 1 Gagne !")
    if PVj2[0]+PVj2[1]+PVj2[2]+PVj2[3]+PVj2[4]>0 :
        print("joueur 2 Gagne !")

#Fermeture de la fenêtre pygame
pygame.quit()
if PVj1[0]+PVj1[1]+PVj1[2]+PVj1[3]+PVj1[4]==0 or PVj2[0]+PVj2[1]+PVj2[2]+PVj2[3]+PVj2[4]==0 :
    if PVj1[0]+PVj1[1]+PVj1[2]+PVj1[3]+PVj1[4]>0 :
        print("Joueur 1 Gagne !")
    if PVj2[0]+PVj2[1]+PVj2[2]+PVj2[3]+PVj2[4]>0 :
        print("joueur 2 Gagne !")
else :
    print("Pas de Gagnant !")