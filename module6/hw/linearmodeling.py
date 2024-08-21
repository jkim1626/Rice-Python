import simpleplot
import codeskulptor
from urllib import request
filename = "comp140_module6_candy_data.txt"

def read_data(filename):
    """
    Read and parse a file into a list of ordered pairs.
    """
    url = codeskulptor.file2url(filename)
    netfile = request.urlopen(url)
    values = []
        
    for line in netfile.readlines():
        strline = line.decode('utf-8')
        two = strline.split()
        tuples = (float(two[0]), float(two[1]))
        values.append(tuples)
            
    # print(values)        
    return values

# print(read_data(filename))

def model(xval, slope):
    """
    Evaluate the 1D linear model, y = mx, (where m = slope) 
    at the given x value.
    """
    y_val = xval * slope
    
    return y_val

# print(model(2, 5))

def generate_predictions(xvalues, slope):
    """
    Using the x-values of the data and the given slope (m), 
    use the model y = mx to generate predictions.
    """
    lst = []
    for i in xvalues:
        yval = i * slope
        tup = (i, yval)
        lst.append(tup)
        
    return lst

# print(generate_predictions([1,2,3],2))

def mse(result, expected):
    """
    Calculate the mean squared error between the sequences 
    result and expected.
    """
    total = 0
    for i in range(len(result)):
        total += (result[i] - expected[i]) ** 2
    
    return total

# print(mse([1,2,3],[4,5,6]))

def calc_mse(slope):
    """
    Calc mse given dataset
    """
    data = []
    result = []
    expected = []
    
    for item in read_data(filename):
        data.append(item[0])
        result.append(item[1])
        
    temp_pred = generate_predictions(data, slope)
    
    for pred in temp_pred:
        expected.append(pred[1])
    
    return mse(result, expected)

# print(calc_mse(3))

def calculate_slope(data):
    """
    Calculate the value for the slope, m, which minimizes the MSE
    between the data and the model "y = mx".
    """
    smallest = calc_mse(2)
    best_slope = 0
    for num in range(50):
        if calc_mse(num) < smallest:
            smallest = calc_mse(num)
            best_slope = num
            
    return num

# print(calculate_slope(read_data(filename)))

def apply_model(filename, data, slope):
    """
    Fit the input data with the model "y = mx". 
    Graph the resulting model against the data.
    """
    # Make predictions
    xvalues = [item[0] for item in data]
    predictions = generate_predictions(xvalues, slope)

    # Get actual values and predicted values into lists    
    actual = [item[1] for item in data]
    predicted = [item[1] for item in predictions]
    
    print("File:", filename)
    print("Slope:", slope)
    print("Error:", mse(predicted, actual))
    
    simpleplot.plot_lines(filename, 450, 300, 'x', 'y', 
                          [data, predictions], True, ['data', 'model'])

def run(filename):
    """
    Load the data at the provided filename and fit it with the model
    "y = mx". Graph the resulting model against the data.
    """
    # Read data
    data = read_data(filename)
    
    # Determine best slope
    slope = calculate_slope(data)
    
    # Build and apply model using this slope
    apply_model(filename, data, slope)

#Uncomment this to apply the model to the Halloween data
run("comp140_module6_candy_data.txt")
