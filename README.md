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

## Homework 3
### Problems Addressed
1. **Patient Temperature Analysis:**
- Reads a CSV file containing patient temperatures and ages.
- Statistical Calculations:
  - Mean, mode, variance, standard deviation, and median for both temperature and age.
  - Prints the results.
- Histograms:
  - Plots the frequency distribution of patient temperatures using Matplotlib.
- Mode Note:
  - The mode of age was manually determined as 73 and 78 after filtering and counting in Excel.

2. **Probability of IQ Over 110:**
  - Given an average IQ of 100 and a standard deviation of 5, calculates the probability of an IQ exceeding 110.
- Calculations:
  - Computes the Z-score for 110.
  - Uses the Z-table to find the cumulative probability and subtracts it from 1.
- Visualization:
  - Plots a bell curve representing the probability distribution.

3. **Probability of Overfilled Cups:**
  - For a cup-fill operation with an average of 16 oz and a standard deviation of 2 oz, calculates the probability of overfilling cups (>18 oz).
- Calculations:
  - Computes the Z-score for 18 oz.
  - Uses the Z-table to determine the probability of overfilling.
- Visualization:
  - Displays the probability distribution with overfilled areas highlighted.

4. **Product Lifetime Promotion:**
  - For a product with an average lifetime of 4000 hours and a standard deviation of 200 hours, calculates the promotion lifetime for the bottom 2% of products.
- Calculations:
  - Uses the Z-score for 2% from the Z-table to compute the lifetime.
- **Visualization**:
  - Plots the bell curve with the promoted lifetime highlighted.

5. **Warranty Calculation:**
  - For a product with an average lifetime of 10 years and a standard deviation of 2 years, calculates the warranty period for the bottom 3%.
- Calculations:
  - Uses the Z-score for 3% from the Z-table to determine the warranty period.
- Visualization:
  - Draws a bell curve with the warranty period highlighted.

### Key Functions and Libraries Used:
1. **NumPy**:
   - For array operations, statistical calculations, and numerical ranges.
2. **SciPy (norm from `scipy.stats`)**:
   - For normal distributions and probability density functions.
3. **Matplotlib**:
   - For plotting histograms and bell curves.
4. **Statistics Module**:
   - For computing mode, variance, standard deviation, and median.
5. **Custom Function (`draw_z_score`)**:
   - Visualizes the Z-score areas on a bell curve.

### **Output:**
The program provides:
- Statistical summaries for temperature and age.
- Probabilities for various scenarios (e.g., IQ, overfilled cups).
- Recommended promotional lifetimes and warranties for products.
- Visualizations (histograms and bell curves) to illustrate the distributions.
