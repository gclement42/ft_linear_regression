import utils
import numpy as np
import matplotlib.pyplot as plt
import json

class LinearRegression:
    def __init__(self, learning_rate, a, b, data):
        self.learning_rate = learning_rate
        self.a = a
        self.b = b
        self.prev_a = 0
        self.prev_b = 0
        self.prev_cost = 0
        self._x = np.array([float(row['features']) for row in data])
        self.x = utils.normalisation(self._x)
        self._y = np.array([float(row['target']) for row in data])
        self.y = utils.normalisation(self._y)
        self.m = len(data)
        plt.ion()
        fig, self.ax = plt.subplots()

    def cost_function(self):
        global_cost = 0
        for i in range(0, self.m):
            cost_i = ((self.a + (self.b * self.x[i])) - float(self.y[i])) ** 2
            global_cost += cost_i
        return (1 / (2 * self.m)) * global_cost
    
    def derivative(self):
        d_a = float(0)
        d_b = float(0)
        for i in range(0, self.m):
            d_a += (self.prev_a + (self.prev_b * self.x[i])) - self.y[i]
            d_b += (self.prev_a + (self.prev_b * self.x[i]) - self.y[i]) * self.x[i]
        d_a = (1 / self.m) * d_a
        d_b = (1 / self.m) * d_b
        return d_a, d_b
    
    def gradient_descent(self):
        d_a, d_b = self.derivative()
        self.prev_a = self.a
        self.prev_b = self.b
        self.a = self.prev_a - (self.learning_rate * d_a)
        self.b = self.prev_b - (self.learning_rate * d_b)

    def calc_predictions(self):
        predictions = self.b + (self.a * self.x)
        return predictions
    
    def calc_errors(self, predictions):
        errors = predictions - self.y
        return errors

    def train(self):
        iterations = 0
        while True:
            self.plot_data_and_regression()
            cost = self.cost_function()
            if abs(cost - self.prev_cost) < 0.0000001:
                print(f'Cost function converged after {iterations} iterations with cost: {cost}')
                break
            self.gradient_descent()
            print(f'i: {iterations}, cost: {cost}, a: {self.a}, b: {self.b}')
            iterations += 1
            self.prev_cost = cost
            if iterations > 5000:
                print('Reached maximum number of iterations')
                break
        plt.ioff()
        plt.show()
        print(f'Training completed after {iterations} iterations')
        deltaX = max(self._x) - min(self._x)
        deltaY = max(self._y) - min(self._y)
        t0 = ((deltaY * self.a) + min(self._y) - self.b * (deltaY / deltaX) * min(self._x))
        t1 = deltaY * self.b / deltaX
        with open('params.json', 'w') as f:
            json.dump({'theta0': t0, 'theta1': t1}, f)

    def plot_data_and_regression(self):
        self.ax.clear()
        
        plt.scatter(self.x, self.y)
        x_values = np.linspace(min(self.x), max(self.x), 100)
        y_values = self.a + self.b * x_values
        self.line = plt.plot(x_values, y_values, color='red')
        plt.ylim(0, max(self.y))
        plt.xlabel('km')
        plt.ylabel('price')
        plt.title('Price of cars based on their mileage')
        plt.draw()
        plt.pause(0.1)

model = LinearRegression(0.075, 0, 0, utils.get_data())
model.train()




