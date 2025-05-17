# Experimental-Physics-and-Engineering-Lab-2
Collection of exercises from the Experimental Physics and Engineering Lab 2: Mechanics class (ENGR-216) in the College of Engineering at Texas A&amp;M University

## Homework 2
### Problems Addressed:
1. **Matrix Operations (Problem 1):**
   - Performs operations such as addition, scalar multiplication, and subtraction on two given matrices \( A_1 \) and \( B_1 \).
   - Verifies the results programmatically.

2. **Matrix Multiplication (Problem 2):**
   - Multiplies two matrices \( A_2 \) and \( B_2 \), showing that \( B_2 \cdot A_2 \) cannot be computed due to incompatible dimensions.

3. **Matrix Properties (Problem 3):**
   - Multiplies two matrices \( A_3 \) and \( B_3 \), demonstrating that their product results in the identity matrix.
   - Concludes that \( A_3 \) and \( B_3 \) are inverses of each other.

4. **Linear Equation System (Problem 4):**
   - Solves a system of three linear equations using NumPy's `solve()` function.
   - Verifies the solution by re-computing \( A \cdot x \).
   - Computes the inverse of matrix \( A \) and demonstrates that \( A^{-1} \cdot b \) also produces the solution \( x \).

5. **Linear Equation System (Problem 5):**
   - Solves a system of four linear equations with four variables using NumPy's linear algebra tools.
   - Verifies the solution and computes the inverse of \( A \) for comparison.

### Key Concepts Covered:
- Matrix addition, subtraction, and scalar multiplication.
- Matrix multiplication and dimensional compatibility.
- Linear equation solving using `numpy.linalg.solve`.
- Matrix inversion and the relationship between \( A^{-1} \cdot b \) and solutions of linear equations.

### Output:
The script displays the results of each operation and verifies them where possible. It also comments on undefined operations due to dimensional incompatibility.
