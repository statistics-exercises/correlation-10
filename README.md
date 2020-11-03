# Generating linearly correlated random variables

You should have found that the idea in the last exercise was the same.  In the new exercise, the coefficient of the X in the expression for the random variable is increased.  You thus have:

![](https://render.githubusercontent.com/render/math?math=Y=2X%2B\frac{1}{2}\delta)

as opposed to the:

![](https://render.githubusercontent.com/render/math?math=Y=X%2B\delta)

that you had in the first of these two exercises.  In these expressions Y is the random variable that is plotted on the y-axis and X is the random variable that is plotted on the X axis.  X is a uniform random variable that falls between 0 and 1.  ![](https://render.githubusercontent.com/render/math?math=\delta) meanwhile is a uniform random variable that falls between -1 and +1. ![](https://render.githubusercontent.com/render/math?math=\delta) is thus generated as:

````
delta = -0.5 + np.random.uniform(0,1) 
````

If you press run in the panel on the left you will see that this exercise generates yet another set of lines that you must generate points between.  In this case the equations of the lines are:

y = x + 1 

y = x + 3

As always your task is to generate 100 random points that fall between these lines.  Furthermore, as in the previous tasks you should not need to use conditional (if) statements in order to achieve this.

