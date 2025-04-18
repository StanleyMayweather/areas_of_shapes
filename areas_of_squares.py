# Coding starts here...
import math

# --- Area Functions (Return Only) ---

def compute_area_rectangle(length, width):
    """Returns the area of a rectangle."""
    return length * width

def compute_area_square(side):
    """Returns the area of a square by using compute_area_rectangle."""
    return compute_area_rectangle(side, side)

def compute_area_circle(radius):
    """Returns the area of a circle."""
    return math.pi * (radius ** 2)


# --- Program Interaction Below ---

while True:
    shape = input("\nEnter the shape (square, rectangle, circle) or 'quit' to exit: ").strip().lower()

    if shape == "quit":
        print("Goodbye fella!")
        break

    elif shape == "square":
        try:
            side = float(input("Enter the length of the side of the square: "))
            area = compute_area_square(side)
            print(f"The area of the square is: {area:.2f}")
        except ValueError:
            print("Please enter a valid number.")

    elif shape == "rectangle":
        try:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = compute_area_rectangle(length, width)
            print(f"The area of the rectangle is: {area:.2f}")
        except ValueError:
            print("Please enter valid numbers.")

    elif shape == "circle":
        try:
            radius = float(input("Enter the radius of the circle: "))
            area = compute_area_circle(radius)
            print(f"The area of the circle is: {area:.2f}")
        except ValueError:
            print("Please enter a valid number.")

    else:
        print("Shape not recognized. Please enter 'square', 'rectangle', 'circle', or 'quit'.")
