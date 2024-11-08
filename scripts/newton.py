def newton(f, df, x0, tol=1e-6, max_iter=100):
    """Implementa el método de Newton para encontrar las raíces de una función.

    Parametros
    ----------
    f:
        La función para la cual queremos encontrar la raíz.
    df:
        La derivada de la función f
    x0:
        Estimación inicial de la raíz.\n
    tol:
        Tolerancia para la convergencia (opcional, por defecto es 1e-6).\n
    max_iter:
        Número máximo de iteraciones (opcional, por defecto es 100).\n

    Returna
    -------
    float:
        La estimación de la raíz de la función f.
    """
    x = x0
    for i in range(max_iter):
        # calculo f(x) y df(x)
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            # si f(x) es menor que la tolerancia, devolvemos x
            return x
        else:
            # de lo contrario calculamos el nuevo x
            x = x - fx / dfx
    # Si el metodo no converge retornamos None
    return None


def f(x):
    return x**2 - 1


def df(x):
    return 2 * x


def main():
    print(newton(f, df, -500))


# Esto sirve para poder usar este código como módulo y script al mismo tiempo
if __name__ == "__main__":
    main()
