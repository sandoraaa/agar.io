import random

import pygame

pygame.init()

width = 600
height = 500

size_window = (width, height)
window = pygame.display.set_mode(size_window)
pygame.display.set_caption('Game ')
game = 'run'

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.size = 25
        self.image_or = pygame.image.load("skin.png")
        self.image = pygame.transform.scale(self.image_or, (self.size, self.size))
        self.rect = self.image.get_rect(center=pos)

    def update(self, pos):
        global game
        self.rect.update(self.rect.left, self.rect.top, self.size, self.size)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 10
        if keys[pygame.K_RIGHT]:
            self.rect.x += 10
        if keys[pygame.K_UP]:
            self.rect.y -= 10
        if keys[pygame.K_DOWN]:
            self.rect.y += 10
        self.image = pygame.transform.scale(self.image_or, (self.size, self.size))
        window.blit(self.image, pos)
        if self.size >= 200:
            game = 'win'
            print(game)


class Bubble (pygame.sprite.Sprite):
    def __init__(self,pos, group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.image = pygame.Surface((10, 10))
        self.color = random.choice(["CadetBlue", "BlueViolet", "DarkKhaki"])
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center = pos)
    def update(self, pos):
        pygame.draw.circle(window,self.color, pos, 7)
        if pygame.sprite.spritecollide(self, player_group, False):
            self.kill()
            player.size += 1
        if pygame.sprite.spritecollide(self, enemy_group, False):
            self.kill()
            enemy.size += 2

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.size = 30
        self.dx = random.randint(-10, 10)
        self.dy = random.randint(-10, 10)
        self.image_or = pygame.image.load("skin1.png")
        self.image = pygame.transform.scale(self.image_or, (self.size, self.size))
        self.rect = self.image.get_rect(center=pos)

    def update(self,pos):
        global game
        self.rect.x += self.dx
        self.rect.y += self.dy
        window.blit(self.image, pos)

        if pygame.sprite.spritecollide(self, player_group, False):
            if self.size > player.size:
                print('game over!')
                game = 'lose'
            else:
                player.size += 5
                self.kill()



class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        #зчитуємо розміри екрану та визначаємо координати центра
        self.display = pygame.display.get_surface()
        self.x = 0
        self.y = 0
        self.width_2 = self.display.get_size()[0] // 2
        self.height_2 = self.display.get_size()[1] // 2

    def center_camera(self, player):
        #встановлюємо координати камери на головного героя
        self.x = player.rect.centerx - self.width_2
        self.y = player.rect.centery - self.height_2

    def draw_sprite(self, spritik):
        self.center_camera(spritik)
        # показуємо усі справйти з групи у нових координатах
        for sprite in self.sprites():
            pos_x = sprite.rect.x - self.x
            pos_y = sprite.rect.y - self.y
            sprite.update((pos_x, pos_y))

camera = CameraGroup()

player_group = pygame.sprite.Group()
player = Player((width//2, height//2), camera)
player_group.add (player)
g=2000

bubble_group = pygame.sprite.Group()
for i in range(1000):
    bubble = Bubble((random.randint(-g, g), random.randint(-g, g)), camera)
    bubble_group.add (bubble)

enemy_group = pygame.sprite.Group()
for i in range(200):
    enemy = Enemy((random.randint(-g, g), random.randint(-g, g)), camera)
    enemy_group.add (enemy)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill("black")
    '''bubble_group.update()
    bubble_group.draw(window)
    player_group.update()
    player_group.draw(window)'''
    if game == 'run':
        camera.draw_sprite(player)
    else :
        font = pygame.font.SysFont('mvboli', 100)

        image_game = font.render(game, True, pygame.Color('white'))
        window.blit(image_game, (200 ,150))

    pygame.display.update()
    pygame.time.delay(50)

pygame.quit()