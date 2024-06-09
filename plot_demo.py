import matplotlib.pyplot as plt


if __name__ == "__main__":
    # Sample data
    nodes = [0, 1, 3]
    time = [0, 1.34, 2.5674]

    # Create the plot
    plt.figure(figsize=(6, 4))  # Set the figure size
    plt.scatter(nodes, time)  # Create a scatter plot

    # Set axis labels and title
    plt.xlabel("Node")
    plt.ylabel("Time")
    plt.title("Sample Plot")

    # Using arrow to connect nodes[0] and nodes[1], using slight offset for better visibility
    # Reduce the linewidth and change the color to green
    # Set the arrow to middle of the line
    plt.annotate("", xy=(nodes[1], time[1]), xytext=(nodes[0], time[0]),
                 arrowprops=dict(arrowstyle="->", color="green", lw=1), xycoords='data', textcoords='data')
    
    # Display the plot
    plt.grid(True)  # Add a grid
    plt.show()
    