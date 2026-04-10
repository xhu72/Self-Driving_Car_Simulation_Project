import os
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data():
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'best_car_recordings_comp_vision')
    data_df = pd.read_csv(os.path.join(data_dir, 'driving_log.csv'), names=['center', 'left', 'right', 'steering', 'throttle', 'reverse', 'speed'])

    X = data_df[['center', 'left', 'right']].values
    y = data_df['steering'].values

    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=0)

    return X_train, X_valid, y_train, y_valid
