"""
Stock market prediction using Markov chains.

For each function, replace the return statement with your code.  Add
whatever helper functions you deem necessary.
"""

import comp140_module3 as stocks
import random

### Model

def markov_chain(data, order):
    """
    Create a Markov chain with the given order from the given data.

    inputs:
        - data: a list of ints or floats representing previously collected data
        - order: an integer repesenting the desired order of the markov chain

    returns: a dictionary that represents the Markov chain
    """
    
    dict = {}
    iterable_data = data[order:]
    index = 0
    
    for i in iterable_data:
        temp_set = []
        for j in range(order):
            temp_set.append(data[index + j])
        tup = tuple(temp_set)
        
        if tup not in dict:
            dict[tup] = {}
            dict[tup][i] = 1
        elif i not in dict[tup]:
            dict[tup][i] = 1
        else:
            dict[tup][i] += 1
        index += 1
        
    for key in dict:
        total_val = 0
        for inner_value in dict[key].values():
            total_val += inner_value
        for key1, value1 in dict[key].items():
            dict[key][key1] = value1 / total_val
            
    return dict 

"""
set = [3,2,1,2,3,1,2,0,3,3,2,2,1,2,3,0,0]
set1 = [1,1,1,1,1]
set2 = [0, 1, 2, 3, 0, 1, 2, 3, 0]
set3 = [0, 1, 2, 1, 0, 1, 2, 1, 0]
print(markov_chain(set, 2))
"""

### Predict

def predict(model, last, num):
    """
    Predict the next num values given the model and the last values.

    inputs:
        - model: a dictionary representing a Markov chain
        - last: a list (with length of the order of the Markov chain)
                representing the previous states
        - num: an integer representing the number of desired future states

    returns: a list of integers that are the next num states
    """
    pred = []
    last = tuple(last)
    n = 0
    
    while n < num:
        printed = False
        
        if last not in model:
            pred.append(random.randrange(4))
            printed = True
        else:
            prob = [0,0,0,0]
            for inner_key, inner_value in model[last].items():
                if printed:
                    break

                if inner_value in (1,1.0):
                    pred.append(inner_key)
                    printed = True
                else:
                    prob[inner_key] = inner_value
            
            functional_prob = [prob[0], 
                               (prob[0] + prob[1]), 
                               (prob[0] + prob[1] + prob[2]), 
                               (prob[0] + prob[1] + prob[2] + prob[3])]
            rand = random.random()
            if rand <= prob[0]:
                pred.append(0)
                printed = True
            elif rand <= functional_prob[1]:
                pred.append(1)
                printed = True
            elif rand <= functional_prob[2]:
                pred.append(2)
                printed = True
            elif rand <= functional_prob[3]:
                pred.append(3)
                printed = True
            
        last = list(last)
        last.append(pred[len(pred) - 1])
        last.pop(0)
        last = tuple(last)
        n += 1
    
    return pred

"""
print(predict({(0,): {1: 1}, (1,): {0: 1}}, [0], 3))
print(predict({(0,): {0: 0.3, 1: 0.5, 2: 0.2}}, [0], 1))
"""

### Error

def mse(result, expected):
    """
    Calculate the mean squared error between two data sets.

    The length of the inputs, result and expected, must be the same.

    inputs:
        - result: a list of integers or floats representing the actual output
        - expected: a list of integers or floats representing the predicted output

    returns: a float that is the mean squared error between the two data sets
    """
    
    if len(result) != len(expected):
        return "Error: length of inputs are different sizes"
    
    sum = 0
    n = len(result)
    for i in range(n):
        sum += (result[i] - expected[i]) ** 2
    
    return sum / n

"""
print(mse([1,2,3],[4,5,6]))
"""

### Experiment

def run_experiment(train, order, test, future, actual, trials):
    """
    Run an experiment to predict the future of the test
    data given the training data.

    inputs:
        - train: a list of integers representing past stock price data
        - order: an integer representing the order of the markov chain
                 that will be used
        - test: a list of integers of length "order" representing past
                stock price data (different time period than "train")
        - future: an integer representing the number of future days to
                  predict
        - actual: a list representing the actual results for the next
                  "future" days
        - trials: an integer representing the number of trials to run

    returns: a float that is the mean squared error over the number of trials
    """
    model = markov_chain(train, order)
    error = 0 
    trial = 0
    
    while trial < trials:
        pred = predict(model, test, future)
        error += mse(pred, actual)
        trial += 1
   
    return error / trials

### Application

def run():
    """
    Run application.

    You do not need to modify any code in this function.  You should
    feel free to look it over and understand it, though.
    """
    # Get the supported stock symbols
    symbols = stocks.get_supported_symbols()

    # Get stock data and process it

    # Training data
    changes = {}
    bins = {}
    for symbol in symbols:
        prices = stocks.get_historical_prices(symbol)
        changes[symbol] = stocks.compute_daily_change(prices)
        bins[symbol] = stocks.bin_daily_changes(changes[symbol])

    # Test data
    testchanges = {}
    testbins = {}
    for symbol in symbols:
        testprices = stocks.get_test_prices(symbol)
        testchanges[symbol] = stocks.compute_daily_change(testprices)
        testbins[symbol] = stocks.bin_daily_changes(testchanges[symbol])

    # Display data
    #   Comment these 2 lines out if you don't want to see the plots
    stocks.plot_daily_change(changes)
    stocks.plot_bin_histogram(bins)

    # Run experiments
    orders = [1, 3, 5, 7, 9]
    ntrials = 500
    days = 5

    for symbol in symbols:
        print(symbol)
        print("====")
        print("Actual:", testbins[symbol][-days:])
        for order in orders:
            error = run_experiment(bins[symbol], order,
                                   testbins[symbol][-order-days:-days], days,
                                   testbins[symbol][-days:], ntrials)
            print("Order", order, ":", error)
        print()

run()