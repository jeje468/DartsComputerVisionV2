# %%
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
# from scipy.interpolate import interp2d, griddata
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.optimizers import Adam
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error


# %%
data = pd.read_csv('testData2.txt', names=['detected_hit', 'actual_hit', 'detected_x', 'actual_x', 'detected_y', 'actual_y', 'zone'])

detected_x = data['detected_x']
detected_y = data['detected_y']
detected_distance = np.sqrt(detected_x**2 + detected_y**2)
data['detected_distance'] = detected_distance

actual_x = data['actual_x']
actual_y = data['actual_y']
actual_distance = np.sqrt(actual_x**2 + actual_y**2)
data['actual_distance'] = actual_distance

dist_diff = actual_distance - detected_distance
data['dist_diff'] = dist_diff
data

# # %%
# train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
# train_data, val_data = train_test_split(train_data, test_size=0.2, random_state=42)

# # Extract the input features and output variable
# X_train = train_data[['detected_x', 'detected_y']].values
# y_train = train_data['dist_diff'].values
# X_val = val_data[['detected_x', 'detected_y']].values
# y_val = val_data['dist_diff'].values
# X_test = test_data[['detected_x', 'detected_y']].values
# y_test = test_data['dist_diff'].values

# # Normalize the input features to have zero mean and unit variance
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_val = scaler.transform(X_val)
# X_test = scaler.transform(X_test)

# # Train a linear regression model on the training set
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Evaluate the performance of the model on the validation set
# y_val_pred = model.predict(X_val)
# mse_val = mean_squared_error(y_val, y_val_pred)
# print(f'Validation MSE: {mse_val:.4f}')

# # Evaluate the performance of the model on the test set
# y_test_pred = model.predict(X_test)
# mse_test = mean_squared_error(y_test, y_test_pred)
# print(f'Test MSE: {mse_test:.4f}')

# distance_diff = model.predict(np.array([[2, 2]]))
# distance_diff[0]

# # %%
# X = data[["detected_x", "detected_y"]]
# y = data["dist_diff"]
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# # Train the decision tree
# tree = DecisionTreeRegressor()
# tree.fit(X_train, y_train)

# # Make predictions on the test set
# y_pred = tree.predict(X_test)

# # Calculate the mean squared error
# mse = mean_squared_error(y_test, y_pred)
# print("Mean squared error:", mse)
# prediction = tree.predict(np.array([[2,2]]))[0]
# prediction

# X = np.column_stack((data['x'], data['y']))
# y = data['dist_diff']

# # Split your data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Create a neural network model
# model = Sequential()
# model.add(Dense(units=64, activation='relu', input_shape=(2,)))
# model.add(Dense(units=1))

# # Compile the model
# model.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=0.001))

# # Train the model
# model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

# # Evaluate the model
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# print("Mean squared error:", mse)

# # Use the model to make predictions
# new_detected_x = [2]
# new_detected_y = [2]
# new_distances = model.predict(np.column_stack((new_detected_x, new_detected_y)))
# print(new_distances)

