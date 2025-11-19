# 🧮 Zero of Functions (ZOF) Solver

A comprehensive Python project for solving nonlinear equations using six different numerical methods. This project includes both a Command-Line Interface (CLI) and a modern Web GUI built with Flask.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Numerical Methods](#numerical-methods)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Examples](#examples)
- [Screenshots](#screenshots)

---

## 🎯 Overview

The ZOF Solver is a powerful tool for finding roots (zeros) of nonlinear equations using various numerical methods. It provides:

- **CLI Application**: Interactive command-line interface for quick calculations
- **Web GUI**: Beautiful, responsive web interface built with Flask and Bootstrap
- **Six Numerical Methods**: Multiple algorithms for different use cases
- **Detailed Results**: Iteration tables, convergence analysis, and error tracking

---

## ✨ Features

- ✅ Six different root-finding numerical methods
- ✅ Interactive CLI with input validation
- ✅ Modern web interface with Bootstrap 5
- ✅ Detailed iteration tables for all methods
- ✅ Error handling and convergence checking
- ✅ Support for complex mathematical expressions
- ✅ Real-time calculation and visualization
- ✅ Easy deployment to cloud platforms

---

## 🔢 Numerical Methods

### 1. **Bisection Method**
- **Type**: Bracketing method
- **Requirements**: Two initial guesses (a, b) where f(a) and f(b) have opposite signs
- **Convergence**: Guaranteed but slow (linear)
- **Best for**: Robust root finding when you have a bracket

### 2. **Regula Falsi (False Position) Method**
- **Type**: Bracketing method
- **Requirements**: Two initial guesses (a, b) where f(a) and f(b) have opposite signs
- **Convergence**: Generally faster than bisection
- **Best for**: When you need guaranteed convergence with better speed

### 3. **Secant Method**
- **Type**: Open method
- **Requirements**: Two initial guesses (x₀, x₁)
- **Convergence**: Superlinear (order ~1.618)
- **Best for**: When derivative is difficult to compute

### 4. **Newton-Raphson Method**
- **Type**: Open method
- **Requirements**: One initial guess (x₀)
- **Convergence**: Quadratic (very fast)
- **Best for**: When good initial guess is available and function is smooth

### 5. **Fixed Point Iteration Method**
- **Type**: Open method
- **Requirements**: Rearrange f(x) = 0 to x = g(x), one initial guess
- **Convergence**: Depends on |g'(x)| < 1
- **Best for**: When equation can be easily rearranged

### 6. **Modified Secant Method**
- **Type**: Open method
- **Requirements**: One initial guess (x₀) and delta (δ)
- **Convergence**: Similar to secant method
- **Best for**: When only one initial point is available

---

## 📁 Project Structure

```
ZOF_Project/
│
├── ZOF_CLI.py                 # Command-line interface application
├── app.py                     # Flask web application
├── requirements.txt           # Python dependencies
├── ZOF_hosted_webGUI_link.txt # Deployment information
├── README.md                  # This file
│
├── templates/
│   └── index.html            # Web GUI HTML template
│
└── static/
    └── style.css             # Custom CSS styling
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download the Project

```bash
cd ZOF_Project
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 💻 Usage

### Running the CLI Application

```bash
python ZOF_CLI.py
```

**Example Session:**

```
================================================================================
                    ZERO OF FUNCTIONS (ZOF) SOLVER
                         Numerical Methods CLI
================================================================================

Available Methods:
1. Bisection Method
2. Regula Falsi (False Position) Method
3. Secant Method
4. Newton-Raphson Method
5. Fixed Point Iteration Method
6. Modified Secant Method

Select method (1-6): 1

Enter the equation f(x) = 0
Example: x**3 - x - 2  or  math.exp(x) - 3*x
f(x) = x**3 - x - 2
Enter tolerance (default 1e-6): 0.0001
Enter maximum iterations (default 100): 50
Enter lower bound a: 1
Enter upper bound b: 2
```

### Running the Web GUI

```bash
python app.py
```

Then open your browser and navigate to:
```
http://localhost:5000
```

---

## 🌐 Deployment

### Option 1: Deploy to Render

1. Create a free account at [Render.com](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Add `gunicorn` to requirements.txt:
   ```bash
   echo "gunicorn==21.2.0" >> requirements.txt
   ```

### Option 2: Deploy to PythonAnywhere

1. Create account at [PythonAnywhere.com](https://www.pythonanywhere.com)
2. Upload project files via Files tab
3. Create new web app (Flask)
4. Configure WSGI file to point to `app.py`
5. Reload web app

### Option 3: Deploy to Heroku

1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: gunicorn app:app
   ```
3. Deploy:
   ```bash
   heroku login
   heroku create zof-solver
   git push heroku main
   ```

---

## 📊 Examples

### Example 1: Solving x³ - x - 2 = 0

**Using CLI (Bisection Method):**
- Equation: `x**3 - x - 2`
- Method: Bisection
- Initial interval: [1, 2]
- Tolerance: 1e-6

**Expected Result:**
- Root: x ≈ 1.521379707
- Iterations: ~20

### Example 2: Solving e^x - 3x = 0

**Using Web GUI (Newton-Raphson):**
- Equation: `math.exp(x) - 3*x`
- Method: Newton-Raphson
- Initial guess: 1.5
- Tolerance: 1e-6

**Expected Result:**
- Root: x ≈ 1.512134551
- Iterations: ~5

### Example 3: Solving x² - 2 = 0 (Finding √2)

**Using Fixed Point Method:**
- Equation: `x**2 - 2`
- g(x): `math.sqrt(2)` or `2/x`
- Initial guess: 1.5
- Tolerance: 1e-6

**Expected Result:**
- Root: x ≈ 1.414213562
- Iterations: varies

---

## 📸 Screenshots

### CLI Interface
```
[Screenshot placeholder - CLI showing iteration table]
```

### Web GUI - Input Form
```
[Screenshot placeholder - Web form with method selection]
```

### Web GUI - Results
```
[Screenshot placeholder - Results with iteration table]
```

---

## 🛠️ Technical Details

### Dependencies

- **Flask**: Web framework for the GUI
- **sympy**: Symbolic mathematics (optional, for advanced features)
- **numpy**: Numerical computations (optional, for enhanced calculations)

### Mathematical Expression Syntax

The solver supports standard Python mathematical expressions:

- **Basic operators**: `+`, `-`, `*`, `/`, `**` (power)
- **Math functions**: `math.sin()`, `math.cos()`, `math.tan()`
- **Exponential**: `math.exp()`, `math.log()`
- **Square root**: `math.sqrt()`
- **Constants**: `math.pi`, `math.e`

**Examples:**
- `x**2 - 4`
- `math.sin(x) - 0.5`
- `math.exp(x) - x**2`
- `x**3 - 2*x - 5`

---

## ⚠️ Important Notes

### Convergence Criteria

All methods stop when either:
1. Error < Tolerance
2. |f(x)| < Tolerance
3. Maximum iterations reached

### Input Validation

- The CLI validates all numeric inputs
- The Web GUI provides client-side and server-side validation
- Invalid expressions are caught and reported

### Method Selection Guidelines

| Method | Speed | Reliability | Initial Guesses | Derivative Needed |
|--------|-------|-------------|-----------------|-------------------|
| Bisection | Slow | Very High | 2 (bracket) | No |
| Regula Falsi | Medium | High | 2 (bracket) | No |
| Secant | Fast | Medium | 2 | No |
| Newton-Raphson | Very Fast | Medium | 1 | Yes (auto) |
| Fixed Point | Varies | Low | 1 | No |
| Modified Secant | Fast | Medium | 1 | No |

---

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

---

## 📝 License

This project is open-source and available for educational purposes.

---

## 👨‍💻 Author

**Name**: [Your Name]  
**Matric Number**: [Your Matric Number]  
**Contact**: [Your Email]

---

## 🙏 Acknowledgments

- Numerical methods theory from standard numerical analysis textbooks
- Flask documentation and community
- Bootstrap for the beautiful UI components

---

**Happy Computing! 🎉**

