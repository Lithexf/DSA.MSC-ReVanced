import logging
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Configure the logger
logging.basicConfig(filename='db_changes.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()

def log_change(change_type, message):
    if change_type == "ADDED":
        color = Fore.GREEN
    elif change_type == "DELETED":
        color = Fore.RED
    elif change_type == "UPDATED":
        color = Fore.YELLOW
    else:
        color = Fore.WHITE  # Default color for unknown change types

    log_message = f"{change_type} value: {message}"
    color_log_message = f"{color}{change_type}{Fore.WHITE} value: {message}{Style.RESET_ALL}"
    
    logger.info(log_message)  # Log plain text message to file
    print(color_log_message)  # Print colored message to terminal

# Example usage
log_change("ADDED", "New record")
log_change("DELETED", "Old record")
log_change("UPDATED", "Old value to New value")
