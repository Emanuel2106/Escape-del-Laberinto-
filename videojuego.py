import pygame
import random

# Inicialización de PyGame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600  # Tamaño de la pantalla
TILE_SIZE = 40  # Tamaño de las casillas del laberinto
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape del Laberinto")

# Colores
WHITE = (255, 255, 255)  # Blanco
BLACK = (0, 0, 0)        # Negro
RED = (255, 0, 0)        # Rojo para el jugador
BLUE = (0, 0, 255)       # Azul para el texto

# Jugador
player_size = TILE_SIZE - 10  # Tamaño del jugador (cuadro rojo)
player_x, player_y = TILE_SIZE + 5, TILE_SIZE + 5  # Posición inicial del jugador
player_speed = TILE_SIZE  # El jugador se moverá de casilla en casilla

# Laberinto
maze_width = WIDTH // TILE_SIZE  # Ancho del laberinto en casillas
maze_height = HEIGHT // TILE_SIZE  # Alto del laberinto en casillas
maze = []  # Guardaremos el laberinto aquí

# Direcciones para moverse en el laberinto (arriba, abajo, izquierda, derecha)
directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

# Variables del juego
start_time = 0  # Tiempo al iniciar
end_time = 0  # Tiempo al finalizar
game_running = True  # Control del estado del juego

# Fuente para el texto en pantalla
font = pygame.font.SysFont(None, 35)

# Función para generar el laberinto
def generate_maze():
    global maze
    maze = [[1 for _ in range(maze_width)] for _ in range(maze_height)]  # Crear un laberinto lleno de paredes

    # Algoritmo de backtracking para crear caminos
    def dfs(x, y):
        maze[y][x] = 0  # Crear un camino en la posición actual
        random.shuffle(directions)  # Aleatoriza las direcciones para mayor variabilidad
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < maze_width - 1 and 1 <= ny < maze_height - 1 and maze[ny][nx] == 1:
                maze[ny - dy // 2][nx - dx // 2] = 0  # Quitar la pared entre celdas
                dfs(nx, ny)

    dfs(1, 1)  # Empezar desde la celda (1, 1)
    maze[maze_height - 2][maze_width - 2] = 0  # Asegura que la salida esté abierta

# Función para dibujar el laberinto
def draw_maze():
    for y in range(maze_height):
        for x in range(maze_width):
            color = BLACK if maze[y][x] == 1 else WHITE  # Paredes son negras, caminos blancos
            pygame.draw.rect(screen, color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

# Función para mover al jugador
def move_player(dx, dy):
    global player_x, player_y
    new_x = player_x + dx  # Nueva posición en X
    new_y = player_y + dy  # Nueva posición en Y

    # Verificar si la nueva posición está dentro del laberinto y si no es una pared
    if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT:
        tile_x = new_x // TILE_SIZE
        tile_y = new_y // TILE_SIZE

        if maze[tile_y][tile_x] == 0:  # Verifica si es un camino
            player_x = new_x
            player_y = new_y

# Función para verificar si el jugador llegó a la salida
def detect_exit():
    if player_x // TILE_SIZE == maze_width - 2 and player_y // TILE_SIZE == maze_height - 2:
        return True
    return False

# Muestra el tiempo en pantalla
def display_time(current_time):
    time_text = font.render(f"Tiempo: {current_time:.2f} s", True, BLUE)
    screen.blit(time_text, [10, 10])

# Menú principal
def main_menu():
    running = True
    while running:
        screen.fill(WHITE)
        
        # Mensaje principal
        menu_text = font.render("Presiona 'J' para jugar o 'Q' para salir", True, BLACK)
        screen.blit(menu_text, [WIDTH // 4, HEIGHT // 2])

        # Instrucciones de juego
        controls_text = font.render("Usa las flechas del teclado para moverte", True, BLACK)
        screen.blit(controls_text, [WIDTH // 4, (HEIGHT // 2) + 50])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:  # Si presiona "J", comienza el juego
                    game_loop()
                if event.key == pygame.K_q:  # Si presiona "Q", sale del juego
                    pygame.quit()
                    quit()

        pygame.display.update()

# Bucle principal del juego
def game_loop():
    global player_x, player_y, start_time, end_time, game_running

    # Generar el laberinto y reiniciar variables
    generate_maze()
    player_x, player_y = TILE_SIZE + 5, TILE_SIZE + 5  # Posición inicial del jugador
    start_time = pygame.time.get_ticks()  # Inicia el temporizador
    game_running = True

    while game_running:
        screen.fill(WHITE)
        draw_maze()  # Dibuja el laberinto

        # Movimiento del jugador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # Mover a la izquierda
                    move_player(-player_speed, 0)
                if event.key == pygame.K_RIGHT:  # Mover a la derecha
                    move_player(player_speed, 0)
                if event.key == pygame.K_UP:  # Mover hacia arriba
                    move_player(0, -player_speed)
                if event.key == pygame.K_DOWN:  # Mover hacia abajo
                    move_player(0, player_speed)

        # Dibuja al jugador en su posición
        pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

        # Verificar si el jugador ha llegado a la salida
        if detect_exit():
            game_running = False  # Termina el juego
            end_time = pygame.time.get_ticks()  # Guarda el tiempo al final

        # Muestra el tiempo transcurrido
        current_time = (pygame.time.get_ticks() - start_time) / 1000  # Convertir a segundos
        display_time(current_time)

        pygame.display.update()

    # Mostrar el tiempo final y regresar al menú principal
    while True:
        screen.fill(WHITE)
        final_time = (end_time - start_time) / 1000  # Calcula el tiempo final
        end_text = font.render(f"¡Lo lograste! Tiempo final: {final_time:.2f} s", True, BLUE)
        screen.blit(end_text, [WIDTH // 4, HEIGHT // 2])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                main_menu()  # Regresar al menú principal

        pygame.display.update()

# Ejecutar el menú principal
main_menu()
