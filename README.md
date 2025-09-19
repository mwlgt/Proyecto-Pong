# Pong: Supercharged

### Evidencia final TC1001S

## Juego inicial:
1. Dos tablas se pueden subir y bajar con el teclado (w-s y i-k)
2. La pelota tiene rebota con las paredes y con las tablas
3. La pelota se mueve a velocidad fija
4. El momento en el que un jugador falle (la pelota golpea la pared del lado izquierdo o derecho), el juego para
5. Todo es de color negro

## Juego final:
1. Una tabla se puede subir y bajar con el teclado (arriba-abajo)
2. La segunda tabla se mueve en automático, se juega contra un CPU
3. Se seleccionan diferentes niveles de dificultad (velocidad del CPU) de acuerdo al puntaje actual del jugador
4. La pelota acelera con cada golpe
5. Cuando suceden suficientes golpes, se crea una segunda bola para añadir dificultad
6. Las pelotas cambian de color con cada golpe, indicando su velocidad
7. Cada vez que el jugador o el cpu falla, se añade un punto al tablero y se continua jugando
8. Hay un powerup que duplica el tamaño de la tabla/raqueta de cualquiera que haya conseguido el powerup

## Requisitos para correr
1. Python, probado entre versiones 3.6-3.10 (checar documentación freegames)
2. Freegames  

`python3 -m pip install freegames`
### Al cumplir con los requisitos, correr:
`python3 pong.py`
