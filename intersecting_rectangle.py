# Write a piece of code to determine if two rectangles are intersecting each other or not?
def are_rectangles_intersecting(rect1, rect2):
    # Unpacking the coordinates
    # Bottom-left and top-right of first rectangle
    x1, y1, x2, y2 = rect1
    # Bottom-left and top-right of second rectangle
    x3, y3, x4, y4 = rect2  

    # Checking for non-overlapping conditions
    if x2 < x3 or x4 < x1:
        # if No horizontal overlap
        return False
    if y2 < y3 or y4 < y1:
        # if No vertical overlap
        return False

    # If neither condition is met, rectangles are intersecting
    return True

# Example usage
# Bottom-left (2,2), Top-right (5,5)
rect1 = (2, 2, 5, 5)
# Bottom-left (4,4), Top-right (7,7)
rect2 = (4, 4, 7, 7)
# Bottom-left (6,6), Top-right (8,8)
rect3 = (6, 6, 8, 8)

print(are_rectangles_intersecting(rect1, rect2))
print(are_rectangles_intersecting(rect1, rect3))
