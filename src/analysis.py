import re
import pickle
import csv
import pandas
import matplotlib.pyplot as plt

cache_path = "/root/data/performance-timings.pkl"
csv_path = "/root/data/results.csv"
figure_path = "/root/data/3d-scatter-plot.png"
performance_timings = {}
results = []

def extract_divs_and_height(url):
    """
    Extracts numbers from a string in the format '/how-many-divs/1000-35px'.

    Args:
        input_string (str): The input string to parse.

    Returns:
        tuple: A tuple containing the two extracted numbers as integers, or None if not found.
    """
    # Define the regex pattern to match the format
    pattern = r"https://ramity.github.io/how-many-divs/(\d+)-(\d+)px"
    
    # Search for matches
    match = re.search(pattern, url)
    
    if match:

        # Extract the two groups as integers
        divs = int(match.group(1))
        height = int(match.group(2))
        return divs, height

    else:

        return None

with open(cache_path, "rb") as file:

    performance_timings = pickle.load(file)

for url in performance_timings:

    divs, height = extract_divs_and_height(url)
    metrics = performance_timings[url]

    # Variables describing various events
    dnsLookupTime = metrics['domainLookupEnd'] - metrics['domainLookupStart']  # DNS lookup duration
    tcpConnectTime = metrics['connectEnd'] - metrics['connectStart']           # TCP connection duration
    secureConnectTime = (
        metrics['connectEnd'] - metrics['secureConnectionStart']
        if metrics['secureConnectionStart'] > 0 else 0
    )  # SSL/TLS handshake duration
    requestTime = metrics['responseStart'] - metrics['requestStart']           # Time to first byte
    responseTime = metrics['responseEnd'] - metrics['responseStart']           # Response duration
    domInteractiveTime = metrics['domInteractive'] - metrics['navigationStart']  # Time to DOM interactive
    domContentLoadedTime = metrics['domContentLoadedEventEnd'] - metrics['navigationStart']  # DOMContentLoaded event time
    domCompleteTime = metrics['domComplete'] - metrics['navigationStart']      # DOM complete time
    loadEventTime = metrics['loadEventEnd'] - metrics['loadEventStart']        # Load event duration
    totalPageLoadTime = metrics['loadEventEnd'] - metrics['navigationStart']   # Total page load time

    # Output example
    result = {
        "Div Count": divs,
        "Div Height": height,
        "DNS Lookup Time": dnsLookupTime,
        "TCP Connect Time": tcpConnectTime,
        "Secure Connection Time": secureConnectTime,
        "Request Time (TTFB)": requestTime,
        "Response Time": responseTime,
        "Time to DOM Interactive": domInteractiveTime,
        "Time to DOMContentLoaded": domContentLoadedTime,
        "Time to DOM Complete": domCompleteTime,
        "Load Event Duration": loadEventTime,
        "Total Page Load Time": totalPageLoadTime
    }
    results.append(result)

with open(csv_path, "w") as file:

    writer = csv.DictWriter(file, fieldnames=result.keys())
    writer.writeheader()
    writer.writerows(results)

dataframe = pandas.DataFrame(results)

def plot_3d_scatter(df, x_col, y_col, z_col):
    """
    Creates a 3D scatter plot from a pandas DataFrame.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        x_col (str): The column name for the x-axis.
        y_col (str): The column name for the y-axis.
        z_col (str): The column name for the z-axis.
    """
    if x_col not in df.columns or y_col not in df.columns or z_col not in df.columns:
        raise ValueError("Specified columns must exist in the DataFrame.")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(df[x_col], df[y_col], df[z_col], c='blue', marker='o')
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col + " (px)")
    ax.set_zlabel(z_col + " (ms)")

    plt.savefig(figure_path)

plot_3d_scatter(dataframe, "Div Count", "Div Height", "Time to DOM Complete")
