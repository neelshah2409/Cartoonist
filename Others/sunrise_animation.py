# sunrise.py

import random
import turtle

from collections import namedtuple

number_of_steps = 500
number_of_stars = 200
sun_size = 150
width = 1200
height = 800

# Create Named Tuple Classes
RangeLimits = namedtuple("RangeLimits", "start, end")
Colour = namedtuple("Colour", "red, green, blue")

sky_colour = RangeLimits(
    Colour(0 / 255, 0 / 255, 0 / 255),
    Colour(0 / 255, 191 / 255, 255 / 255),
)
petal_colour = RangeLimits(
    Colour(50 / 255, 50 / 255, 50 / 255),
    Colour(138 / 255, 43 / 255, 226 / 255),
)
flower_centre_colour = RangeLimits(
    Colour(30 / 255, 30 / 255, 30 / 255),
    Colour(255 / 255, 165 / 255, 0 / 255),
)
stem_colour = RangeLimits(
    Colour(15 / 255, 15 / 255, 15 / 255),
    Colour(34 / 255, 139 / 255, 34 / 255),
)
star_colour = RangeLimits(
    Colour(1, 1, 1),
    sky_colour.end,
)
sun_colour = RangeLimits(
    Colour(10 / 255, 10 / 255, 10 / 255),
    Colour(249 / 255, 215 / 255, 28 / 255),
)

sun_x_coordinate = -width / 3
sun_y_position = RangeLimits(
    -height / 2 - sun_size / 2,
    height / 2 - height / 8,
)

def calculate_colour_change(
    start: Colour,
    end: Colour,
    n_steps: int,
):
    red_step = (end.red - start.red) / n_steps
    green_step = (end.green - start.green) / n_steps
    blue_step = (end.blue - start.blue) / n_steps

    return Colour(red_step, green_step, blue_step)

def calculate_movement_change(start, end, n_steps):
    return (end - start) / n_steps

# Set up the window for the animation
# Sky
sky = turtle.Screen()
sky.setup(width, height)
sky.tracer(0)
sky.title("Good morning…")
sky.bgcolor(sky_colour.start)

# Flower and Stem
flower = turtle.Turtle()
flower.hideturtle()
stem = turtle.Turtle()
stem.hideturtle()
stem.right(90)
stem.pensize(10)

def draw_flower(petal_col, flower_centre_col, stem_col):
    stem.clear()
    stem.color(stem_col)
    stem.forward(height / 2)
    stem.forward(-height / 2)

    flower.clear()
    flower.color(petal_col)
    # Draw petals
    for _ in range(6):
        flower.forward(100)
        flower.dot(75)
        flower.forward(-100)
        flower.left(360 / 6)
    # Draw centre of flower
    flower.color(flower_centre_col)
    flower.dot(175)

# Draw the initial flower using the starting colours
draw_flower(
    petal_colour.start,
    flower_centre_colour.start,
    stem_colour.start,
)

# Stars
stars = turtle.Turtle()
stars.hideturtle()
stars.penup()

# Generate pairs of coordinates for the star positions
star_positions = tuple(
    (
        random.randint(-width // 2, width // 2),
        random.randint(-width // 2, width // 2),
    )
    for _ in range(number_of_stars)
)
# …and size for the stars
star_sizes = tuple(
    random.randint(2, 8) for _ in range(number_of_stars)
)

def draw_stars(colour):
    stars.clear()
    stars.color(colour)
    for position, size in zip(star_positions, star_sizes):
        stars.setposition(position)
        stars.dot(size)

# Draw the initial stars using the starting colour
draw_stars(star_colour.start)

# Sun
sun = turtle.Turtle()
sun.hideturtle()
sun.setposition(sun_x_coordinate, sun_y_position.start)

def draw_sun(sun_col, sun_height):
    sun.clear()
    sun.color(sun_col)
    sun.sety(sun_height)
    sun.dot(sun_size)

draw_sun(sun_colour.start, sun_y_position.start)

####
# Calculate step sizes needed for colour changes
sky_colour_steps = calculate_colour_change(
    sky_colour.start, sky_colour.end, number_of_steps
)
petal_colour_steps = calculate_colour_change(
    petal_colour.start, petal_colour.end, number_of_steps
)
flower_centre_colour_steps = calculate_colour_change(
    flower_centre_colour.start,
    flower_centre_colour.end,
    number_of_steps,
)
stem_colour_steps = calculate_colour_change(
    stem_colour.start, stem_colour.end, number_of_steps
)
star_colour_steps = calculate_colour_change(
    star_colour.start, star_colour.end, number_of_steps
)
sun_colour_steps = calculate_colour_change(
    sun_colour.start, sun_colour.end, number_of_steps
)

sun_movement_steps = calculate_movement_change(
    sun_y_position.start, sun_y_position.end, number_of_steps
)

####
# Start animation
current_sky_colour = sky_colour.start._asdict()
current_petal_colour = petal_colour.start._asdict()
current_flower_centre_colour = flower_centre_colour.start._asdict()
current_stem_colour = stem_colour.start._asdict()
current_star_colour = star_colour.start._asdict()
current_sun_colour = sun_colour.start._asdict()

current_sun_y_position = sun_y_position.start

for _ in range(number_of_steps):
    # Sky
    current_sky_colour["red"] += sky_colour_steps.red
    current_sky_colour["green"] += sky_colour_steps.green
    current_sky_colour["blue"] += sky_colour_steps.blue
    # Change the background to use the new colour
    sky.bgcolor(current_sky_colour.values())

    # Stars
    current_star_colour["red"] += star_colour_steps.red
    current_star_colour["green"] += star_colour_steps.green
    current_star_colour["blue"] + star_colour_steps.blue

    draw_stars(current_star_colour.values())

    # Flower and Stem
    current_petal_colour["red"] += petal_colour_steps.red
    current_petal_colour["green"] += petal_colour_steps.green
    current_petal_colour["blue"] += petal_colour_steps.blue

    current_flower_centre_colour["red"] += flower_centre_colour_steps.red
    current_flower_centre_colour["green"] += flower_centre_colour_steps.green
    current_flower_centre_colour["blue"] += flower_centre_colour_steps.blue

    current_stem_colour["red"] += stem_colour_steps.red
    current_stem_colour["green"] += stem_colour_steps.green
    current_stem_colour["blue"] += stem_colour_steps.blue

    # Draw the flower again with the new colours
    draw_flower(
        current_petal_colour.values(),
        current_flower_centre_colour.values(),
        current_stem_colour.values(),
    )

    # Sun
    current_sun_colour["red"] += sun_colour_steps.red
    current_sun_colour["green"] += sun_colour_steps.green
    current_sun_colour["blue"] += sun_colour_steps.blue
    current_sun_y_position += sun_movement_steps

    draw_sun(current_sun_colour.values(), current_sun_y_position)

    sky.update()

turtle.done()