from playwright.sync_api import sync_playwright
import pickle
import os

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)
    context = browser.new_context()

    # Init cache
    cache_path = "performance-timings.pkl"
    performance_timings = {}

    # Load file into context if it already exists
    if os.path.exists(cache_path):
        with open(cache_path, "wb") as file:
            pickle.dump(performance_timings, file)

    for divs in range(1000, 10100, 100):

        # Skip clause - Skip if divs category has already been successful
        if f"https://ramity.github.io/how-many-divs/{divs}-35px" in performance_timings:
            print(f"Skipping divs {divs} - a")
            continue

        # Logic
        for height in range(1, 36):

            page = context.new_page()
            url = f"https://ramity.github.io/how-many-divs/{divs}-{height}px"
            page.goto(url)
            performance_timings[url] = page.evaluate("() => performance.timing")
            print(f"{url} Performance Timing: {performance_timings[url]}")

        # Update saved file
        with open(cache_path, "wb") as file:
            pickle.dump(performance_timings, file)

    browser.close()
