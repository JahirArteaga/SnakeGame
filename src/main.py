import pygame
import sys

def main():
    # Inicializar el entorno de desarrollo y la librería multimedia
    pygame.init()
    
    # Definición inicial de las dimensiones de la ventana gráfica (600x600)
    ANCHO_VENTANA = 600
    ALTO_VENTANA = 600
    
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Snake Game - Avance Inicial Jahir Arteaga")
    
    # Gobernación del tiempo mediante tics para regular el bucle operativo
    reloj = pygame.time.Clock()
    ejecutando = True
    
    # Bucle de juego activo inicial (Game Loop básico no recurrente)
    while ejecutando:
        # Captura y evaluación de eventos del sistema operativo (Inputs)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
                
        # Estructura de refresco: Limpieza del lienzo visual con fondo oscuro
        pantalla.fill((18, 18, 18))
        
        # Intercambio de buffers de pantalla para actualizar los gráficos en la interfaz
        pygame.display.update()
        
        # Sincronización fija para estabilizar el hilo principal
        reloj.tick(60)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
