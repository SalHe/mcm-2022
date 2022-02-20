import os
import sys
import getopt
import pandas as pd
from xgboost_helper import *

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "i:s:k:", [
                               'input=', 'steps=', 'known='])
    for (opt, arg) in opts:
        if opt in ('-i', '--input'):
            csv_file = arg
        elif opt in ('-s', '--steps'):
            steps_in = int(arg)
        elif opt in ('-k', '--known'):
            known_item_count = int(arg)
    
    df = pd.read_csv(csv_file)
    data = series_to_supervised(df, n_in=steps_in)
    data = data[:known_item_count+1]
    error, test_y, predictions = walk_forward_validation(data, 1)
    print('> Error: %.3f' % error)
    print('> Test: %.3f' % test_y)
    print('> Pred: %.3f' % predictions[0])

