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

## Documentación
### Horacio Díaz
Yo lo que hice fue el punto 3 y 4, los cuales consistieron en hacer que la pelota cambie de color cada vez que le peguen y también en poder añadir más de una bola en la partida, para que el juego se vuelva más desafiante. Para hacer que la pelota cambie de color, simplemente creé una funcion en la cual permita escojer un color de la lista de colores al azar, y seleccionarlo para la bola cada vez que le peguen y que cambie de trayectoria, y para añadir más bolas al juego, lo hise con un for donde le puedas cambiar el numero de bolas que quieres en el juego, y dentro del for con un append hice para que añada a la lista de bolas el número de bolas del range.
