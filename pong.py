"""Pong, classic arcade game.

Posibles cambios

1. Colisiones de las tablas con la pared - Mauricio Caballero
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
from random import choice, random, randint
from turtle import *

from freegames import vector


def value():
    """Randomly generate value between (-5, -3) or (3, 5)."""
    return (3 + random() * 2) * choice([1, -1])


ball = vector(0, 0)
aim = vector(value(), value())
state = {1: 0, 2: 0}

# Variables para determinar el power-up
powerup = vector(0, 100)
powerup_direction = 1
powerup_timer = 0
paddle_sizes = {1: 50, 2: 50}
last_hit = None

# Marcadores
score1 = 0 # Jugador
score2 = 0 # CPU


def move(player, change):
    """Move player position by change."""
    state[player] += change
    if state[player] > 160:
        state[player] = 160
    elif state[player] < -210:
        state[player] = -210


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


def increase_speed():
    """Aumenta la velocidad de la vola en cada rebote con la tabla."""
    global aim
    aim.x *= 1.1
    aim.y *= 1.1
    

def draw():
    """Draw game and move pong ball."""
    global score1, score2
    global powerup, powerup_direction, powerup_timer
    global last_hit

    clear()
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)
    rectangle(-200, state[1], 10, paddle_sizes[1])
    rectangle(190, state[2], 10, paddle_sizes[2])

    # Dibujar marcador
    up()
    goto(0, 180)
    write(f"Jugador: {score1} CPU: {score2}", align= "center", font=("Arial", 16, "normal"))

    # Dibujar power-up
    # Dibujar power-up
    if powerup is not None:
        powerup.y += 2 * powerup_direction  # velocidad de subida/bajada
        if powerup.y > 180 or powerup.y < -180:
            powerup_direction *= -1  # invertir dirección

        up()
        goto(powerup.x, powerup.y)
        dot(15, "purple")


    ball.move(aim)
    x = ball.x
    y = ball.y

    # Calcular cantidad de movimiento que necesita la segunda tabla
    cpu_movement = y - state[2]
    # mover la tabla por la cantidad requerida, con reducción para hacer el juego vencible
    move(2, cpu_movement*0.15)

    up()
    goto(x, y)
    dot(10)
    update()

    if y < -200 or y > 200:
        aim.y = -aim.y

    if x < -185:
        low = state[1]
        high = state[1] + 50
        high = state[1] + paddle_sizes[1]

        if low <= y <= high:
            aim.x = -aim.x
<<<<<<< Updated upstream
            increase_speed() # aumenta velocidad al rebotar con jugador
=======
            last_hit = 1
>>>>>>> Stashed changes
        else:
            score2 += 1 # CPU gana punto
            reset_ball()

    if x > 185:
        low = state[2]
        high = state[2] + 50
        high = state[2] + paddle_sizes[2]

        if low <= y <= high:
            aim.x = -aim.x
<<<<<<< Updated upstream
            increase_speed() # aumenta velocidad al rebotar con CPU
=======
            last_hit = 2
>>>>>>> Stashed changes
        else:
            score1 += 1 # Jugador gana punto
            reset_ball()

    # Colisión con la pelota
    if powerup is not None:
        if abs(x - powerup.x) < 15 and abs(y - powerup.y) < 15:
            if last_hit:
                activate_powerup(last_hit)
            powerup = None  # quitarlo tras colisión


    powerup_timer += 1

    if powerup_timer >= 200 and powerup is None:
        powerup_timer = 0
        powerup = vector(randint(-100, 100), randint(-150, 150))
        powerup_direction = 1

    ontimer(draw, 50)


def reset_ball():
    """Reinicia la bola al centro con nueva dirección"""
    global ball, aim
    ball = vector(0, 0)
    aim = vector(value(), value())


def activate_powerup(player):
    """Duplica tamaño de la paleta temporalmente"""
    global paddle_sizes
    paddle_sizes[player] = 100  # duplicar tamaño

    def reset_size():
        paddle_sizes[player] = 50

    # restaurar después de 10 segundos
    ontimer(reset_size, 10000)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
# Controles modificados para hacerlos intuitivos
onkey(lambda: move(1, 20), 'Up')
onkey(lambda: move(1, -20), 'Down')
draw()
done()
