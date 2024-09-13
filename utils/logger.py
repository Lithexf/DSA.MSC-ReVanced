'This file handles every interaction with logging'
import logging
from logging.handlers import RotatingFileHandler
import os
from colorama import Fore, Style, init


class RelativePathFilter(logging.Filter):
    def filter(self, record):
        record.pathname = os.path.relpath(record.pathname)
        return True

error_path = 'logs/errors.log'
change_path = 'logs/changes.log'



# creates error logger.
def setup_error_logger(log_file: str = error_path) -> logging.Logger:
    logger = logging.getLogger("errorLogger")
    logger.setLevel(logging.DEBUG)

    # Ensure the log file path is relative to the current working directory
    log_file_path = os.path.join(os.getcwd(), log_file)

    # File handler
    file_handler = RotatingFileHandler(log_file_path, maxBytes=5000000, backupCount=5, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    
    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(threadName)s - .\\%(pathname)s:%(lineno)d')
    file_handler.setFormatter(formatter)
    file_handler.addFilter(RelativePathFilter())
    console_handler.setFormatter(formatter)
    
    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger


def setup_change_logger(log_file: str = change_path)->logging.Logger:
    logger = logging.getLogger("changeLogger")
    logger.setLevel(logging.INFO)

    log_file_path = os.path.join(os.getcwd(), log_file)
    
    file_handler = RotatingFileHandler(log_file_path, maxBytes=5000000, backupCount=5, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger


if __name__ == "__main__":
    error_logger = setup_error_logger()
    error_logger.debug("This is a debug message")
    error_logger.info("This is an info message")
    error_logger.warning("This is a warning message")
    error_logger.error("This is an error message")
    error_logger.critical("This is a critical message")

    change_logger = setup_change_logger()
    change_logger.info(f"alama hozzáadva az adatbázishoz")
    change_logger.info(f"UPDATED value from {"old_value"} to {"new_value"}")

