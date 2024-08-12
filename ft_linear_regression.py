import utils

data = utils.get_data()
if not data:
    exit(1)

utils.plot_data(data)

