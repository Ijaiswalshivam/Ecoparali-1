# machine_learning_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_model(df, feature_cols, target_col):
    X = df[feature_cols]
    y = df[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')
    return model

if __name__ == "__main__":
    data = pd.read_csv('clean_stubble_data.csv')
    feature_cols = ['stubble_quantity', 'soil_health']
    target_col = 'crop_yield'
    model = train_model(data, feature_cols, target_col)
