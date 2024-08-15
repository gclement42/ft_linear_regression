import utils
import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self, learning_rate, a, b, data):
        self.learning_rate = learning_rate
        self.a = a
        self.b = b
        self.x = np.array([int(row['features']) for row in data])
        self.y = np.array([int(row['target']) for row in data])
        self.m = len(data)
        plt.ion()
        fig, self.ax = plt.subplots()

    def cost_function(self, predictions):
        error = np.mean(predictions - self.y)
        cost = 1 / (2 * self.m) * np.mean(error ** 2)
        return cost
    
    def derivative(self):
        predictions = self.calc_predictions()
        errors = np.mean(predictions - self.y)
        d_a = (1 / self.m) * np.mean(np.multiply(errors, self.x))
        d_b = (1 / self.m) * np.mean(errors)
        print(f'd_a: {d_a}, d_b: {d_b}')
        return d_a, d_b
    
    def gradient_descent(self):
        predictions = self.calc_predictions()
        errors = np.mean(predictions - self.y)
        self.a = self.a - self.learning_rate * np.multiply((1 / self.m), np.sum(errors))
        self.b = self.b - self.learning_rate * np.multiply((1 / self.m), np.mean(np.multiply(errors, self.x)))

    def calc_predictions(self):
        predictions = np.multiply(self.a, np.mean(self.x)) + self.b
        return predictions
    
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
        x_values = np.linspace(min(self.x), max(self.x), self.m)
        y_values = self.a * x_values + self.b
        self.line = plt.plot(x_values, y_values, color='red')
        plt.ylim(0, max(self.y))
        plt.xlabel('km')
        plt.ylabel('price')
        plt.title('Price of cars based on their mileage')
        plt.draw()
        plt.pause(0.1)

model = LinearRegression(0.00001, 0, 0, utils.get_data())
model.train()




