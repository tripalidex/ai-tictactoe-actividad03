# ai-tictactoe-actividad03 🎮🤖

Este repositorio contiene la implementación de un agente de Inteligencia Artificial capaz de jugar Tic-Tac-Toe (Tres en Raya) de manera óptima. El proyecto utiliza el algoritmo matemático **Minimax** para la toma de decisiones, garantizando que el agente nunca pueda ser derrotado. 

La interfaz gráfica del usuario ha sido construida utilizando la librería Pygame.

## 🗂️ Estructura del Proyecto

El proyecto está dividido en dos módulos principales para separar la lógica del juego de la interfaz visual:

* **`tictactoe.py`**: Contiene toda la lógica del entorno de juego (definición de turnos, movimientos permitidos y detección de estados terminales). Además, incluye el motor de la IA implementado a través de la función `minimax(board)` y sus funciones de evaluación `max_valor` y `min_valor`.
* **`runner.py`**: Es el motor gráfico del juego. Maneja el bucle principal, renderiza el tablero interactivo de 3x3 y procesa los eventos del ratón para que el usuario pueda interactuar con la IA.
* **`requirements.txt`**: Archivo que lista las dependencias necesarias para la correcta ejecución del entorno.
* **`OpenSans-Regular.ttf`**: Archivo tipográfico utilizado por Pygame para renderizar los textos y fichas en la interfaz.

## 🚀 Instalación y Uso (Recomendado con Anaconda)

Para garantizar un entorno limpio y evitar conflictos entre librerías, se recomienda el uso de **Anaconda** o **Miniconda**. Sigue estos pasos para configurar el proyecto:

1.  **Clona el repositorio** en tu máquina local.
2.  **Abre tu terminal** (Anaconda Prompt en Windows o tu terminal habitual en macOS/Linux).
3.  **Crea un entorno virtual** llamado `tictactoe`.
4.  **Activa el entorno** recién creado.
5.  **Instala las dependencias** necesarias desde la terminal activa:
    ```bash
    pip install pygame
    ```
6.  **Ejecuta el simulador**:
    ```bash
    python runner.py
    ```

## 🎮 Cómo Jugar

1. Al ejecutar el programa, aparecerá el menú principal donde podrás elegir jugar como **X** o como **O**.
2. Por las reglas clásicas del juego, el jugador **X** siempre tiene el primer movimiento.
3. La Inteligencia Artificial evaluará el árbol de estados en cada turno y tomará siempre la acción matemática que maximice sus posibilidades de victoria o, en el peor de los casos, asegure un empate. 

¡Intenta ganarle!
