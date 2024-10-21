import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Function to solve linear equations
def solve_linear(a, b):
    if a == 0:
        return "No solution (a cannot be 0 for a linear equation)"
    return -b / a

# Function to solve polynomial equations
def solve_polynomial(coefficients):
    x = sp.symbols('x')
    polynomial = sum([coeff * x**i for i, coeff in enumerate(coefficients)])
    solutions = sp.solve(polynomial, x)
    return polynomial, solutions

# Function to plot the equation (linear or polynomial)
def plot_equation(coefficients, solutions, title):
    x_vals = np.linspace(-10, 10, 400)
    y_vals = sum([coeff * x_vals**i for i, coeff in enumerate(coefficients)])
    
    plt.figure(figsize=(6, 4))
    plt.plot(x_vals, y_vals, label=f'{title}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)

    # Highlight the roots if they exist
    if solutions:
        for root in solutions:
            if sp.im(root) == 0:  # Plot only real solutions
                plt.scatter(float(root), 0, color='red')
                plt.text(float(root), 0, f'Root: {float(root):.2f}', color='red', fontsize=10)

    plt.title(f'Graph of {title}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    st.pyplot(plt)

# Streamlit app
st.title("Equation Solver and Visualizer")

# Choose the type of equation
equation_type = st.selectbox("Choose the type of equation", ["Linear", "Polynomial"])

if equation_type == "Linear":
    st.subheader("Solve a Linear Equation (ax + b = 0)")

    # Input for linear equation coefficients
    a = st.number_input("Enter the coefficient a (for x):", value=1.0)
    b = st.number_input("Enter the constant b:", value=0.0)

    # Solve the linear equation
    if a != 0:
        solution = solve_linear(a, b)
        st.write(f"The solution is: x = {solution}")
        
        # Plot the linear equation
        plot_equation([b, a], [solution], f'{a}x + {b} = 0')
    else:
        st.write("Coefficient 'a' cannot be 0 for a linear equation.")
    
elif equation_type == "Polynomial":
    st.subheader("Solve a Polynomial Equation")

    # Input for the degree of the polynomial
    degree = st.number_input("Enter the degree of the polynomial:", min_value=1, value=2, step=1)

    # Input for polynomial coefficients
    coefficients = []
    for i in range(degree, -1, -1):
        coeff = st.number_input(f"Enter the coefficient for x^{i}:", value=0.0)
        coefficients.append(coeff)
    
    coefficients.reverse()  # Reverse to match the correct power order

    # Solve the polynomial equation
    polynomial, solutions = solve_polynomial(coefficients)
    
    st.write(f"The polynomial is: {polynomial} = 0")
    st.write(f"The solutions are: {solutions}")
    
    # Plot the polynomial equation
    plot_equation(coefficients, solutions, f'{polynomial} = 0')
