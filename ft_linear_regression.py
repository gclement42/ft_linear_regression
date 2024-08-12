import utils

def linear_function(x, theta0, theta1):
    return theta0 * x + theta1

def main():
    data = utils.get_data()
    if not data:
        exit(1)
    x = [int(row['price']) for row in data]
    x = sum(x) / len(x)
    y = linear_function(x, 0, 0)

    utils.plot_data(data, x, y)

main()
    

