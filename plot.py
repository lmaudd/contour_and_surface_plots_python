import numpy as np
import matplotlib.pyplot as plt
from matplotlib import projections
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch

def cplot(function, xmin=-5, xmax=5, ymin=-5, ymax=5):
    
    """
    |––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––|
    | CONTOUR PLOT                                                           |
    |                                                                        |
    | function: input function in terms of X and Y. Wrap in quotation marks. |
    | Bounds default to (-5, 5), x and y.                                    |
    |––––––––––––––––––––––––––––––––––––––––––––––––––––––––––-–––––––––––––|
    """

    # Bounds
    x = np.linspace(xmin, xmax, 500)
    y = np.linspace(ymin, ymax, 500)

    # Function
    X, Y = np.meshgrid(x,y)
    Z = eval(function)

    # Plot
    plt.contourf(X, Y, Z, levels = 25)
    plt.colorbar()

def splot(function, xmin=-5, xmax=5, ymin=-5, ymax=5):
    
    """
    |––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––|
    | SURFACE PLOT                                                           |
    |                                                                        |
    | function: input function in terms of X and Y. Wrap in quotation marks. |
    | Bounds default to (-5, 5), x and y.                                    |
    |––––––––––––––––––––––––––––––––––––––––––––––––––––––––––-–––––––––––––|
    """
    
    # Bounds
    x = np.linspace(xmin, xmax, 500)
    y = np.linspace(ymin, ymax, 500)

    # Function
    X, Y = np.meshgrid(x,y)
    Z = eval(function)

    # Plot
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, cmap='ocean')
    plt.show

"""
––––––––––––––––––––––––––––––––––––––––––––––––––––––
x = np.linspace(-3, 3, 10)
y = np.linspace(-3, 3, 10)

X, Y = np.meshgrid(x,y)

Z = 3*X*Y / (np.e**(X**2 + Y**2))
z = 3*x*y / (np.e**(x**2 + y**2))

def change(X,Y): # Determine vector from grad function??????
    
    U = np.gradient(z)[0]
    V = np.gradient(z)[1]
    
    return [U,V]
    
    
U, V = change(X, Y)
    
plt.quiver(X,Y,U,V)

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

x = np.arange(-3, 3, 0.5)
y = np.arange(-3, 3, 0.5)
X, Y = np.meshgrid(x, y)

Z = 3*X*Y / (np.e**(X**2 + Y**2))



U = np.gradient(Z)[1]
V = np.gradient(Z)[0]


plt.quiver(X, Y, U, V)
plt.show()
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––-----––----------------------
"""