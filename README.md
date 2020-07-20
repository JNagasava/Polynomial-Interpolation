# Polynomial Interpolation

## Introduction
Python application which makes graphs interpolating functions (and splines) from python functions or csv files.

<img src="./assets/function.gif">

<img src="./assets/csv.gif">

## Motivation
An interpolation function can be used to know unknown values in a data set. There are different ways to find these values.

## Methods
Each point (x, y) of the data set can be interpreted by the following equation:

<img src="./assets/polynomial_equation.png">

### Linear System
To find the "a" coefficients, we can use a linear system:

<img src="./assets/linear_system.png">

### Lagrange

Another more efficient method than using linear system, is the lagrange method:

<img src="./assets/lagrange.png">

The cofficient can be obtained from:

<img src="./assets/lagrange_l.png">

### Newton
The biggest problem with the Lagrange method is when a new value (x, y) is added, the polynomial function has to be rewritten. To solve this problem, we can use the newton method.

<img src="./assets/newton.png">

The cofficient can be obtained by divided differences:

<img src="./assets/newton_f.png">

## Splines

The previous methods help a lot to "estimate" data. But they are "inefficient" for a large data set (polynomial degree gets too large) and functions with uniform distribution (for example: Runge Function). To solve this, we can make polynomial functions between each two nodes.

### Linear Spline

Linear splines makes a straight line for every two nodes

<img src="./assets/linear_spline.png">

### Cubic Spline

Cubic splines have a third degree k-equation for every two nodes

<img src="./assets/cubic_spline.png">

The cofficients can be obtained from:

<img src="./assets/cubic_spline_a.png">

<img src="./assets/cubic_spline_b.png">

<img src="./assets/cubic_spline_c.png">

<img src="./assets/cubic_spline_d.png">

<img src="./assets/cubic_spline_h.png">

for <img src="./assets/cubic_spline_k.png">

From the list of equations above, we have:

<img src="./assets/cubic_spline_A.png">

<img src="./assets/cubic_spline_x.png">

<img src="./assets/cubic_spline_bb.png">

<img src="./assets/Axb.png">

## The Application

### Function

### CSV File

## Resources and Tools

https://convertio.co/pt/mkv-gif/

https://plotly.com/

https://hackmd.io/

https://www.codecogs.com/latex/eqneditor.php?lang=pt-br









