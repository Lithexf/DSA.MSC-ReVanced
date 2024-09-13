'This file helps with any parsing of config.ini'
import configparser
from logger import setup_error_logger

error_logger = setup_error_logger()

try:
    config_path = "config/config.ini"
    config = configparser.ConfigParser()
    config.read(config_path)

    config.get('config_log', 'config_log_path')
except Exception as e:
    error_logger.error(f'nem lehetett a config filet beolvasni, {e}')

#Test
if __name__ == "__main__":
    print("config pasrse test")
