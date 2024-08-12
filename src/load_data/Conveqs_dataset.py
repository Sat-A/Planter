# THIS FILE IS PART OF Planter PROJECT
# Planter.py - The core part of the Planter library
#
# THIS PROGRAM IS FREE SOFTWARE TOOL, WHICH MAPS MACHINE LEARNING ALGORITHMS TO DATA PLANE, IS LICENSED UNDER Apache-2.0
# YOU SHOULD HAVE RECEIVED A COPY OF WTFPL LICENSE, IF NOT, PLEASE CONTACT THE FOLLOWING E-MAIL ADDRESSES
#
# E-mail: changgang.zheng@eng.ox.ac.uk or changgangzheng@qq.com
#
# Functions: This file loads the data from the given dataset.
#            Please refer to ./Docs/Planter_User_Document.pdf or further information.

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def load_data(num_features, data_dir):
    # Load the dataset with the relevant columns
    #data = pd.read_csv(data_dir + '/Conveqs/conveqs.csv', usecols=['Avg_Timestamp', 'Source', 'N_Objects', 'Avg_Speed', 'Avg_Acceleration', 'Group2'])
    data = pd.read_csv(data_dir + '/Conveqs/conveqs.csv', usecols=[0,2,3,4,5])
    data['Avg_Timestamp'] = (data['Avg_Timestamp']%100000).astype("int")
    data['Avg_Speed'] = (data['Avg_Speed']*100).astype("int")
    data['Avg_Acceleration'] = (data['Avg_Acceleration']*100).astype("int")
    print(data)
    # Select the features based on the number specified
    used_features = ['Avg_Timestamp', 'N_Objects', 'Avg_Speed', 'Avg_Acceleration'][:num_features]

    # Extract the features (X)
    X = data[used_features]

    # Encode the target variable (Group2) using LabelEncoder
    encoder_target = LabelEncoder()
    y = encoder_target.fit_transform(data['Group2'])

    # Split the dataset into training and testing sets
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=101, shuffle=True)

    return train_X, train_y, test_X, test_y, used_features
