import utils
import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self, learning_rate, a, b, data):
        self.learning_rate = learning_rate
        self.a = a
        self.b = b
        self.prev_a = 0
        self.prev_b = 0
        self.x = np.array([int(row['features']) for row in data])
        self.y = np.array([int(row['target']) for row in data])
        self.m = len(data)
        plt.ion()
        fig, self.ax = plt.subplots()

    def cost_function(self, predictions):
        errors = self.calc_errors(predictions)
        cost = (1 / (2 * self.m)) * np.sum(np.power(errors, 2))
        return cost
    
    def derivative(self):
        d_a = float(0)
        d_b = float(0)
        for i in range(0, self.m):
            d_a += float(((self.prev_a + self.prev_b * self.x[i]) - self.y[i]))
            d_b += (((self.prev_a + self.prev_b * self.x[i]) - self.y[i]) * self.x[i])
        d_a = (1 / self.m) * d_a
        d_b = (1 / self.m) * d_b
        return d_a, d_b
    
    def gradient_descent(self):
        d_a, d_b = self.derivative()
        self.a = self.prev_a - (self.learning_rate * d_a)
        self.b = self.prev_b - (self.learning_rate * d_b)
        self.prev_a = self.a
        self.prev_b = self.b

    def calc_predictions(self):
        predictions = self.b + (self.a * self.x)
        return predictions
    
    def calc_errors(self, predictions):
        errors = predictions - self.y
        return errors

    
    def train(self):
        cost = 11
        iterations = 0
        while cost > 10:
            self.plot_data_and_regression()
            predictions = self.calc_predictions()
            cost = self.cost_function(predictions)
            self.gradient_descent()
            print(f'i: {iterations}, cost: {cost}, a: {self.a}, b: {self.b}')
            iterations += 1
            if iterations > 100:
                print('Reached maximum number of iterations')
                break
        plt.ioff()
        plt.show()
        print(f'Training completed after {iterations} iterations')

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

model = LinearRegression(0.0001, 0, 0, utils.get_data())
model.train()




