import pygame
import random
import time

l10 = 0
l11 = False
time1=time.time()+10000000
pygame.init()
pygame.font.init()
propusk = 0
sbito = 0
heals = 3
f1 = pygame.font.SysFont('Arial', 36)
text1 = f1.render('пропущенно '+str(propusk), True,(180, 0, 0))
text5 = f1.render('жизней '+str(heals), True,(180, 0, 0))
f1 = pygame.font.SysFont('Arial', 36)
text2 = f1.render('сбито '+str(sbito), True,(180, 0, 0))
f2 = pygame.font.SysFont('Arial', 100)
text3 = f2.render('YOU WIN', True,(180, 0, 0))
text4 = f2.render('LOSE', True,(180, 0, 0))
# pygame.mixer.init()
WW =700
WH = 500
sc = pygame.display.set_mode((WW, WH))
pygame.display.set_caption('galaxy')
clock = pygame.time.Clock()
# объекты
# sc.fill(color)
# mixer.music.load('jungles.ogg')
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (70, 70))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        sc.blit(self.image, (self.rect.x, self.rect.y))
        




class Player(GameSprite):
    def update(self):

        keyp = pygame.key.get_pressed()
        if keyp[pygame.K_LEFT] and self.rect.x >= 5:
            self.rect.x -= 5
        if keyp[pygame.K_RIGHT] and self.rect.x <= 630:
            self.rect.x += 5
    def fire(self):
        self.sp_x_center = self.rect.x
        self.sp_top = self.rect.top
        global l10
        n8 = bullet("bullet.png",self.sp_x_center,self.sp_top,2)        
        bullets.add(n8)
            
        l10 +=1



            

class ememy(GameSprite):
    
    
    def update(self):

            self.rect.y+= random.randint(1,3)
            if self.rect.y >= 500:
                self.rect.y = 0
                self.rect.x = random.randint(0,700)
                global propusk
                propusk+=1

class bullet(GameSprite):
    def update(self):

        self.rect.y -= 3
        if self.rect.y <= 10:
            self.kill()
            
monsters = pygame.sprite.Group()
meteoriteos = pygame.sprite.Group()
back = pygame.transform.scale(pygame.image.load('galaxy.jpg'), (700, 500))
kvadratik1 = pygame.transform.scale(pygame.image.load('rocket.png'), (70, 70))
sokrovishe = pygame.transform.scale(pygame.image.load('bullet.png'), (80, 80))
run = True
n2 = Player("rocket.png",2,390,490)

n3 = ememy("ufo.png",random.randint(5,500),0,0)
n4 = ememy("ufo.png",random.randint(5,500),0,0)
n5 = ememy("ufo.png",random.randint(5,500),0,0)
n6 = ememy("ufo.png",random.randint(5,500),0,0)
n7 = ememy("ufo.png",random.randint(5,500),0,0)
n8 = ememy("asteroid.png",random.randint(5,500),0,0)
n9 = ememy("asteroid.png",random.randint(5,500),0,0)
n10 = ememy("asteroid.png",random.randint(5,500),0,0)
bullets = pygame.sprite.Group()


monsters.add(n3)
monsters.add(n4)
monsters.add(n5)
monsters.add(n6)
monsters.add(n7)
meteoriteos.add(n8)
meteoriteos.add(n9)
meteoriteos.add(n10)
run2= True
while run:
    if run2:
        text1 = f1.render('пропущенно '+str(propusk), True,(180, 0, 0))
        text2 = f1.render('сбито '+str(sbito), True,(180, 0, 0))
        text5 = f1.render('жизней '+str(heals), True,(180, 0, 0))
        sc.blit(back,(0,0))
        n2.update()
        n2.reset()
        monsters.update()
        monsters.draw(sc)
        bullets.update()
        bullets.draw(sc)
        meteoriteos.update()
        meteoriteos.draw(sc)
        sc.blit(text1,(20,20))
        sc.blit(text2,(20,50))
        sc.blit(text5,(20,80))
    if propusk == 100:
        sc.blit(text4,(180,180))
        run2=False
    if sbito == 40:
        sc.blit(text3,(180,180))
        run2=False
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                if l10 <= 10 and l11 ==False:
                    n2.fire()
                if l10 >= 10 and l11== False :
                    time1 = time.time()
                    l11 = True
                time2 = time.time()
                print(time2-time1)   
                print(l10)
                if time2 - time1 > 4.0 and l11 == True:
                    l10 = 0
                    print(12131)
                    l11 = False
    if pygame.sprite.groupcollide(monsters,bullets,True,True):
        sbito+=1
    
        n3 = ememy("ufo.png",random.randint(5,500),0,0)
        monsters.add(n3)
    if pygame.sprite.spritecollide(n2,monsters,True):
        heals-=1
        print(heals)
        n3 = ememy("ufo.png",random.randint(5,500),0,0)
        monsters.add(n3)
        if heals <=0 or heals == 0:
            sc.blit(text4,(180,180))
            run2=False
        
    if pygame.sprite.collide_rect(n2,n8) or pygame.sprite.collide_rect(n2,n9 ) or pygame.sprite.collide_rect(n2,n10 ):
        heals-=1
        print(heals)
        
        if heals <=0 or heals == 0:
            sc.blit(text4,(180,180))
            run2=False

    pygame.display.update()