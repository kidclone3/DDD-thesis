# Using mathplotlib to plot the data

import matplotlib.pyplot as plt
import numpy as np

# Given 3 functions and range, plot the functions
def plot_functions(f1, f2, f3, f4="", f5="", name=""):
    x1 = np.linspace(0, 1, 20)
    x2 = np.linspace(1, 2, 20)
    
    y1 = f1(x1)
    y2 = f2(x2)
    plt.plot(x1, y1, color='orange')
    plt.plot(x2, y2, color='orange')

    if f4 == "" and f5 == "":
        x3 = np.linspace(2, 5, 60)
        
    else: 
        x3 = np.linspace(2, 3, 20)
        x4 = np.linspace(3, 4, 20)
        x5 = np.linspace(4, 5, 20)
    
        y4 = f4(x4)
        y5 = f5(x5)
        plt.plot(x4, y4, color='orange')
        plt.plot(x5, y5, color='orange')

    y3 = f3(x3)
    plt.plot(x3, y3, color='orange')
    
    # Add labels
    plt.xlabel('Time')
    plt.ylabel('Travel Time')
    # Add title, and bold the title
    plt.title(f'Travel Time of {name}', fontweight='bold')
    plt.ylim(0, 3.2)
    plt.xlim(0, 5)
    plt.show()

if __name__ == '__main__':
    # Arc (1,2)
    # f1 = lambda t: 1.34 - 0.68 *t
    # f2 = lambda t: 1.18 - 0.52 *t
    # f3 = lambda t: 0.4 - 0.13 * t
    # f4 = lambda t: -1.01+0.34*t
    # f5 = lambda t: -2.25+0.65*t

    # Arc (1,3)
    # name = "Arc (1,3)"
    # f1 = lambda t: 2.85 + 0.10*t
    # f2 = lambda t: 2.90 + 0.05*t
    # f3 = lambda t: 3.04 - 0.02*t
    # f4 = lambda t: 3.22 - 0.08*t
    # f5 = lambda t: 3.46 - 0.14*t

    # Arc (2,3)
    # name = "Arc (2,3)"
    # f1 = lambda t: 1.99 - 0.17*t
    # f2 = lambda t: 2.13 - 0.31*t
    # f3 = lambda t: 2.33 - 0.41*t
    # f4 = lambda t: 2.39 - 0.43*t
    # f5 = lambda t: 2.15 - 0.37*t
    
    # Arc (2,4)
    # name="Arc (2,4)"
    # f1 = lambda t: 1.29 - 0.27*t
    # f2 = lambda t: 0.41 + 0.61*t
    # f3 = lambda t: -0.25 + 0.94*t
    # f4 = lambda t: 1.28 + 0.43*t
    # f5 = lambda t: 4.84 - 0.46*t

    # Arc (3,4)
    name = "Arc (3,4)"
    f1 = lambda t: 0.61 + 0.12*t
    f2 = lambda t: 0.63 + 0.10 *t
    f3 = lambda t: 0.72 + 0.06*t
    f4 = ""
    f5 = ""
    plot_functions(f1, f2, f3, f4, f5, name)