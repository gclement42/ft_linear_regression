import os
import csv
import numpy as np
import matplotlib.pyplot as plt

def check_if_file_is_readable():
    if not os.path.exists('data.csv') or not os.access('data.csv', os.R_OK):
        print('data.csv does not exist or is not readable')
        return False
    return True

def get_data():
    if not check_if_file_is_readable():
        return None
    
    data = []
    with open('data.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            row = { 'km': row[0], 'price': row[1] }
            data.append(row)
    return data

def plot_data_and_regression(data, theta0, theta1):
    x = [int(row['km']) for row in data]
    y = [int(row['price']) for row in data]
    plt.scatter(x, y)
    x_values = np.linspace(min(x), max(x), 1000)
    y_values = theta0 + theta1 * x_values
    plt.plot(x_values, y_values, color='red')
    plt.xlabel('km')
    plt.ylabel('price')
    plt.title('Price of cars based on their mileage')
    y_min, y_max = plt.ylim()
    plt.yticks(np.arange(y_min, y_max, 500))
    plt.show()

def plot_linear_regression(x, y):
    plt.plot(x, y)
    plt.show()