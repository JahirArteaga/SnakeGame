# SnakeGame
# Proyecto: Juego de la Serpiente

Este repositorio centraliza la fase inicial de desarrollo, la ingeniería de requerimientos y la fundamentación de arquitectura para la materia de Programación.

*   **Estudiante:** Jahir Arteaga
*   **Institución:** Universidad Internacional del Ecuador (UIDE)
*   **Carrera:** Ingeniería en Inteligencia Artificial

## Estructura Inicial del Repositorio
*   `docs/`: Directorio que almacena el Diagrama de Casos de Uso y la Arquitectura MVC extraídos del modelo funcional de ingeniería.
*   `src/main.py`: Código de avance inicial que establece de forma limpia la ventana gráfica y el Game Loop básico de tics temporales.
*   `requirements.txt`: Declaración de la dependencia tecnológica multimedia del sistema (Pygame).

##  Fundamentación Científica y Posición del Estudiante
*   **Enfoque Monolítico vs. Modular**: Tras evaluar la literatura de desarrollo, autores clásicos argumentan que un script monolítico optimiza el rendimiento en juegos pequeños debido a la baja sobrecarga en memoria. Cuestiono críticamente esta postura: un sistema monolítico genera un alto acoplamiento que imposibilita el escalamiento lógico.
*   **Selección Arquitectónica (MVC)**: Se eligió el patrón Modelo-Vista-Controlador (MVC). El fuerte desacoplamiento que proporciona es crítico. Separar el núcleo lógico y los datos de la interfaz visual permitirá, en iteraciones avanzadas de la carrera, sustituir el controlador humano por un agente inteligente autónomo sin modificar la renderización gráfica del juego.
