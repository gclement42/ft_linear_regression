import utils
import numpy as np
import matplotlib.pyplot as plt

def main():
    data = utils.get_data()
    if not data:
        exit(1)
    learning_rate = 0.01
    theta0 = 0
    theta1 = 0
    plt.ion()
    fig, ax = plt.subplots()
    for i in range(50):
        ax.clear()
        utils.plot_data_and_regression(data, theta0, theta1)
        plt.pause(0.5)
        theta0, theta1 = loss_function(learning_rate, theta0, theta1, data)
    plt.show()

def loss_function(learning_rate, theta0, theta1, data):
    tmp_theta0 = 0
    tmp_theta1 = 0
    m = len(data)
    price = np.array([int(row['price']) for row in data])
    km = np.array([int(row['km']) for row in data])
    predictions = theta0 + theta1 * km
    errors = predictions - price
    tmp_theta0 = (learning_rate / m) * np.sum(errors)
    tmp_theta1 = (learning_rate / m) * np.sum(errors * km)
    theta0 -= tmp_theta0
    theta1 -= tmp_theta1
    return theta0, theta1


main()
    

