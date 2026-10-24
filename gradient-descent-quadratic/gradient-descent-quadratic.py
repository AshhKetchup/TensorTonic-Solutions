def f(a: float, b: float, c: float, x0: float) -> float:
    return a*(x0*x0) + b*x0 + c

def f_der(a: float, b: float, x0: float) -> float:
    return 2*a*x0 + b

def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    for i in range(steps):
        x0 = x0 - lr * f_der(a, b, x0)
    
    return x0
    