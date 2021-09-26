import os
import random
import pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_0,
    QUIT,
)

# Screen size
screen_width = 800
screen_height = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load(os.path.join('assets', 'img', 'jet1.png')).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
            move_left_sound.play()
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            move_right_sound.play()

        # Player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(os.path.join('assets', 'img', 'ufo1.png')).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (random.randint(screen_width + 20, screen_width + 100), 
                        random.randint(0, screen_height),
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load(os.path.join('assets', 'img', 'cloud.png')).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (random.randint(screen_width + 20, screen_width + 100), random.randint(0, screen_height),
            )
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

# Initialize pygame
pygame.init()

# Screen object
screen = pygame.display.set_mode((screen_width, screen_height))

# Enemy
addenemy = pygame.USEREVENT + 1
pygame.time.set_timer(addenemy, 250)
addcloud = pygame.USEREVENT + 2
pygame.time.set_timer(addcloud, 1000)

# Sound effect
pygame.mixer.init()

#  Frame rate
clock = pygame.time.Clock()

# initialize player
player = Player()
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Sound effect
pygame.mixer.music.load(os.path.join('assets', 'audio', 'ursus.mp3'))
pygame.mixer.music.play(loops = -1)

move_up_sound = pygame.mixer.Sound(os.path.join('assets', 'audio', 'dec.mp3'))
move_down_sound = pygame.mixer.Sound(os.path.join('assets', 'audio', 'dec.mp3'))
collision_sound = pygame.mixer.Sound(os.path.join('assets', 'audio', 'stop.flac'))
move_left_sound = pygame.mixer.Sound(os.path.join('assets', 'audio', 'rec.mp3'))
move_right_sound = pygame.mixer.Sound(os.path.join('assets', 'audio', 'rec.mp3'))

# Main loop running
running = True

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        
        elif event.type == QUIT:
            running = False

        elif event.type == addenemy:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == addcloud:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # Getting all keys
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    clouds.update()

    # Screen color black
    screen.fill((135, 206, 250))

    # sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Enemy collied with player
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        move_up_sound.stop()
        move_down_sound.stop()
        move_left_sound.stop()
        move_right_sound.stop()
        collision_sound.play()
        running = False

    # Player on screen
    screen.blit(player.surf, player.rect)

    # Update the display
    pygame.display.flip()

    # Maintain fram rate
    clock.tick(30)

# Stop sound
pygame.mixer.music.stop()
pygame.mixer.quit()

