from datetime import datetime, timedelta
from threading import Timer
from xManager import send_tweet

# Configuration
target_hour = 8  # Set the target hour (8 AM)
target_minute = 0  # Set the target minute (0 minutes)
daily_interval = 24 * 60 * 60  # Interval to run once per day (in seconds)

def run_at_time(target_time, func):
    now = datetime.now()
    wait_time = (target_time - now).total_seconds()
    if wait_time < 0:
        wait_time += daily_interval  # This ensures the function runs the next day if the target time has passed
    Timer(wait_time, func).start()

def daily_sequence():
    # send_tweet(tweet_message)
    print(f"Task ran at {datetime.now()}")
    
    # Schedule the next run at 8 AM the next day
    target_time = datetime.now() + timedelta(days=1)
    target_time = target_time.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)
    run_at_time(target_time, daily_sequence)

if __name__ == "__main__":
    # Start the sequence
    now = datetime.now()
    
    # Calculate the next 8 AM (whether today or tomorrow)
    if now.hour < target_hour or (now.hour == target_hour and now.minute == 0):
        target_time = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)
    else:
        target_time = (now + timedelta(days=1)).replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)

    print(f"Starting sequence at {datetime.now()}")
    run_at_time(target_time, daily_sequence)
