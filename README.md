# Purpose

This project is a stepping stone project that explores the limit of modern browsers.
More specifically, how many divs can a browser handle for the purposes of rendering file text.
I'd like to explore the idea of an IDE within a browser, but I'm jaded by a past experience.
Once upon a time, I sought out to make a spreadsheets clone within a browser, but quickly found the need for a clever rendering scheme for it to work.
It occured to me that I had never made reference to how Google implemented spreadsheets in a browser.
Checking it would reveal, the canvas element, and thus brings us back to my previous delima.
Now, near the end of 2024, how many divs?

# Signals

`performance.timing` values are pulled to assess the performance for each page. Values are added to a performance-timings.pkl file for later analysis and visualization.

# Research

Through my research of lighthouse, it seems 1,000 - 1,500 are considered cutoffs for "ideal" DOM sizes.
Google lighthouse discusses max of 60 child nodes and max depth of 32 per branch.

# Testing

Create a python script that generates static webpages.

Create a html + js webpage that generates the same params as above, but using javascript to create the elements after pageload.

Create a canvas based approach that handles memory

# Implementation

`generate.py` is a python script that generates 1000 to 10000 (@100 increments; inclusive) divs, at 1 to 35 (@1 increments; inclusive) heights rendering a total of 100 * 35 = 3,500 static webpages.

`evaluate.py` is a python script that leverages the playwright library to navigate to each static webpage and pulls the javascript performance timing metrics and stores the results into a performance-timings.pkl file.

`performance-timings.pkl` contains an object following a key (URL) object (metrics object) scehma.

- navigationStart - Marks the time when the navigation to the document started.
This is the starting point for all other timing metrics.
- unloadEventStart - Indicates the time immediately before the unload event of the previous document is fired, if applicable.
- unloadEventEnd - Indicates the time immediately after the unload event of the previous document is completed.
- redirectStart - Marks the time of the start of the first HTTP redirect, if any occurred.
0 if there were no redirects.
- redirectEnd - Marks the time of the completion of the last HTTP redirect, if any occurred.
0 if there were no redirects.
- fetchStart - Indicates when the browser started fetching the resource (before DNS lookup).
- domainLookupStart - Marks the time just before the DNS lookup for the domain name starts.
- domainLookupEnd - Marks the time immediately after the DNS lookup for the domain name is completed.
- connectStart - Marks the time just before the connection to the server starts, including any required proxy negotiation.
- connectEnd - Marks the time immediately after the connection to the server is established.
Includes SSL handshake completion, if applicable.
- secureConnectionStart - Marks the time when the SSL/TLS handshake starts.
0 if the connection is not secure.
- requestStart - Indicates the time when the browser sends the request for the document to the server.
- responseStart - Marks the time immediately after the browser receives the first byte of the response from the server.
- responseEnd - Marks the time immediately after the browser receives the last byte of the response.
- domLoading - Indicates when the browser starts parsing the HTML document.
- domInteractive - Marks the time when the browser has finished parsing the HTML document and the DOMContentLoaded event is about to be fired.
- domContentLoadedEventStart - Marks the time just before the DOMContentLoaded event is fired.
- domContentLoadedEventEnd - Marks the time just after the DOMContentLoaded event is completed.
- domComplete - Indicates the time when the HTML document and all subresources are completely loaded and parsed.
- loadEventStart - Marks the time just before the load event of the document is fired.
loadEventEnd - Marks the time immediately after the load event is completed.

`analysis.py` is a python script that looks in the `performance-timings.pkl` file described above and creates a plot on how div counts and div heights impact render performance.
