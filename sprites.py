import pygame,random


white = (255,255,255)
black = (0,0,0)

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()# pocisionar sprite

    def update(self):
        self.rect.y += 1
        if self.rect.y > 600:
            self.rect.y = -10
            self.rect.x = random.randrange(900)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()# pocisionar sprite

    def update(self) :
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = mouse_pos[1]


pygame.init()

screen = pygame.display.set_mode([900,600])
clock = pygame.time.Clock()
done = False
score =0

meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
pygame.mouse.set_visible(0)
score = 0

# dibujando meteoros
for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(900)
    meteor.rect.y = random.randrange(600)

    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

player = Player()
all_sprite_list.add(player)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         done = True

    all_sprite_list.update()
    # colisiones
    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True )
    # aumentar el score
    for meteor in meteor_hit_list:
        score += 1
        print(score)


    screen.fill(white)

    all_sprite_list.draw(screen)

    clock.tick(60)
    pygame.display.flip()
pygame.quit()
