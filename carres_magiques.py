import pygame
import random
import time

# Définir le délai entre chaque changement d'image (en millisecondes)
CHANGE_INTERVAL = 2000  # 2 secondes

# Variables pour gérer le changement d'image
last_change_time = 0
current_mosaic = None

# Définir les constantes
WINDOW_SIZE = (700, 700)
TILE_SIZE = 2  # Taille des petits carrés en pixels
TILE_COUNT = WINDOW_SIZE[0] // TILE_SIZE
PALETTE_SIZE = 255  # Ajuster la taille de la palette
PALETTE_COLORS = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(PALETTE_SIZE)]

# Initialiser Pygame
pygame.init()
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Carré magique avec mosaïque [APPUER SUR ESPACE]")
clock = pygame.time.Clock()

# Convertir un index de couleur de la palette en une couleur RVB
def get_color_from_palette(color_index):
    return pygame.Color(*PALETTE_COLORS[color_index])

# Convertir un index de couleur de la palette en une couleur RVB
def get_color_from_palette(color_index):
    return pygame.Color(*PALETTE_COLORS[color_index])

# Dessiner la mosaïque à l'écran
def draw_mosaic(mosaic):
    for row in range(TILE_COUNT):
        for col in range(TILE_COUNT):
            color_index = mosaic[row][col]
            color = get_color_from_palette(color_index)
            x, y = col * TILE_SIZE, row * TILE_SIZE
            pygame.draw.rect(window, color, pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))

# Générer une nouvelle mosaïque
def generate_mosaic():
    mosaic = []
    for row in range(TILE_COUNT):
        row_mosaic = []
        for col in range(TILE_COUNT):
            color_index = random.randint(0, PALETTE_SIZE - 1)
            row_mosaic.append(color_index)
        mosaic.append(row_mosaic)
    return mosaic

# Générer une nouvelle mosaïque avec des formes géométriques en utilisant la suite de Fibonacci
def generate_fibonacci_mosaic():
    mosaic = []
    fib_sequence = [0, 1]  # Initialiser la suite de Fibonacci avec les deux premiers termes

    # Générer les termes de la suite de Fibonacci jusqu'à atteindre la taille de la mosaïque
    while len(fib_sequence) < TILE_COUNT * TILE_COUNT:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    # Utiliser les termes de la suite de Fibonacci comme indices de couleur dans la palette
    for row in range(TILE_COUNT):
        row_mosaic = []
        for col in range(TILE_COUNT):
            color_index = fib_sequence[row * TILE_COUNT + col] % PALETTE_SIZE
            row_mosaic.append(color_index)
        mosaic.append(row_mosaic)
    return mosaic

# Boucle principale du jeu
def main():
    global last_change_time, current_mosaic

    running = True
    current_mosaic = generate_mosaic()
    last_change_time = pygame.time.get_ticks()  # Initialise le temps de dernier changement

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_mosaic = generate_fibonacci_mosaic()
                    last_change_time = pygame.time.get_ticks()

        # Obtenir le temps actuel
        current_time = pygame.time.get_ticks()

        # Vérifier si le délai de 5 secondes s'est écoulé
        if current_time - last_change_time >= CHANGE_INTERVAL:
            # Changer l'image en générant une nouvelle mosaïque
            current_mosaic = generate_mosaic()
            last_change_time = current_time

        window.fill((255, 255, 255))  # Remplir l'écran avec du blanc
        draw_mosaic(current_mosaic)  # Dessiner la mosaïque courante
        pygame.display.flip()  # Rafraîchir l'écran
        clock.tick(60)  # Limiter la vitesse de la boucle principale à 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
