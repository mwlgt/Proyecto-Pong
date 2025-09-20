"""Pong, classic arcade game.

Posibles cambios

1. Colisiones de las tablas con la pared                 - Mauricio Caballero
2. Incrementar la velocidad de la bola con cada golpe    - Fernando Robles
3. Cambiar la bola de color con cada golpe               - Horacio Díaz
4. Agregar más de una bola                               - Horacio Díaz
5. Agregar jugador CPU                                   - Mauricio Caballero
6. Niveles de dificultad                                 - Gabriel Espino
7. Marcadores                                            - Fernando Robles
8. Power-ups                                             - Gabriel Espino
"""

from random import choice, random, randint
from turtle import *

from freegames import vector


def value():
    """Randomly generate value between (-5, -3) or (3, 5)."""
    return (3 + random() * 2) * choice([1, -1])


# --- Configuración inicial ---
balls = []  # lista de pelotas
state = {1: 0, 2: 0}
powerup = vector(0, 100)
powerup_direction = 1
powerup_timer = 0
paddle_sizes = {1: 50, 2: 50}
score1 = 0  # Jugador
score2 = 0  # CPU
colors = ["red", "blue", "green", "orange", "purple", "cyan", "magenta", "black"]


def new_ball():
    """Crea una nueva pelota en el centro con dirección aleatoria."""
    return {
        "pos": vector(0, 0),
        "vel": vector(value(), value()),
        "color": "black",
        "last_hit": None,
    }


for _ in range(2):  # numero de bolas
    balls.append(new_ball())


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


def increase_speed(ball):
    """Aumenta la velocidad de la bola en cada rebote con la tabla."""
    ball["vel"].x *= 1.1
    ball["vel"].y *= 1.1


def change_ball_color(ball):
    """cambia color de la bola con cada golpe."""
    ball["color"] = choice(colors)


def draw():
    """Draw game and move pong balls."""
    global score1, score2
    global powerup, powerup_direction, powerup_timer

    clear()
    rectangle(-200, state[1], 10, paddle_sizes[1])
    rectangle(190, state[2], 10, paddle_sizes[2])

    # Dibujar marcador
    up()
    goto(0, 180)
    write(f"Jugador: {score1}  CPU: {score2}", align="center", font=("Arial", 16, "normal"))

    # Dibujar power-up
    if powerup is not None:
        powerup.y += 2 * powerup_direction
        if powerup.y > 180 or powerup.y < -180:
            powerup_direction *= -1

        up()
        goto(powerup.x, powerup.y)
        dot(15, "yellow")

    # Dibujar y mover todas las pelotas
    for ball in balls:
        ball["pos"].move(ball["vel"])
        x = ball["pos"].x
        y = ball["pos"].y

        #Dificultades
        difficulty = 0.15
        if score1 >= 3:
            difficulty = 0.25
        if score1 >= 6:
            difficulty = 0.35
        if score1 >= 10:
            difficulty = 0.6


        # CPU movimiento
        target_ball = max(balls, key=lambda b: b["pos"].x)
        cpu_movement = target_ball["pos"].y - state[2]
        move(2, cpu_movement * difficulty)

        # Dibujar pelota
        up()
        goto(x, y)
        dot(10, ball["color"])
        update()

        # Rebote con techo y piso
        if y < -200 or y > 200:
            ball["vel"].y = -ball["vel"].y

        # Rebote con jugador
        if x < -185:
            low = state[1]
            high = state[1] + paddle_sizes[1]

            if low <= y <= high:
                ball["vel"].x = -ball["vel"].x
                increase_speed(ball)
                change_ball_color(ball)
                ball["last_hit"] = 1
            else:
                score2 += 1
                reset_ball(ball)

        # Rebote con CPU
        if x > 185:
            low = state[2]
            high = state[2] + paddle_sizes[2]

            if low <= y <= high:
                ball["vel"].x = -ball["vel"].x
                increase_speed(ball)
                change_ball_color(ball)
                ball["last_hit"] = 2
            else:
                score1 += 1
                reset_ball(ball)

        # Colisión con power-up
        if powerup is not None:
            if abs(x - powerup.x) < 15 and abs(y - powerup.y) < 15:
                if ball["last_hit"] is not None:
                    activate_powerup(ball["last_hit"])
                powerup = None

    powerup_timer += 1
    if powerup_timer >= 200 and powerup is None:
        powerup_timer = 0
        powerup = vector(randint(-100, 100), randint(-150, 150))
        powerup_direction = 1

    ontimer(draw, 50)


def reset_ball(ball):
    """Reinicia una pelota al centro con nueva dirección"""
    ball["pos"] = vector(0, 0)
    ball["vel"] = vector(value(), value())
    ball["color"] = "black"


def activate_powerup(player):
    """Duplica tamaño de la paleta temporalmente"""
    global paddle_sizes
    paddle_sizes[player] = 100

    def reset_size():
        paddle_sizes[player] = 50

    ontimer(reset_size, 10000)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: move(1, 20), 'Up')
onkey(lambda: move(1, -20), 'Down')
draw()
done()


