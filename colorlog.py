"""colorlog.py: A logger module for logging to stdout and/or a file"""
__version__ = '1.0'


import traceback
from datetime import datetime
from pathlib import Path


class ColorLogger:
    """A class for logging messages in color to stdout and/or a file"""

    # ANSI color codes
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    GREEN = '\033[32m'
    MAGENTA = '\033[35m'
    RED = '\033[31m'
    RESET = '\033[0m'
    WHITE = '\033[37m'
    YELLOW = '\033[33m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_CYAN = '\033[96m'
    LIGHT_GRAY = '\033[37m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_MAGENTA = '\033[95m'
    LIGHT_RED = '\033[91m'
    LIGHT_WHITE = '\033[97m'
    LIGHT_YELLOW = '\033[93m'
    LEVELS = {'DEBUG': 1, 'INFO': 2, 'SUCCESS':3, 'WARNING': 4, 'ERROR': 5, 'NONE': 6}

    def __init__(self, *, log_name='logger.log', log_dir=None, level='INFO', log_to_file=False):
        """
        Initialize the ColorLogger class
        Args:
            log_name (str): The name of the log file.
            level (str): The logging level. One of 'DEBUG', 'INFO', 'WARNING', 'ERROR', or 'NONE'.
            out_dir (str): The directory to save the log file.
            log_to_file (bool): Whether to save the log to a file.
        """
        self.log_dir = Path(log_dir) if log_dir is not None else Path.cwd()
        self.log_to_file = log_to_file and self.log_dir is not None

        if not level in self.LEVELS:
            raise ValueError(f'Invalid log level: {level}')
        self.level = self.LEVELS[level]

        if self.log_to_file:
            self.log_dir.mkdir(parents=True, exist_ok=True)
            if not Path(log_name).suffix:
                log_name += '.log'
            self.log_file = self.log_dir / log_name
        print(end='\n')

    def log(self, level, color, message):
        """Logs a message to stdout and/or a file
        Args:
            level (str): the log level, e.g., DEBUG, INFO, etc.
            color (str): the color (ANSI escape code) to use, e.g., Logger.RED
            message (str): the message to log
        """
        if self.LEVELS[level] < self.level:
            return
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        stdout_msg = f'{color}{timestamp} {level}: {message}{self.RESET}'
        file_msg = f'{timestamp} {level}: {message}'
        print(stdout_msg)

        if self.log_to_file:
            with self.log_file.open('a') as fh:
                fh.write(f'{file_msg}\n')

    @staticmethod
    def print_color(color, message):
       """prints a message to stdout in the specified color
       Args:
           color (str): the color (ANSI escape code) to use, e.g., Logger.RED
           message (str): message to print
        """
       print(f'{color}{message}{ColorLogger.RESET}')


    def debug(self, message, include_traceback=False):
        """Logs a debug message
        Args:
            message (str): message to log
            include_traceback (bool): include traceback info in the log
        """
        self.log('DEBUG', self.LIGHT_BLUE, message)
        if include_traceback:
            self.log('DEBUG', self.LIGHT_BLUE, traceback.format_exc())    

    def info(self, message):
        """Logs an info message
        Args:
            message (str): message to log
        """
        self.log('INFO', self.LIGHT_MAGENTA, message)

    def success(self, message):
        """Logs a success message
        Args:
            message (str): message to log
        """
        self.log('SUCCESS', self.LIGHT_GREEN, message)

    def warning(self, message):
        """Logs a warning message
        Args:
            message (str): message to log
        """
        self.log('WARNING', self.YELLOW, message)

    def error(self, message):
        """Logs an error message
        Args:
            message (str): message to log
        """
        self.log('ERROR', self.LIGHT_RED, message)