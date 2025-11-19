import math
import sys

def safe_eval(expr, x_val):
    """Safely evaluate mathematical expression"""
    try:
        return eval(expr, {"__builtins__": None}, {
            "x": x_val, "math": math, "sin": math.sin, "cos": math.cos,
            "tan": math.tan, "exp": math.exp, "log": math.log,
            "sqrt": math.sqrt, "pi": math.pi, "e": math.e,
            "abs": abs, "pow": pow
        })
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")

def derivative(expr, x_val, h=1e-7):
    """Numerical derivative using central difference"""
    return (safe_eval(expr, x_val + h) - safe_eval(expr, x_val - h)) / (2 * h)

def bisection_method(expr, a, b, tol, max_iter):
    """Bisection Method"""
    print("\n" + "="*80)
    print("BISECTION METHOD")
    print("="*80)
    print(f"{'Iter':<6} {'a':<15} {'b':<15} {'c':<15} {'f(c)':<15} {'Error':<15}")
    print("-"*80)
    
    iterations = []
    fa = safe_eval(expr, a)
    fb = safe_eval(expr, b)
    
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    
    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = safe_eval(expr, c)
        error = abs(b - a) / 2
        
        iterations.append({
            'iter': i, 'a': a, 'b': b, 'c': c, 'fc': fc, 'error': error
        })
        print(f"{i:<6} {a:<15.8f} {b:<15.8f} {c:<15.8f} {fc:<15.8e} {error:<15.8e}")
        
        if error < tol or abs(fc) < tol:
            print("="*80)
            print(f"Root found: x = {c:.10f}")
            print(f"f(x) = {fc:.10e}")
            print(f"Total iterations: {i}")
            print(f"Final error: {error:.10e}")
            return c, i, error
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    raise ValueError("Maximum iterations reached without convergence")

def regula_falsi_method(expr, a, b, tol, max_iter):
    """Regula Falsi (False Position) Method"""
    print("\n" + "="*80)
    print("REGULA FALSI METHOD")
    print("="*80)
    print(f"{'Iter':<6} {'a':<15} {'b':<15} {'c':<15} {'f(c)':<15} {'Error':<15}")
    print("-"*80)
    
    iterations = []
    c_old = a
    
    for i in range(1, max_iter + 1):
        fa = safe_eval(expr, a)
        fb = safe_eval(expr, b)
        
        c = (a * fb - b * fa) / (fb - fa)
        fc = safe_eval(expr, c)
        error = abs(c - c_old) if i > 1 else abs(b - a)
        
        iterations.append({
            'iter': i, 'a': a, 'b': b, 'c': c, 'fc': fc, 'error': error
        })
        print(f"{i:<6} {a:<15.8f} {b:<15.8f} {c:<15.8f} {fc:<15.8e} {error:<15.8e}")
        
        if error < tol or abs(fc) < tol:
            print("="*80)
            print(f"Root found: x = {c:.10f}")
            print(f"f(x) = {fc:.10e}")
            print(f"Total iterations: {i}")
            print(f"Final error: {error:.10e}")
            return c, i, error
        
        if fa * fc < 0:
            b = c
        else:
            a = c
        
        c_old = c
    
    raise ValueError("Maximum iterations reached without convergence")

def secant_method(expr, x0, x1, tol, max_iter):
    """Secant Method"""
    print("\n" + "="*80)
    print("SECANT METHOD")
    print("="*80)
    print(f"{'Iter':<6} {'x0':<15} {'x1':<15} {'f(x1)':<15} {'Error':<15}")
    print("-"*80)
    
    iterations = []
    
    for i in range(1, max_iter + 1):
        f0 = safe_eval(expr, x0)
        f1 = safe_eval(expr, x1)
        
        if abs(f1 - f0) < 1e-14:
            raise ValueError("Division by zero in secant method")
        
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        error = abs(x2 - x1)
        
        iterations.append({
            'iter': i, 'x0': x0, 'x1': x1, 'f1': f1, 'error': error
        })
        print(f"{i:<6} {x0:<15.8f} {x1:<15.8f} {f1:<15.8e} {error:<15.8e}")
        
        if error < tol or abs(f1) < tol:
            print("="*80)
            print(f"Root found: x = {x2:.10f}")
            print(f"f(x) = {safe_eval(expr, x2):.10e}")
            print(f"Total iterations: {i}")
            print(f"Final error: {error:.10e}")
            return x2, i, error
        
        x0, x1 = x1, x2
    
    raise ValueError("Maximum iterations reached without convergence")

def newton_raphson_method(expr, x0, tol, max_iter):
    """Newton-Raphson Method"""
    print("\n" + "="*80)
    print("NEWTON-RAPHSON METHOD")
    print("="*80)
    print(f"{'Iter':<6} {'x':<15} {'f(x)':<15} {'f\'(x)':<15} {'Error':<15}")
    print("-"*80)

    iterations = []
    x = x0

    for i in range(1, max_iter + 1):
        fx = safe_eval(expr, x)
        fpx = derivative(expr, x)

        if abs(fpx) < 1e-14:
            raise ValueError("Derivative too close to zero")

        x_new = x - fx / fpx
        error = abs(x_new - x)

        iterations.append({
            'iter': i, 'x': x, 'fx': fx, 'fpx': fpx, 'error': error
        })
        print(f"{i:<6} {x:<15.8f} {fx:<15.8e} {fpx:<15.8e} {error:<15.8e}")

        if error < tol or abs(fx) < tol:
            print("="*80)
            print(f"Root found: x = {x_new:.10f}")
            print(f"f(x) = {safe_eval(expr, x_new):.10e}")
            print(f"Total iterations: {i}")
            print(f"Final error: {error:.10e}")
            return x_new, i, error

        x = x_new

    raise ValueError("Maximum iterations reached without convergence")

