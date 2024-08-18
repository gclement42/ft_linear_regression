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
            row = { 'features': row[0], 'target': row[1] }
            data.append(row)
    return data

def normalisation(s):
    return [((_ - min(s)) / (max(s) - min(s))) for _ in s]