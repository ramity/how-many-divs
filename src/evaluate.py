from playwright.sync_api import sync_playwright
import pickle

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)
    performance_timings = {}

    for divs in range(1000, 10000, 100):
        for height in range(1, 36):

            context = browser.new_context()
            page = context.new_page()

            url = f"https://ramity.github.io/how-many-divs/{divs}-{height}.html"
            page.goto(url)
            performance_timings[url] = page.evaluate("() => performance.timing")
            print(f"{url} Performance Timing: {performance_timings[url]}")

    browser.close()
    with open("performance-timings.pkl", "wb") as file:
        pickle.dump(performance_timings, file)
