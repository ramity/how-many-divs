from playwright.sync_api import sync_playwright
import pickle
import os

# Init cache
cache_path = "/root/data/performance-timings.pkl"
performance_timings = {}

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)
    context = browser.new_context()

    # Load file into context if it already exists
    if os.path.exists(cache_path):
        with open(cache_path, "rb") as file:
            performance_timings = pickle.load(file)

    for divs in range(1000, 10100, 100):

        print(f"https://ramity.github.io/how-many-divs/{divs}")

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

        # Update saved file
        with open(cache_path, "wb") as file:
            pickle.dump(performance_timings, file)

    browser.close()
