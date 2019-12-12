from math import *


def prog_length(n1: int, n2: int):
    return n1 * log2(n1) + n2 * log2(n2)

def prog_volume(n: int, N: int):
    return N * log2(n)

def min_prog_volume(nstar: int):
    return (2 + nstar) * log2(2 + nstar)

def border_volume(nstar: int):
    return (2 + nstar * log2(nstar)) * log2(2 + nstar)

def ratio_operand_operator(n1: int, n2: int, nstar: int):
    A = nstar / (nstar+2) * log2(2 + nstar)
    B = nstar - 2 * A
    return A, B, A * n1

def prog_lvl(V: float, VS: float):
    return VS / V

def intelligent_content(n1: int, n2: int, N: int, N2: int):
    return 2 * n2 / (n1 * N2) * N * log2(n)

def work(V: int, L: int):
    return V / L

def time(E: float, S: float = 18):
    return E / S

def lang_lvl(L: float, V: float):
    return L ** 2 * V

def errors(V: float, VS: float, A: float):
    E0 = VS ** 3 / A ** 2
    print(E0)
    return V / E0


if __name__ == '__main__':
    n1 = int(input('Number of operators (n1): '))
    n2 = int(input('Number of operands (n2): '))
    N1 = int(input('Number of all operators (N1): '))
    N2 = int(input('Number of all operands (N2): '))
    nstar = int(input('Number of i/o operands: '))

    n = n1 + n2
    N = N1 + N2
    NTilda = prog_length(n1, n2)
    V = prog_volume(n, N)
    VS = min_prog_volume(nstar)
    VSS = border_volume(nstar)
    R = ratio_operand_operator(n1, n2, nstar)
    L = prog_lvl(V, VS)
    I = intelligent_content(n1, n2, N, N2)
    E = work(V, L)
    T = time(E)
    A = lang_lvl(L, V)
    B = errors(V, VS, A)

    print(f"""
        1) N': {round(NTilda, 2)}
        2) V: {round(V, 2)}
        3) V*: {round(VS, 2)}
        4) V**: {round(VSS, 2)}
        5) R: {round(R[2], 2)}, Ra: {R[0]}, Rb: {R[1]}
        6) L: {round(L, 2)}
        7) I: {round(I, 2)}
        8) E: {round(E, 2)}
        9) T: {round(T, 2)}
        10) A: {round(A, 2)}
        11) B: {round(B, 2)}
        """)
