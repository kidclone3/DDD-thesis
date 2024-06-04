# Using mathplotlib to plot the data

import matplotlib.pyplot as plt
import numpy as np

# Given 3 functions and range, plot the functions
def plot_functions(f1, f2, f3, f4="", f5="", name=""):
    x1 = np.linspace(0, 1, 20)
    x2 = np.linspace(1, 2, 20)
    color = 'cornflowerblue'
    y1 = f1(x1)
    y2 = f2(x2)
    plt.plot(x1, y1, color=color)
    plt.plot(x2, y2, color=color)

    if f4 == "" and f5 == "":
        x3 = np.linspace(2, 5, 60)
        print(f3(3))
        print(f3(4))
        
    else: 
        x3 = np.linspace(2, 3, 20)
        x4 = np.linspace(3, 4, 20)
        x5 = np.linspace(4, 5, 20)
    
        y4 = f4(x4)
        y5 = f5(x5)
        plt.plot(x4, y4, color=color)
        plt.plot(x5, y5, color=color)

    y3 = f3(x3)
    plt.plot(x3, y3, color=color)
    
    # Add labels
    plt.xlabel('Time')
    plt.ylabel('Travel Time')
    # Add title, and bold the title
    plt.title(f'Travel Time of {name}', fontweight='bold')
    plt.ylim(0, 3.2)
    plt.xlim(0, 5)
    
    # plt.show()
    # save plot
    plt.savefig(f'/Users/delus/Documents/projects/school/DDD-thesis/sections/plot/{name}.png')

def line_plot():
    ddd = [49.7, 66.5, 32.8, 34.2, 33.7, 45.7, 115.6, 126.8, 63.7, 68.7, 116.9, 98.4]
    enums = [774.7, 856.2, 474.9, 515.4, 621.1, 667.4, 2375.9, 2496.5, 1352.1, 1461.1, 1934.2, 2043.5]
    x = np.linspace(0, 12, 12)
    plt.plot(x, ddd, color='orange')
    plt.plot(x, enums, color='blue')
    plt.xlabel('Time')
    plt.ylabel('Travel Time')
    # Add title, and bold the title
    plt.title(f'Travel Time of Arc (1,2)', fontweight='bold')
    # exp plot
    plt.yscale('log')
    plt.xlim(0, 12)
    plt.show()

def example_plot():

    # Data
    col1 = [
        49.7,

        66.5,

        32.8,

        34.2,

        33.7,

        45.7,

        115.6,

        126.8,

        63.7,

        68.7,

        116.9,

        98.4]
    col2 = [
        774.7,
        856.2,

        474.9,
        515.4,

        621.1,
        667.4,

        2375.9,
        2496.5,

        1352.1,
        1461.1,

        1934.2,
        2043.5]
    percent = [
        6.4,

        7.8,

        6.9,

        6.6,

        5.4,

        6.8,

        4.9,

        5.1,

        4.7,

        4.7,

        6.0,

        4.8,
    ]
    percent_orig = percent[::]
    percent = [x*100 for x in percent]

    # Data
    countries = [
        "(30, 1, 1)",
        "(30, 1, 2)",
        "(30, 2, 1)",
        "(30, 2, 2)",
        "(30, 3, 1)",
        "(30, 3, 2)",
        "(50, 1, 1)",
        "(50, 1, 2)",
        "(50, 2, 1)",
        "(50, 2, 2)",
        "(50, 3, 1)",
        "(50, 3, 2)"
    ]

    # Create a double bar chart
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    bar_width = 0.35

    index = range(len(col1))
    plt.bar(index, col1, bar_width, label='DDD', color='teal')
    plt.bar([i + bar_width for i in index], col2, bar_width, label='Enum', color="lightgreen")

    # Draw a dot and line plot for the percentage data, with the point in center of the bars
    plt.plot([i + bar_width/2 for i in index], percent, marker='o', color='green', label='Phần trăm DDD/Enum')

    # Show the percentage data on top of the bars
    for i, v in enumerate(percent_orig):
        plt.text(i + bar_width/2, v + 100 + percent[i], str(v)+"%", ha='center', va='bottom')



    # Set axis labels and title, bold the title
    plt.xlabel("Các bộ ba (n, g-type, t-type)", fontsize=12, fontweight='bold')
    plt.ylabel("Thời gian (ms)", fontsize=12, fontweight='bold')
    plt.title("So sánh thời gian của DDD và Enum", fontsize=16, fontweight='bold')

    # Add data labels (optional)
    # You can uncomment this section to add data labels to the bars
    # for i, (v1, v2) in enumerate(zip(visitors_2022, visitors_2023)):
    #     plt.text(i - bar_width/2, v1 + 20000, str(v1), ha='center', va='bottom')
    #     plt.text(i + bar_width/2, v2 + 20000, str(v2), ha='center', va='bottom')

    # Customize the plot
    plt.xticks([i + bar_width/2 for i in index], countries, rotation=45)  # Rotate x-axis labels for better readability
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # # use log scale
    # plt.yscale('log')

    # Show the plot
    plt.tight_layout()
    plt.show()

    # Show the plot
    plt.show()
    # Save plot to file
    # plt.savefig('double_bar_chart.png', dpi=300)


if __name__ == '__main__':
    # Arc (1,2)
    # name = "Arc (1,2)"
    # f1 = lambda t: 1.34 - 0.68 *t
    # f2 = lambda t: 1.18 - 0.52 *t
    # f3 = lambda t: 0.4 - 0.13 * t
    # f4 = lambda t: -1.01+0.34*t
    # f5 = lambda t: -2.25+0.65*t

    # Arc (1,3)
    name = "Arc (1,3)"
    f1 = lambda t: 2.85 + 0.10*t
    f2 = lambda t: 2.90 + 0.05*t
    f3 = lambda t: 3.04 - 0.02*t
    f4 = lambda t: 3.22 - 0.08*t
    f5 = lambda t: 3.46 - 0.14*t

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

    # # Arc (3,4)
    # name = "Arc (3,4)"
    # f1 = lambda t: 0.61 + 0.12*t
    # f2 = lambda t: 0.63 + 0.10 *t
    # f3 = lambda t: 0.72 + 0.06*t
    # f4 = ""
    # f5 = ""
    plot_functions(f1, f2, f3, f4, f5, name)

    # line_plot()
    # example_plot()
    # example_plot2()