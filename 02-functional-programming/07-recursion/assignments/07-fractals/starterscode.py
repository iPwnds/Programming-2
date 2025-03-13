import turtle

SPEED = 5
BG_COLOR = "blue"
PEN_COLOR = "lightgreen"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
DRAWING_WIDTH = 700
DRAWING_HEIGHT = 700
PEN_WIDTH = 5
TITLE = "H-Tree Fractal with Python Turtle Graphics"
FRACTAL_DEPTH = 5


def draw_line(tur, pos1, pos2):
    # print("Drawing from", pos1, "to", pos2)  # Uncomment for tracing the algorithm.
    tur.penup()
    tur.goto(pos1[0], pos1[1])
    tur.pendown()
    tur.goto(pos2[0], pos2[1])
    
    
# tur = the instance of a turtle object, we need to pass this to the draw_line function to draw lines.
# x = the X-coordinate to start drawing from
# y = the Y-coordinate to start drawing from
# width = the width of the space we draw the next drawing in
# height = the height of the space we draw the next drawing in
# count = the depth of the recursive element at this point.
def recursive_draw(tur, x, y, length, angle, count):
    """
    Draws a Y-shaped fractal recursively.
    
    Parameters:
    - tur: The turtle instance for drawing.
    - x, y: Starting position for the current branch.
    - length: The length of the current branch.
    - angle: The angle between branches.
    - count: The recursion depth.
    """
    if count == 0:
        return  # Base case: stop when depth is 0

    # Move to starting position
    tur.penup()
    tur.goto(x, y)
    tur.pendown()
    
    # Draw trunk
    tur.setheading(angle)  # Point upwards
    tur.forward(length)

    # Get the endpoint of the trunk
    new_x, new_y = tur.position()

    # Compute new branch length
    new_length = length * 0.6  # Reduce size at each step

    # Draw left branch
    tur.setheading(angle+30)
    tur.forward(new_length)
    left_x, left_y = tur.position()
    tur.backward(new_length)  # Move back

    # Draw right branch
    tur.setheading(angle-30)
    tur.forward(new_length)
    right_x, right_y = tur.position()
    tur.backward(new_length)  # Move back

    # Recursive calls for the left and right branches
    recursive_draw(tur, left_x, left_y, new_length, angle+30, count - 1)
    recursive_draw(tur, right_x, right_y, new_length, angle-30, count - 1)



if __name__ == "__main__":
    # Screen setup
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title(TITLE)
    screen.bgcolor(BG_COLOR)

    # Turtle artist (pen) setup
    tur = turtle.Turtle()
    tur.hideturtle()
    tur.pensize(PEN_WIDTH)
    tur.color(PEN_COLOR)
    tur.speed(SPEED)

    # Initial call to recursive draw function
    recursive_draw(tur, 0, -SCREEN_HEIGHT // 3, DRAWING_HEIGHT // 4, 90, FRACTAL_DEPTH)

    # Every Python Turtle program needs this (or an equivalent) to work correctly.
    turtle.done()