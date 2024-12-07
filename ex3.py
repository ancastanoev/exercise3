import turtle
import math

# Define the points
points = [
    (4, 2), (7, -1), (3, -5), (-3, 6), (-4, 4), (-1, -1), (-2, -6)
]


# Step 1: Compute the Center of Mass
def center_of_mass(points):
    n = len(points)
    x_sum = sum(x for x, y in points)
    y_sum = sum(y for x, y in points)
    return (x_sum / n, y_sum / n)


# Step 2: Compute the Angle of Each Point
def angle_from_center(point, center):
    x, y = point
    cx, cy = center
    return math.atan2(y - cy, x - cx)


# Step 3: Sort Points by Angle
def sort_points_by_angle(points, center):
    return sorted(points, key=lambda point: angle_from_center(point, center))


# Step 4: Draw the Polygon using Turtle
def draw_polygon(sorted_points):
    turtle.speed(1)
    turtle.penup()

    # Move to the first point
    turtle.goto(sorted_points[0][0] * 20, sorted_points[0][1] * 20)  # Scale points
    turtle.pendown()

    # Draw the polygon
    for point in sorted_points[1:]:
        turtle.goto(point[0] * 20, point[1] * 20)  # Scale points

    # Close the polygon by returning to the starting point
    turtle.goto(sorted_points[0][0] * 20, sorted_points[0][1] * 20)


# Main Program
center = center_of_mass(points)
sorted_points = sort_points_by_angle(points, center)

# Set up the screen
turtle.bgcolor("white")
turtle.title("Polygon Drawing with Turtle")

# Set the screen to fit all points (optional scaling and positioning)
turtle.setworldcoordinates(-200, -200, 200, 200)

# Draw the sorted polygon
draw_polygon(sorted_points)

# Finish drawing
turtle.done()
