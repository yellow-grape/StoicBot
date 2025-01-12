from datetime import datetime, timedelta
from threading import Timer
from xManager import send_tweet
import json

# Constants
TARGET_HOUR = 8  # Set the target hour (8 AM)
TARGET_MINUTE = 0  # Set the target minute (0 minutes)
DAILY_INTERVAL = 24 * 60 * 60  # Interval to run once per day (in seconds)

# Global Variables
current_index = 0

def get_next_quote():
    """Fetch the next quote from the JSON file and send it as a tweet."""
    global current_index
    try:
        with open('tweets.json', 'r') as file:
            data = json.load(file)
            quote = data['quotes'][current_index]
            print(f"Current index: {current_index}")
            print(f"Sending tweet: {quote}")
            send_tweet(quote)

            # Increment the index
            current_index += 1

            # Reset index if all quotes have been sent
            if current_index >= len(data['quotes']):
                current_index = 0
    except Exception as e:
        print(f"Error reading quotes: {e}")

def run_at_time(target_time, func):
    """Run a function at a specific target time."""
    now = datetime.now()
    wait_time = (target_time - now).total_seconds()
    Timer(wait_time, func).start()

def daily_sequence():
    """Define the daily sequence of tasks."""
    print(f"Task ran at {datetime.now()}")
    get_next_quote()  # Fetch and send the next quote

if __name__ == "__main__":
    # Start the sequence
    now = datetime.now()
    target_time = now.replace(hour=TARGET_HOUR, minute=TARGET_MINUTE, second=0, microsecond=0)
    if now > target_time:
        target_time += timedelta(days=1)
    run_at_time(target_time, daily_sequence)