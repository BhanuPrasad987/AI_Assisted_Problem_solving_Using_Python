#Write python code to find value of x at which the function f(x)=2X3+4x+5 will be minimum
import sympy as sp

x = sp.symbols('x')
f = 2*x**3 + 4*x + 5
# derivative
f_prime = sp.diff(f, x)
# solve derivative
critical_points = sp.solve(f_prime, x)
print("Critical points:", critical_points)
# Check if any are real
real_points = [cp for cp in critical_points if cp.is_real]

if real_points:
    print("Minimum occurs at:", real_points)
else:
    print("The function has no real minimum.")

