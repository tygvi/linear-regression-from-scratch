# Linear Regression From Scratch 🚀

This repository contains my implementation of Linear Regression from scratch while following Andrew Ng's Machine Learning Specialization.

Instead of using scikit-learn's built-in LinearRegression model, the goal of this project is to understand the mathematics and intuition behind linear regression by implementing the optimization process manually.

---

## Dataset ##

Advertising Dataset

Features:
- TV Advertising Budget

Target:
- Sales

---

## Concepts Implemented

✅ Data Loading with Pandas

✅ Data Visualization with Matplotlib

✅ Cost Function (Mean Squared Error)

✅ Brute Force Search for Optimal Parameters

✅ Manual Optimization of:
- Slope (w)
- Intercept (b)

✅ Best Fit Regression Line Visualization

---

## Linear Regression Model

The model follows the equation:

Sales = w × TV + b

where:

- w = slope
- b = intercept

The objective is to find values of w and b that minimize the cost function.

---

## Cost Function

The optimization objective is:

J(w,b) = (1 / 2m) × Σ(y_pred - y)²

where:

- m = number of training examples
- y_pred = predicted sales
- y = actual sales

---

## Current Approach

This implementation uses a brute-force parameter search:

1. Iterate through possible values of w
2. Iterate through possible values of b
3. Compute the cost function
4. Store the parameters with the lowest cost
5. Plot the resulting regression line

This was done intentionally to build intuition before implementing Gradient Descent.

---

## Future Improvements

Planned additions:

- [ ] Gradient Descent from Scratch
- [ ] Vectorized Implementation using NumPy
- [ ] Multiple Linear Regression
- [ ] Train/Test Split
- [ ] Model Evaluation Metrics
- [ ] Comparison with Scikit-Learn
- [ ] Feature Scaling
- [ ] Cost Function Visualization

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib

---

## Learning Goal

The primary goal of this repository is not to build the most accurate model, but to understand how Linear Regression works internally before relying on machine learning libraries.

This repository will continue to evolve as I progress through the Machine Learning Specialization.
