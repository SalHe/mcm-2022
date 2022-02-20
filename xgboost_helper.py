import pandas as pd
import numpy as np
import xgboost

def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    df.reset_index(drop=True, inplace=True)
    df = df.iloc[:, n_vars-1:]
    cols = list()
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
    for i in range(0, n_out):
        cols.append(df.shift(-i))
    agg = pd.concat(cols, axis=1)
    if dropnan:
        agg.dropna(inplace=True)
    return agg.values


def train_test_split(data, n_test):
    return data[:-n_test], data[-n_test:]


def xgboost_forecast(train, test_x):
    train = np.asarray(train)
    train_x, train_y = train[:, :-1], train[:, -1]
    model = xgboost.XGBRegressor(
        objective='reg:squarederror', n_estimators=1000)
    model.fit(train_x, train_y)
    yhat = model.predict([test_x])
    return yhat[0]


def mean_absolute_error(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))


def walk_forward_validation(data, n_test):
    predictions = list()
    train, test = train_test_split(data, n_test)
    history = [x for x in train]
    for i in range(len(test)):
        test_x, test_y = test[i, :-1], test[i, -1]
        yhat = xgboost_forecast(train, test_x)
        predictions.append(yhat)
        history.append(test[i])
        # print('>Predicted=%f, Expected=%f' % (yhat, test_y))
    error = mean_absolute_error(test[:, 1], predictions)
    return error, test[:, -2], predictions
