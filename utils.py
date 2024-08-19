import os
import csv
import numpy as np
import matplotlib.pyplot as plt

def check_if_file_is_readable(filename):
    if not os.path.exists(filename) or not os.access(filename, os.R_OK):
        print('data.csv does not exist or is not readable')
        return False
    return True

def check_if_file_is_writable(filename):
    if not os.path.exists(filename) or not os.access(filename, os.W_OK):
        print('params.json does not exist or is not writable')
        return False
    return True

def get_data():
    if not check_if_file_is_readable('data.csv'):
        return None
    
    data = []
    try:
        with open('data.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                row = { 'features': row[0], 'target': row[1] }
                data.append(row)
    except:
        print('Error while reading data.csv')
        return None
    return data

def normalisation(s):
    return [((_ - min(s)) / (max(s) - min(s))) for _ in s]