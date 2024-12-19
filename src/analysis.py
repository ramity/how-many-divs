import matplotlib
import pickle
import re
import csv

cache_path = "performance-timings.pkl"
results_path = "results.pkl"
csv_path = "results.csv"
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

    print(divs, height)

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
