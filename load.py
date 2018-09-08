# Author Andrew Chupin
# Coding in UTF-8
import os
import pandas
import matplotlib
import matplotlib.pyplot as plt


HOUSING_PATH = os.path.join("datasets", "housing")


def load_housing_data(housing_path=HOUSING_PATH):
    cvs_path = os.path.join(housing_path, "housing.csv")
    return pandas.read_csv(cvs_path)

frame = load_housing_data()

import numpy as np


def split_train_test(data, test_ratio):
    np.random.seed(42)
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


def test_slit():
    train_set, test_set = split_train_test(frame, 0.2)
    print(f"{len(train_set)} train + {len(test_set)} test")
    print(test_set)




