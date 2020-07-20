# Polynomial Interpolation

## Introduction
Python application which makes graphs interpolating functions (and splines) from python functions or csv files.

![](https://i.imgur.com/HcDZxu5.gif)

![](https://i.imgur.com/ehYHIcY.gif)

## Motivation
An interpolation function can be used to know unknown values in a data set. There are different ways to find these values.

## Methods
Each point (x, y) of the data set can be interpreted by the following equation:

![](https://i.imgur.com/WlHKxoa.png)

### Linear System
To find the "a" coefficients, we can use a linear system:

![](https://i.imgur.com/o0qtSNW.png)


### Lagrange

Another more efficient method than using linear system, is the lagrange method:

![](https://i.imgur.com/AHqFBgh.png)

The cofficient can be obtained from:

![](https://i.imgur.com/pqNmyQ0.png)

### Newton
The biggest problem with the Lagrange method is when a new value (x, y) is added, the polynomial function has to be rewritten. To solve this problem, we can use the newton method.

![](https://i.imgur.com/UqFkMuv.png)

The cofficient can be obtained by divided differences:

![](https://i.imgur.com/NvGBpEk.png)

## Splines

The previous methods help a lot to "estimate" data. But they are "inefficient" for a large data set (polynomial degree gets too large) and functions with uniform distribution (for example: Runge Function). To solve this, we can make polynomial functions between each two nodes.

### Linear Spline

Linear splines makes a straight line for every two nodes

### Cubic Spline

Cubic splines have a third degree k-equation for every two nodes

![](https://i.imgur.com/6ZwXHs8.png)

The cofficients can be obtained from:

![](https://i.imgur.com/eUGV8b4.png)

![](https://i.imgur.com/v0J42tE.png)

![](https://i.imgur.com/qC9ATV7.png)

![](https://i.imgur.com/niqmEeO.png)

![](https://i.imgur.com/p52SKkd.png)

for ![](https://i.imgur.com/QaAA9r5.png)

From the list of equations above, we have:

![](https://i.imgur.com/Qi9KwOp.png)

![](https://i.imgur.com/HGUkgdo.png)

![](https://i.imgur.com/9nxV0kB.png)

![](https://i.imgur.com/ObkWS6L.png)

## The Application

### Function

### CSV File

## Resources and Tools

https://convertio.co/pt/mkv-gif/

https://plotly.com/

https://hackmd.io/

https://www.codecogs.com/latex/eqneditor.php?lang=pt-br









