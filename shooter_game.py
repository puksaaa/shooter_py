#Создай собственный Шутер!
from random import randint
from pygame import *

'''
mixer.init()
mixer.music.load('gul.ogg')
mixer.music.play()'''


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def fire(self):
        bullet = Bullet('poop.png', self.rect.centerx, self.rect.top, 20, 30, -15)
        bullets.add(bullet)


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= 5
    
        if keys_pressed[K_RIGHT] and self.rect.x < 625:
            self.rect.x += 5


class Enemy(GameSprite):
    def update(self):
        self.rect.y += randint(1,3)
        global lost
        
        if self.rect.y > 500:
            self.rect.x = randint(80, 520)
            self.rect.y = 0
            lost = lost + 1

lost = 0 #счет пропущеных
score = 0 #счет сбитых


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()





window = display.set_mode((800, 500))
display.set_caption("шутер")










#спрайты
background = transform.scale(image.load("fon.jpg"), (800, 500))
hero = Player("kira.png", 400, 420, 50, 80, 15)



#группы
monsters = sprite.Group()
for i in range(1,6):
    monster = Enemy('nasta.png', randint(80, 520), -40, 60, 40, randint(1,5))
    monsters.add(monster)

bullets = sprite.Group()




#шрифт
font.init()
font1 =  font.SysFont('impact', 36)
font2 =  font.SysFont('impact', 80)




clock = time.Clock()



finish = False
game = True
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()
    
    if finish != True:

        window.blit(background, (0,0))

        #текст
        text = font1.render('счет:' + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font1.render('пропущено:' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        #отрисовка
        hero.reset()
        monsters.draw(window)
        bullets.draw(window)

        bullets.update()
        hero.update()
        monsters.update()
        
        #удаление
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy('nasta.png', randint(80, 520), -40, 60, 40, randint(1,5))
            monsters.add(monster)


        if sprite.spritecollide(hero, monsters, False) or lost > 3:
            lose = font2.render('ti lox', True, (255, 0, 0))
            window.blit(lose, (300, 200))
            finish = True

        if score >= 10:
            win = font2.render('YOU WIN', True, (255, 215, 0))
            window.blit(win, (300, 200))
            finish = True


    clock.tick(60)

    display.update()
