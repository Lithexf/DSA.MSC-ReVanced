from utils.logger import setup_error_logger

error_logger = setup_error_logger()

class UserNotFoundError(Exception):
    """Exception raised when a user is not found."""
    error_logger(f'User Not found error: {Exception}')

class PermissionError(Exception):
    """Exception raised for permission-related errors."""
    error_logger(f'Permission Error: {Exception}')
