import os

STEPS_IN = 5
ALWAYS_RETRAIN = True # If true, always retrain the model. If false, only retrain if the error is greater than the previous error.
MODEL_PATH_BITCOIN = os.path.abspath(os.path.join(os.path.curdir, 'bitcoin.model'))
N_TEST = 800

LABEL_BITCOIN_VALUE = 'Value'
LABEL_DATE = 'Date'

LABEL_GOLD_VALUE = 'USD (PM)'

LABEL_GOLD_DEAL_OPEN = 'Gold Deal Open'
LABEL_GOLD_LAST_TEN_DAYS_MEAN = "Gold Value's Mean"
LABEL_BITCOIN_LAST_TEN_DAYS_MEAN = "BTC Value's Mean"
LABEL_PREDICTION_GOLD = 'Gold Prediction'
LABEL_PREDICTION_BTC = 'BTC Prediction'

LABEL_GOLD_INCREASE = 'Gold Increasement'
LABEL_BTC_INCREASE = 'BTC Increasement'
LABEL_GOLD_INCREASE_PERCENT = 'Gold Increasement Percent'
LABEL_BTC_INCREASE_PERCENT = 'BTC Increasement Percent'

LABEL_ACCURACY_BTC = 'Accuracy BTC'
LABEL_ACCURACY_GOLD = 'Accuracy Gold'
