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
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

def load_data(num_features, data_dir):
    # Load the combined dataset
    data = pd.read_csv(data_dir + '/Conveqs/conveqs.csv') 
    # Select the features to be used in the model, including 'Source'
    feature_columns = ['Avg_Timestamp', 'Source', 'N_Objects', 'Avg_Speed', 'Avg_Acceleration', 'Approaching', 'Accelerating']
    
    # Ensure that only the required number of features are used
    used_features = feature_columns[:num_features]
    
    # Extract the features (X)
    X = data[used_features]
    
    # Label encode the categorical features
    encoder = LabelEncoder()
    
    if 'Source' in used_features:
        X['Source'] = encoder.fit_transform(X['Source'])
    
    if 'Approaching' in used_features:
        X['Approaching'] = encoder.fit_transform(X['Approaching'])
    
    if 'Accelerating' in used_features:
        X['Accelerating'] = encoder.fit_transform(X['Accelerating'])
    
    # Apply custom scaling for integer features
    X['Avg_Timestamp'] = (X['Avg_Timestamp'] % 100000).astype(int)
    X['N_Objects'] = (X['N_Objects'] * 10).astype(int)
    X['Avg_Speed'] = (X['Avg_Speed'] * 100).astype(int)
    X['Avg_Acceleration'] = (X['Avg_Acceleration'] * 10000).astype(int)
    
    # Encode the target variable (Group2) using LabelEncoder
    y = encoder.fit_transform(data['Group2'])
    
    # Split the dataset into training and testing sets
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=101, shuffle=True)
    
    return train_X, train_y, test_X, test_y, used_features    