def fixed_point_method(expr, g_expr, x0, tol, max_iter):
    """Fixed Point Iteration Method"""
    print("\n" + "="*80)
    print("FIXED POINT ITERATION METHOD")
    print("="*80)
    print(f"{'Iter':<6} {'x':<15} {'g(x)':<15} {'f(x)':<15} {'Error':<15}")
    print("-"*80)

    iterations = []
    x = x0

    for i in range(1, max_iter + 1):
        g_x = safe_eval(g_expr, x)
        fx = safe_eval(expr, x)
        error = abs(g_x - x)

        iterations.append({
            'iter': i, 'x': x, 'gx': g_x, 'fx': fx, 'error': error
        })
        print(f"{i:<6} {x:<15.8f} {g_x:<15.8f} {fx:<15.8e} {error:<15.8e}")

        if error < tol or abs(fx) < tol:
            print("="*80)
            print(f"Root found: x = {g_x:.10f}")
            print(f"f(x) = {safe_eval(expr, g_x):.10e}")
            print(f"Total iterations: {i}")
            print(f"Final error: {error:.10e}")
            return g_x, i, error

        x = g_x

    raise ValueError("Maximum iterations reached without convergence")

def modified_secant_method(expr, x0, delta, tol, max_iter):
    """Modified Secant Method"""
    print("\n" + "="*80)
    print("MODIFIED SECANT METHOD")
    print("="*80)
    print(f"{'Iter':<6} {'x':<15} {'f(x)':<15} {'f(x+δx)':<15} {'Error':<15}")
    print("-"*80)

    iterations = []
    x = x0

    for i in range(1, max_iter + 1):
        fx = safe_eval(expr, x)
        fx_delta = safe_eval(expr, x + delta * x)

        if abs(fx_delta - fx) < 1e-14:
            raise ValueError("Division by zero in modified secant method")

        x_new = x - fx * (delta * x) / (fx_delta - fx)
        error = abs(x_new - x)

        iterations.append({
            'iter': i, 'x': x, 'fx': fx, 'fx_delta': fx_delta, 'error': error
        })
        print(f"{i:<6} {x:<15.8f} {fx:<15.8e} {fx_delta:<15.8e} {error:<15.8e}")

        if error < tol or abs(fx) < tol:
            print("="*80)
            print(f"Root found: x = {x_new:.10f}")
            print(f"f(x) = {safe_eval(expr, x_new):.10e}")
            print(f"Total iterations: {i}")
            print(f"Final error: {error:.10e}")
            return x_new, i, error

        x = x_new

    raise ValueError("Maximum iterations reached without convergence")

def get_float_input(prompt, default=None):
    """Get validated float input from user"""
    while True:
        try:
            value = input(prompt)
            if value.strip() == "" and default is not None:
                return default
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_int_input(prompt, default=None):
    """Get validated integer input from user"""
    while True:
        try:
            value = input(prompt)
            if value.strip() == "" and default is not None:
                return default
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    """Main CLI interface"""
    print("\n" + "="*80)
    print(" "*20 + "ZERO OF FUNCTIONS (ZOF) SOLVER")
    print(" "*25 + "Numerical Methods CLI")
    print("="*80)

    print("\nAvailable Methods:")
    print("1. Bisection Method")
    print("2. Regula Falsi (False Position) Method")
    print("3. Secant Method")
    print("4. Newton-Raphson Method")
    print("5. Fixed Point Iteration Method")
    print("6. Modified Secant Method")

    method = get_int_input("\nSelect method (1-6): ")

    if method not in [1, 2, 3, 4, 5, 6]:
        print("Invalid method selection.")
        return

    print("\nEnter the equation f(x) = 0")
    print("Example: x**3 - x - 2  or  math.exp(x) - 3*x")
    expr = input("f(x) = ")

    tol = get_float_input("Enter tolerance (default 1e-6): ", 1e-6)
    max_iter = get_int_input("Enter maximum iterations (default 100): ", 100)

    try:
        if method == 1:  # Bisection
            a = get_float_input("Enter lower bound a: ")
            b = get_float_input("Enter upper bound b: ")
            bisection_method(expr, a, b, tol, max_iter)

        elif method == 2:  # Regula Falsi
            a = get_float_input("Enter lower bound a: ")
            b = get_float_input("Enter upper bound b: ")
            regula_falsi_method(expr, a, b, tol, max_iter)

        elif method == 3:  # Secant
            x0 = get_float_input("Enter first initial guess x0: ")
            x1 = get_float_input("Enter second initial guess x1: ")
            secant_method(expr, x0, x1, tol, max_iter)

        elif method == 4:  # Newton-Raphson
            x0 = get_float_input("Enter initial guess x0: ")
            newton_raphson_method(expr, x0, tol, max_iter)

        elif method == 5:  # Fixed Point
            print("\nFor f(x) = 0, rearrange to x = g(x)")
            print("Example: if f(x) = x**2 - 2, then g(x) = sqrt(2) or math.sqrt(2)")
            g_expr = input("g(x) = ")
            x0 = get_float_input("Enter initial guess x0: ")
            fixed_point_method(expr, g_expr, x0, tol, max_iter)

        elif method == 6:  # Modified Secant
            x0 = get_float_input("Enter initial guess x0: ")
            delta = get_float_input("Enter delta (default 0.01): ", 0.01)
            modified_secant_method(expr, x0, delta, tol, max_iter)

    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

