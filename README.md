# Escape del Laberinto 🧩

### Descripción:
**Escape del Laberinto** es un juego de puzzle en el que el jugador debe guiar a su personaje a través de un laberinto generado aleatoriamente y encontrar la salida. Cada partida genera un laberinto diferente, lo que garantiza que siempre habrá un nuevo desafío. El jugador se mueve por las casillas del laberinto usando las flechas del teclado.

### Objetivo del juego:
- El jugador controla un cuadrado rojo que debe encontrar la salida del laberinto.
- El laberinto es generado de manera aleatoria, pero siempre tendrá un camino hasta la salida.
- El tiempo que el jugador tarda en resolver el laberinto se muestra en pantalla.

---

### Características:
- Laberintos generados aleatoriamente en cada partida, usando el algoritmo de **backtracking** para garantizar siempre una salida.
- Control del personaje mediante las flechas del teclado.
- Se muestra el tiempo que el jugador tarda en completar el laberinto, lo que añade un elemento de desafío.

---

### Controles:
- **Flechas del teclado**:
  - `←` Mover a la izquierda
  - `→` Mover a la derecha
  - `↑` Mover hacia arriba
  - `↓` Mover hacia abajo

---

### Requisitos:
- **Python 3.x** (tiene que ser superior a 3)
- **Pygame** (librería para manejar gráficos y eventos)

---

### Instalación:
1. Clona o descarga este repositorio en tu computadora.
2. Abre una terminal o consola y navega al directorio del proyecto.
3. Asegúrate de tener **Pygame** instalado. Si no lo tienes, instálalo con el siguiente comando:
    ```
    pip install pygame
    ```
4. Para ejecutar el juego, corre el siguiente comando en la terminal:
    ```
    python game.py
    ```

---

### Cómo jugar:
1. Al iniciar el juego, se mostrará un menú con las siguientes instrucciones:
   - **Presiona 'J' para jugar**.
   - **Presiona 'Q' para salir**.
   - **Usa las flechas del teclado para moverte**.
2. Después de presionar 'J', se generará un laberinto aleatorio y el jugador (representado por un cuadro rojo) aparecerá en la esquina superior izquierda.
3. Usa las flechas del teclado para mover al jugador a través del laberinto.
4. El objetivo es llegar a la esquina inferior derecha del laberinto.
5. El tiempo que tardas en completar el laberinto se mostrará al final del juego.



