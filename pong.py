"""Pong, classic arcade game.

Posibles cambios

1. Colisiones de las tablas con la pared
2. Incrementar la velocidad de la bola con cada golpe - Fernando Robles
3. Cambiar la bola de color con cada golpe
4. Cambiar el tamaño de la bola
5. Agregar más de una bola
6. Agregar jugador CPU - Mauricio Caballero
6. Niveles de dificultad
7. Marcadores - Fernando Robles
8. Power-ups
"""

from random import choice, random
from turtle import *

from freegames import vector


def value():
    """Randomly generate value between (-5, -3) or (3, 5)."""
    return (3 + random() * 2) * choice([1, -1])


ball = vector(0, 0)
aim = vector(value(), value())
state = {1: 0, 2: 0}


def move(player, change):
    """Move player position by change."""
    state[player] += change


def rectangle(x, y, width, height):
    """Draw rectangle at (x, y) with given width and height."""
    up()
    goto(x, y)
    down()
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()


def draw():
    """Draw game and move pong ball."""
    clear()
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)

    ball.move(aim)
    x = ball.x
    y = ball.y

    # Calcular cantidad de movimiento que necesita la segunda tabla
    cpu_movement = y - state[2]
    # mover la tabla por la cantidad requerida, con reducción para hacer el juego vencible
    move(2, cpu_movement*0.1)

    up()
    goto(x, y)
    dot(10)
    update()

    if y < -200 or y > 200:
        aim.y = -aim.y

    if x < -185:
        low = state[1]
        high = state[1] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    if x > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    ontimer(draw, 50)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
# Controles modificados para hacerlos intuitivos
onkey(lambda: move(1, 20), 'Up')
onkey(lambda: move(1, -20), 'Down')
draw()
done()
