
#Pattern Matching : 2
x = "hello"
match x:
    case "hello":
        print("it is hello")
    case "hi":
        print("it is hi")
    case _:
        print("not a case")
print('-----------------------------------------')

def example_two(coords):
    match coords:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(F"Vertical line at y={y}")
        case (x, 0):
            print(F"Horizontal line at x={x}")
        case (x, y) if x == y:
            print("X = Y")
        case (x, y) if abs(x) == abs(y):
            print("|X| = [Y|")
        case (_, _):
            print("Valid Coords")
        case _:
            print("Invalid Coords")

example_two((-1,1))

print('-----------------------------------------')
def example(lst):
    match lst:
        case [_]:
            print("One element")
        case [_, _]:
            print("Two elements")
        case [x, y, z]:
            print(F"Three elements [x), [y], [2]")
        case [x, y, z, *a]:
            print(F"Three elements or more")
        case [x, y, z, _, *a]:
            print(F"Four elements or more")
        case _:
            print("None")

example((4,5,6,5,4,9,7))
