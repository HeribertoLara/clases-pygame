import pygame, random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()  # pocisionar sprite

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = 510

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(BLACK)# le quita el fondo al png
        self.rect = self.image.get_rect()  # pocisionar sprite


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert()
        self.image.set_colorkey(BLACK)# le quita el fondo al png
        self.rect = self.image.get_rect()  # pocisionar sprite

    def update(self):
        self.rect.y -= 5 # tenemos que decrecer el eje Y
                        # entre mas alto sea el vallor mas rapido va a ir el laser

BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
screen = pygame.display.set_mode([900,600])
clock = pygame.time.Clock()
done = False
score = 0
# creacion de lista de player
all_sprite_list = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
player = Player()
all_sprite_list.add(player)

#crecion de lista de laser



# creacion de los meteoros
for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(880)# delimitando donde apareceran
    meteor.rect.y = random.randrange(450)

    meteor_list.add(meteor)
    all_sprite_list.add(meteor)# agregando  a la lista de meteoros

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            laser = Laser()
            laser.rect.x = player.rect.x +45
            laser.rect.y = player.rect.y -20
            all_sprite_list.add(laser)
            laser_list.add(laser)

    all_sprite_list.update()# debeir arria
    for laser in laser_list:
        meteor_hit_list = pygame.sprite.spritecollide(laser,meteor_list, True)
        for meteor in meteor_hit_list:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)
            score +=1
            print(score)

        if laser.rect.y < 10:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)

    screen.fill(WHITE)
    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()