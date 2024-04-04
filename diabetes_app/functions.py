import config
import numpy as np
import pandas as pd
import json
import pickle

def get_column_names():
    with open(config.COLUMN_NAME_PATH, 'r') as col:
        column_dict = json.load(col)
    return column_dict['columns']

column_list = get_column_names()

def get_predict(*args):
    with open(config.MODEL_FILE_PATH, 'rb') as f:
        model = pickle.load(f)
    x_test_arr = np.zeros(len(column_list))
    for i, val in enumerate(args):
        x_test_arr[i] = val
    x_test = pd.DataFrame([x_test_arr])
    result = model.predict(x_test)
    if result == 1:
        report = "The patient is diabetic"
    else:
        report = "The patient is not diabetic"
    return result[0]
    # return report
