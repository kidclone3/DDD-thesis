import matplotlib.pyplot as plt
import numpy as np


def read_csv(file_name, type=8):
    """Read csv
    Args:
        file_name (_type_): _description_
        type (int): 3 is run time, 2 is bp explored, 8 is iterations

    Returns:
        _type_: _description_
    """
    with open(file_name, 'r') as f:
        lines = f.readlines()
        data = []
        for line in lines:
            data.append(line.strip())
    # print(data)
    times_data = []
    for i in range(len(data)):
        data[i] = data[i].split(",")
        times_data.append(float(data[i][type]))
        
    return times_data
    

if __name__ == "__main__":
    # type = 2 # bp
    type = 3 # run time
    # type = 8 # iterations
    MIN_time = read_csv("MIN.csv", type)
    MED_time = read_csv("MED.csv", type)
    RAND_time = read_csv("RAND.csv", type)
    # print(MIN_time)
    # read_csv("MED.csv")
    # read_csv("RAND.csv")
    data = [MIN_time, MED_time, RAND_time]
    # Draw 3 boxplots, with name for each is MIN, MED, RAND
    # plt.boxplot(data, labels=['MIN', 'MED', 'RAND'])
    # use dashed line for tail ofboxplot
    # plt.ylabel('Iterations')
    plt.ylabel('Times (ms)')
    # plt.ylabel('BP')
    # plt.xlabel('Groups')
    # draw a diamond not filled for mean value
    # 2 lines of boxplot is dashed line
    plt.boxplot(data, labels=['MIN', 'MED', 'RAND'],
                 whiskerprops=dict(linestyle='--'), 
                 showmeans=True, meanprops={'marker':'D', 'markerfacecolor':'white', 'markeredgecolor':'blue'})

    # Set logarit scale for y axis
    plt.yscale('log')


    plt.show()