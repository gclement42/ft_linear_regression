import utils
import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self, learning_rate, a, b, data):
        self.learning_rate = learning_rate
        self.a = a
        self.b = b
        self.prev_a = a
        self.prev_b = b
        self.x = np.array([int(row['features']) for row in data])
        self.y = np.array([int(row['target']) for row in data])
        self.m = len(data)
        plt.ion()
        fig, self.ax = plt.subplots()

    def cost_function(self, predictions):
        error = np.sum(predictions - self.y)
        cost = 1 / (2 * self.m) * np.sum(error ** 2)
        return cost
    
    def gradient_descent(self, predictions):
        errors = predictions - self.y
        tmp_a = self.prev_a - (1 / self.m) * (self.learning_rate * np.sum(errors))
        tmp_b = self.prev_b - (1 / self.m) * (self.learning_rate * np.sum(errors * self.x))
        print(f'tmp_a: {tmp_a}, tmp_b: {tmp_b}')
        self.prev_a = self.a
        self.prev_b = self.b
        self.a = tmp_a
        self.b = tmp_b
    
    def train(self):
        for _ in range(20):
            self.plot_data_and_regression()
            predictions = self.a * self.x + self.b
            cost = self.cost_function(predictions)
            self.gradient_descent(predictions)
            # print(f'cost: {cost}')
            plt.show()

    def plot_data_and_regression(self):
        self.ax.clear()
        
        plt.scatter(self.x, self.y)
        x_values = np.linspace(min(self.x), max(self.x), 100)
        y_values = self.a * x_values + self.b
        plt.plot(x_values, y_values, color='red')
        plt.xlabel('km')
        plt.ylabel('price')
        plt.title('Price of cars based on their mileage')
        plt.draw()
        plt.pause(0.1)

# def loss_function(learning_rate, theta0, theta1, data):
#     m = len(data)
#     price = np.array([int(row['target']) for row in data])
#     km = np.array([int(row['features']) for row in data])
#     predictions = theta0 + theta1 * km
#     errors = predictions - price
#     tmp_theta0 = theta0 - learning_rate * (1 / m) * np.sum(errors)
#     tmp_theta1 = theta1 - learning_rate * (1 / m) * np.sum(errors * km)
#     print(f'tmp_theta0: {tmp_theta0}, tmp_theta1: {tmp_theta1}')
#     theta0 -= tmp_theta0
#     theta1 -= tmp_theta1
#     return theta0, theta1

model = LinearRegression(0.000001, 0, 0, utils.get_data())
model.train()




