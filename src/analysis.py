import matplotlib
import pickle

cache_path = "performance-timings.pkl"
performance_timings = {}
with open(cache_path, "r") as file:
    pickle.dump(performance_timings, file)

for url, metrics in performance_timings:

    time_to_interactive = metrics["domInteractive"] - metrics["navigationStart"]
    dom_content_load_time = metrics["domContentLoadedEventEnd"] - metrics["navigationStart"]
    render_time = metrics["domComplete"] - metrics["navigationComplete"]
    total_page_load_time = metrics["loadEventEnd"] - metrics["navigationStart"]

    print(time_to_interactive, dom_content_load_time, render_time, total_page_load_time)
    break
