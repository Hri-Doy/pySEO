def f(x,y):
    result = 2*x + 4*y
    return result
output = f(2,3)
print(output)


def even_odd(numbers):
    if numbers % 2 == 0:
        return 'This is Even'
    else:
        return 'This is Odd'
output = even_odd(42)
print(output)

def trangle_area(base, height):
    area = .5 * base * height
    return area
output = trangle_area (20, 18)
print(output)