# Purpose

This project is a stepping stone project that explores the limit of modern browsers.
More specifically, how many divs can a browser handle for the purposes of rendering file text.
I'd like to explore the idea of an IDE within a browser, but I'm jaded by a past experience.
Once upon a time, I sought out to make a spreadsheets clone within a browser, but quickly found the need for a clever rendering scheme for it to work.
It occured to me that I had never made reference to how Google implemented spreadsheets in a browser.
Checking it would reveal, the canvas element, and thus brings us back to my previous delima.
Now, near the end of 2024, how many divs?

Using https://ramity.github.io/js-map-generator/ as a format guide, how many divs of uniform size can be rendered on a webpage and what metric should be the signal?

# Signals

In the case of chrome, the creation of lighthouse reports can provide a good amount of data.

# Research

Through my research of lighthouse, it seems 1,000 - 1,500 are considered cutoffs for "ideal" DOM sizes.
Google lighthouse discusses max of 60 child nodes and max depth of 32 per branch.

# Testing

Create a python script that generates 1000 (@100 increments) to 10000 divs, at 1 to 36 (@1 increments) heights.
> 100 * 36 = 3,600 webpages

Create a html + js webpage that generates the same params as above, but using javascript to create the elements after pageload.

Create a canvas based approach that handles memory

# Fleeting thought

What about additional param of text being in the divs?
> 3,600 * 2 = 7,200 webpages for addition case of the static pages
