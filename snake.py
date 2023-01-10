import pygame

# Tamaño de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Velocidad de la serpiente
SNAKE_SPEED = 5

# Inicializa Pygame
pygame.init()

# Crea la ventana del juego
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Snake:
    def __init__(self):
        # Posición inicial de la serpiente
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2

        # Dirección inicial de la serpiente
        self.direction = "UP"

    def move(self):
        # Mueve la serpiente en la dirección actual
        if self.direction == "UP":
            self.y -= SNAKE_SPEED
        elif self.direction == "DOWN":
            self.y += SNAKE_SPEED
        elif self.direction == "LEFT":
            self.x -= SNAKE_SPEED
        elif self.direction == "RIGHT":
            self.x += SNAKE_SPEED

    def draw(self, screen):
        # Dibuja la serpiente en pantalla
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 10, 10))

class Food:
    def __init__(self):
        # Posición aleatoria para la comida
        self.x = randint(0, SCREEN_WIDTH)
        self.y = randint(0, SCREEN_HEIGHT)

    def draw(self, screen):
        # D
