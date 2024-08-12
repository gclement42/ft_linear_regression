import os
import csv
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

def plot_data(data):
    x = [int(row['km']) for row in data]
    y = [int(row['price']) for row in data]
    plt.scatter(x, y)
    plt.xlabel('km')
    plt.ylabel('price')
    plt.title('Price of cars based on their mileage')
    plt.show()