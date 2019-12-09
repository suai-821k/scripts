from math import *


def ellipse():
    while True:
        try:
            a, b = (float(i) for i in input('Enter a b: ').split(' '))
            break
        except ValueError:
            print('Try again.')

    c = sqrt(a - b)

    print(f"""
    1) a^2: {a}
    2) a: {sqrt(a)}
    3) b^2: {b}
    4) b: {sqrt(b)}
    5) A2: ({-sqrt(a)}, 0)
    6) A1: ({sqrt(a)}, 0)
    7) B2: (0, {-sqrt(b)})
    8) B1: (0, {sqrt(b)})
    9) |A2A1|: {sqrt(a) * 2}
    10) |B2B1|: {sqrt(b) * 2}
    11) c: {c}
    12) F2: ({-c}. 0)
    13) F1: ({c}, 0)
    14) |F2F1|: {c * 2}
    15) E: {c / sqrt(a)}
    """)


def hyperbola():
    while True:
        try:
            a, b = (float(i) for i in input('Enter a b: ').split(' '))
            break
        except ValueError:
            print('Try again.')

    c = sqrt(a + b)

    print(f"""
    1) a^2: {a}
    2) a: {sqrt(a)}
    3) b^2: {b}
    4) b: {sqrt(b)}
    5) A2: ({-sqrt(a)}, 0)
    6) A1: ({sqrt(a)}, 0)
    7) B2: (0, {-sqrt(b)})
    8) B1: (0, {sqrt(b)})
    9) |A2A1|: {sqrt(a) * 2}
    10) |B2B1|: {sqrt(b) * 2}
    11) c: {c}
    12) F2: ({-c}. 0)
    13) F1: ({c}, 0)
    14) |F2F1|: {c * 2}
    15) y = ({sqrt(b)}/{sqrt(a)})x, y = -({sqrt(b)}/{sqrt(a)})x
    16) E: {c}/{sqrt(a)} ({c / sqrt(a)})
    """)


def parabola():
    while True:
        while True:
            try:
                choice = int(input('Choose type:\n1) y^2 = 2px\n2) y^2 = -2px\n3) x^2 = 2px\n4) x^2 = -2px\n: '))
                p2 = float(input('p: '))
                p = p2 / 2
                break
            except ValueError:
                print('Try again')
        if choice == 1:
            print(f'1) Branch dir: >\n2) p: {p}\n3) d: x={-(p/2)} ({p}/2)\n4) F: (0, -({p/2}) ({-p}/2))')
        elif choice == 2:
            print(f'1) Branch dir: <\n2) p: {p}\n3) d: x={p/2} ({p}/2)\n4) F: (0, {p/2}({p}/2))')
        elif choice == 3:
            print(f'1) Branch dir: ^\n2) p: {p}\n3) d: y={-(p/2)} -({p}/2)\n4) F: (0, {-(p/2)}({-p}/2))')
        elif choice == 4:
            print(f'1) Branch dir: \/\n2) p: {p}\n3) d: y={p/2} ({p}/2)\n4) F: (0, {p/2}({p}/2)')
        else:
            print('Some error here')
        break

if __name__ == '__main__':
    while True:
        while True:
            try:
                choice: int = int(input('1) Ellipse\n2) Hyperbola\n3) Parabola\n: '))
                break
            except ValueError:
                print('Some error here')

        if choice == 1:
            ellipse()
        elif choice == 2:
            hyperbola()
        elif choice == 3:
            parabola()
        elif choice == 0:
            break