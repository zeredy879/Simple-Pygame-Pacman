import pygame
import platform
import ctypes
import random
import conf


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x


def CreateWalls(working_sprits: pygame.sprite.Group) -> pygame.sprite.Group:
    walls = pygame.sprite.Group()
    for wall in conf.WALL_MAP:
        walls.add(
            Wall(
                wall[0],
                wall[1],
                wall[2],
                wall[3],
                conf.COLOR_SET[random.choice(list(conf.COLOR_SET))],
            )
        )
    working_sprits.add(walls)
    return walls


class Dot(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([width, height])
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


def CreateDots(working_sprits: pygame.sprite.Group) -> pygame.sprite.Group:
    Dots = pygame.sprite.Group()
    Dots.empty
    for row in range(19):
        for col in range(19):
            dot = Dot(conf.COLOR_SET[random.choice(list(conf.COLOR_SET))], 4, 4)
            dot.rect.x = 30 * col + 32
            dot.rect.y = 30 * row + 32
            if not pygame.sprite.spritecollide(dot, working_sprits, False):
                Dots.add(dot)
    working_sprits.add(Dots)
    return Dots


class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.direction = None

    def changedirection(self, direction):
        self.direction = direction

    def update(self, walls, dots):
        prev_x = self.rect.left
        prev_y = self.rect.top
        direction = self.direction
        match direction:
            case None:
                pass
            case pygame.K_LEFT:
                self.rect.left = prev_x - 30
            case pygame.K_RIGHT:
                self.rect.left = prev_x + 30
            case pygame.K_UP:
                self.rect.top = prev_y - 30
            case pygame.K_DOWN:
                self.rect.top = prev_y + 30
        if pygame.sprite.spritecollide(self, walls, False):
            self.rect.left = prev_x
            self.rect.top = prev_y
        pygame.sprite.spritecollide(self, dots, True)


def main():
    pygame.init()
    if platform.system() == "Windows":
        ctypes.windll.user32.SetProcessDPIAware()
    logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption(conf.CAPTION_NAME)
    screen = pygame.display.set_mode([conf.WIDTH, conf.HEIGHT])
    pacman = Pacman(287, (7 * 60) + 19, "pacman.png")
    working_sprites = pygame.sprite.Group()
    working_sprites.add(pacman)
    dots = CreateDots(working_sprites)
    running = True
    while running:
        walls = CreateWalls(working_sprites)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                pacman.changedirection(event.key)
        screen.fill((0, 0, 0))
        pacman.update(walls, dots)
        working_sprites.draw(screen)
        pygame.display.flip()
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    main()
