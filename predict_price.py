import json
import utils

def ask_mileage():
    mileage = input('Please enter the mileage of your car: ')
    while not mileage.isdigit() or int(mileage) < 0:
        print('Please enter a valid number')
        mileage = input('Please enter the mileage of your car: ')
    return mileage

def predict_price(mileage, params):
    return params['theta0'] + (params['theta1'] * mileage)
    

def get_parameters():
    if not utils.check_if_file_is_readable('params.json'):
        exit(1)
    try:
        with open('params.json', 'r', newline='') as jsonfile:
            json_data = json.load(jsonfile)
            params = { 'theta0': json_data['theta0'], 'theta1': json_data['theta1'] }
    except:
        print('Error while reading params.json')
        exit(1)
    return params


def main():
    mileage = ask_mileage()
    params = get_parameters()
    price = predict_price(int(mileage), params)
    print('The estimated price of your car is: ' + str(price))

main()