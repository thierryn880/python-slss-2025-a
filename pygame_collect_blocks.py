# collect blocks
# Author: ThierryNarcisse
# Date: 07/01/26

import random

import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, colour: pygame.Color, width: int, height: int):
        """a block of any colour"""

        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(colour)

        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 100


class Mario(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/mario-snes.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos

class Enemy(pygame.sprite.Sprite):


def game():
    pygame.init()

    # COLOURS - (R, G, B)
    # CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("collect blocks")

    # Variables
    done = False
    clock = pygame.time.Clock()
    all_sprites_group = pygame.sprite.Group()
    block_sprite_group = pygame.sprite.Group()
    for _ in range(100):
        block_one = Block(BLUE, 20, 10)

        block.rect.centerx = random.randrange(0, WIDTH)
        block.rect.centery = random.randrange(0, HEIGHT)

        all_sprites_group.add(block)
        block_sprite_group.add(block)
        player = Mario()
        player.rect.center = (WIDTH / 2, HEIGHT / 2)
        all_sprites_group.add(player)

    block_one = Block(BLUE, 20, 10)
    block_one.rect.centerx = WIDTH / 2
    all_sprites_group.add(block_one)

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC
        all_sprites_group.update()

        block_collided = pygame.sprite.spritecollide(player, block_sprite_group, True)

        if block_collided:
            print("----------")
            print("Mario has collided with a block!")
            print(block_collided)





        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)
        all_sprites_group.draw(screen)

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()
