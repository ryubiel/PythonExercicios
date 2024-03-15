def fatorial(n , show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    f = 1
    for c in range(n,0,-1):
        if show:
            print(f"{c}", end="")
            print(" x " if c > 1 else " = ", end="")
        f *= c
    return f


print(fatorial(5, show=True))