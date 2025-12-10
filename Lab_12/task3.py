#Write python code to solve below case study using linear optimization
'''Consider a chocolate manufacturing company that produces only two types of chocolate i.e. A and B.\
 Both the chocolates require Milk and Choco only.
To manufacture each unit of A and B, the following quantities are required:
Each unit of A requires 1 unit of Milk and 3 units of Choco
Each unit of B requires 1 unit of Milk and 2 units of Choco
The company kitchen has a total of 5 units of Milk and 12 units of Choco.
On each sale, the company makes a profit of Rs 6 per unit A sold and Rs 5 per unit B sold.
Now, the company wishes to maximize its profit. How many units of A and B should it produce respectively?'''

from scipy.optimize import linprog
# Coefficients for the objective function (negative for maximization)
c = [-6, -5]  # Profit coefficients for A and B
# Coefficients for the inequality constraints
A = [
    [1, 1],   # Milk constraint
    [3, 2]    # Choco constraint
]
# Right-hand side of the inequality constraints
b = [5, 12]  # Available resources: 5 units of Milk and 12 units of Choco
# Bounds for each variable (units of A and B cannot be negative)
x0_bounds = (0, None)  # Bounds for units of A
x1_bounds = (0, None)  # Bounds for units of B  
# Solve the linear programming problem
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')
# Print the results
if res.success:
    print(f"Units of A to produce: {res.x[0]:.2f}")
    print(f"Units of B to produce: {res.x[1]:.2f}")
    print(f"Maximum Profit: Rs {-res.fun:.2f}")
else:
    print("No solution found")

