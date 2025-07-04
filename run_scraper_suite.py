import concurrent.futures
from config.config import BROWSERSTACK_CONFIGS
from scraper_runner import run_scraper 

if __name__ == "__main__":
    print(" Running full test suite locally...\n")
    try:
        run_scraper() 
        print("Local test suite completed.\n")
    except Exception as e:
        print(f"Local test suite failed: {e}")

    print("Running test suite on BrowserStack...\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(run_scraper, remote=True, capabilities=config)
            for config in BROWSERSTACK_CONFIGS
        ]

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
                print("Remote suite passed.")
            except Exception as e:
                print(f"Remote suite failed")

    print("\n All test suite runs completed.")
