from datetime import datetime
from xManager import send_tweet
import json
import time
import logging
from colorama import Fore, Style

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
TARGET_HOUR = 8  # Set the target hour (8 AM)
TARGET_MINUTE = 0  # Set the target minute (0 minutes)

# Global Variables
current_index = 0

# ASCII Art for StoicBot
ascii_art_stoicbot = r"""
   _____       _      _____  _              _    _                      
|   __|| |_  ___ |_| ___ | __  | ___ | |_   |   __|| |_  ___  ___ | |_ |_| ___  ___            
|__   ||  _|| . || ||  _|| __ -|| . ||  _|  |__   ||  _|| .'||  _||  _|| ||   || . |   _  _  _ 
|_____||_|  |___||_||___||_____||___||_|    |_____||_|  |__,||_|  |_|  |_||_|_||_  |  |_||_||_|
                                                                               |___|           

"""

# ASCII Art for Sending Tweet
ascii_art_sending_tweet = r"""
                                                            
 _____           _ _            _____                   _   
|   __|___ ___ _| |_|___ ___   |_   _|_ _ _ ___ ___ ___| |_ 
|__   | -_|   | . | |   | . |    | | | | | | -_| -_| -_|  _|
|_____|___|_|_|___|_|_|_|_  |    |_| |_____|___|___|___|_|  
                        |___|                               
"""

# Print StoicBot ASCII Art
print(Fore.CYAN + ascii_art_stoicbot + Style.RESET_ALL)

def get_next_quote():
    """Fetch the next quote from the JSON file and send it as a tweet."""
    global current_index
    try:
        with open('tweets.json', 'r') as file:
            data = json.load(file)
            quote = data['quotes'][current_index]
            print(Fore.MAGENTA + ascii_art_sending_tweet + Style.RESET_ALL)
            logging.info(Fore.MAGENTA + f"Sending tweet: {quote}" + Style.RESET_ALL)
            send_tweet(quote)

            # Increment the index
            current_index += 1

            # Reset index if all quotes have been sent
            if current_index >= len(data['quotes']):
                current_index = 0
    except Exception as e:
        logging.error(f"Error reading quotes: {e}")

def run_daily_sequence():
    """Define the daily sequence of tasks."""
    logging.info(Fore.YELLOW + "Running daily sequence..." + Style.RESET_ALL)
    get_next_quote()  # Fetch and send the next quote

if __name__ == "__main__":
    while True:
        now = datetime.now()
        # Check if it is 8 AM
        if now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE:
            run_daily_sequence()
            time.sleep(59)  # Sleep for 1 minute
        else:
            print(Fore.RED + "Checking......" + Style.RESET_ALL)
            time.sleep(59)  # Sleep for 1 minute
