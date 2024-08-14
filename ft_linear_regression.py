import utils

def main():
    data = utils.get_data()
    if not data:
        exit(1)
    utils.plot_data_and_regression(data, 0, 0)

main()
    

