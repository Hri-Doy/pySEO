def rectangular(length, width):
    """_summary_
    This function calculates the area of rectangular

    Args:
        length (int): Any number
        width (int): Any number
        return: Area of rectangular
    """
    area = length * width
    return area
r2 = rectangular(30, 20)
# Here position must be maintained means which is length and which is width
print(r2)
r1 = rectangular(length=30, width=20)
# Keyword Argument
# Defining which is what
print(r1)
