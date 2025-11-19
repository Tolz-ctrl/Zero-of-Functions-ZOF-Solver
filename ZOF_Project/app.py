from flask import Flask, render_template, request, jsonify
import math
import traceback

app = Flask(__name__)

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
            'iteration': i,
            'a': f"{a:.8f}",
            'b': f"{b:.8f}",
            'c': f"{c:.8f}",
            'fc': f"{fc:.8e}",
            'error': f"{error:.8e}"
        })
        
        if error < tol or abs(fc) < tol:
            return {
                'root': c,
                'iterations': iterations,
                'total_iterations': i,
                'final_error': error,
                'fx': fc
            }
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    raise ValueError("Maximum iterations reached without convergence")

def regula_falsi_method(expr, a, b, tol, max_iter):
    """Regula Falsi Method"""
    iterations = []
    c_old = a
    
    for i in range(1, max_iter + 1):
        fa = safe_eval(expr, a)
        fb = safe_eval(expr, b)
        
        c = (a * fb - b * fa) / (fb - fa)
        fc = safe_eval(expr, c)
        error = abs(c - c_old) if i > 1 else abs(b - a)
        
        iterations.append({
            'iteration': i,
            'a': f"{a:.8f}",
            'b': f"{b:.8f}",
            'c': f"{c:.8f}",
            'fc': f"{fc:.8e}",
            'error': f"{error:.8e}"
        })
        
        if error < tol or abs(fc) < tol:
            return {
                'root': c,
                'iterations': iterations,
                'total_iterations': i,
                'final_error': error,
                'fx': fc
            }
        
        if fa * fc < 0:
            b = c
        else:
            a = c
        
        c_old = c
    
    raise ValueError("Maximum iterations reached without convergence")

def secant_method(expr, x0, x1, tol, max_iter):
    """Secant Method"""
    iterations = []
    
    for i in range(1, max_iter + 1):
        f0 = safe_eval(expr, x0)
        f1 = safe_eval(expr, x1)
        
        if abs(f1 - f0) < 1e-14:
            raise ValueError("Division by zero in secant method")
        
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        error = abs(x2 - x1)
        
        iterations.append({
            'iteration': i,
            'x0': f"{x0:.8f}",
            'x1': f"{x1:.8f}",
            'f1': f"{f1:.8e}",
            'error': f"{error:.8e}"
        })
        
        if error < tol or abs(f1) < tol:
            return {
                'root': x2,
                'iterations': iterations,
                'total_iterations': i,
                'final_error': error,
                'fx': safe_eval(expr, x2)
            }
        
        x0, x1 = x1, x2
    
    raise ValueError("Maximum iterations reached without convergence")

def newton_raphson_method(expr, x0, tol, max_iter):
    """Newton-Raphson Method"""
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
            'iteration': i,
            'x': f"{x:.8f}",
            'fx': f"{fx:.8e}",
            'fpx': f"{fpx:.8e}",
            'error': f"{error:.8e}"
        })

        if error < tol or abs(fx) < tol:
            return {
                'root': x_new,
                'iterations': iterations,
                'total_iterations': i,
                'final_error': error,
                'fx': safe_eval(expr, x_new)
            }

        x = x_new

    raise ValueError("Maximum iterations reached without convergence")

def fixed_point_method(expr, g_expr, x0, tol, max_iter):
    """Fixed Point Iteration Method"""
    iterations = []
    x = x0

    for i in range(1, max_iter + 1):
        g_x = safe_eval(g_expr, x)
        fx = safe_eval(expr, x)
        error = abs(g_x - x)

        iterations.append({
            'iteration': i,
            'x': f"{x:.8f}",
            'gx': f"{g_x:.8f}",
            'fx': f"{fx:.8e}",
            'error': f"{error:.8e}"
        })

        if error < tol or abs(fx) < tol:
            return {
                'root': g_x,
                'iterations': iterations,
                'total_iterations': i,
                'final_error': error,
                'fx': safe_eval(expr, g_x)
            }

        x = g_x

    raise ValueError("Maximum iterations reached without convergence")

def modified_secant_method(expr, x0, delta, tol, max_iter):
    """Modified Secant Method"""
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
            'iteration': i,
            'x': f"{x:.8f}",
            'fx': f"{fx:.8e}",
            'fx_delta': f"{fx_delta:.8e}",
            'error': f"{error:.8e}"
        })

        if error < tol or abs(fx) < tol:
            return {
                'root': x_new,
                'iterations': iterations,
                'total_iterations': i,
                'final_error': error,
                'fx': safe_eval(expr, x_new)
            }

        x = x_new

    raise ValueError("Maximum iterations reached without convergence")

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    """Solve the equation using selected method"""
    try:
        data = request.get_json()

        method = data.get('method')
        expr = data.get('equation')
        tol = float(data.get('tolerance', 1e-6))
        max_iter = int(data.get('max_iterations', 100))

        result = None

        if method == 'bisection':
            a = float(data.get('a'))
            b = float(data.get('b'))
            result = bisection_method(expr, a, b, tol, max_iter)

        elif method == 'regula_falsi':
            a = float(data.get('a'))
            b = float(data.get('b'))
            result = regula_falsi_method(expr, a, b, tol, max_iter)

        elif method == 'secant':
            x0 = float(data.get('x0'))
            x1 = float(data.get('x1'))
            result = secant_method(expr, x0, x1, tol, max_iter)

        elif method == 'newton_raphson':
            x0 = float(data.get('x0'))
            result = newton_raphson_method(expr, x0, tol, max_iter)

        elif method == 'fixed_point':
            g_expr = data.get('g_expr')
            x0 = float(data.get('x0'))
            result = fixed_point_method(expr, g_expr, x0, tol, max_iter)

        elif method == 'modified_secant':
            x0 = float(data.get('x0'))
            delta = float(data.get('delta', 0.01))
            result = modified_secant_method(expr, x0, delta, tol, max_iter)

        else:
            return jsonify({'error': 'Invalid method selected'}), 400

        return jsonify({
            'success': True,
            'root': result['root'],
            'iterations': result['iterations'],
            'total_iterations': result['total_iterations'],
            'final_error': result['final_error'],
            'fx': result['fx']
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

