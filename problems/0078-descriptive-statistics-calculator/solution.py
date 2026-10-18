import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    

    def average(data):
        total = 0
        for i in range(len(data)):
            total += data[i]
        
        return total/len(data)

    def calc_variance(data, mean):
        total = 0
        for i in range(len(data)):
            total += (data[i] - mean) ** 2
        return total/len(data)

    def mode_calc(data):
        vals, counts = np.unique(data, return_counts=True)
        return vals[np.argmax(counts, axis=0)]

    
    mean = average(data)
    var = calc_variance(data, mean)
    std_deviation = np.sqrt(var)
    median = np.median(data)
    quartiles = np.percentile(data, [25, 50, 75])
    iqr = quartiles[2] - quartiles[0]
    mode = mode_calc(data)


    stat_dict = {
        "mean" : mean,
        "median" : median,
        "mode" : mode,
        "variance" : np.round(var, 4),
        "standard_deviation" : np.round(std_deviation,4),
        "25th_percentile" : quartiles[0],
        "50th_percentile" : quartiles[1],
        "75th_percentile" : quartiles[2],
        "interquartile_range" : iqr,
        
    }

    return stat_dict

    
    

    pass