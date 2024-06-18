import logging
import os

class Loger:
    def __init__(self, file: int, message: str) -> None:
        self.setup_loggers()
        if file == 0: 
            self.log_error(message)
        elif file == 1:
            self.log_using(message)
        else:
            self.log_error(message)
    
    @staticmethod
    def setup_loggers():
        log_directory = "logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # Erstelle und konfiguriere den Error Logger
        error_logger = logging.getLogger("error_logger")
        if not error_logger.hasHandlers():
            error_handler = logging.FileHandler(os.path.join(log_directory, "error_logs.log"))
            error_handler.setLevel(logging.ERROR)
            error_format = logging.Formatter('%(asctime)s %(message)s')
            error_handler.setFormatter(error_format)
            error_logger.setLevel(logging.ERROR)
            error_logger.addHandler(error_handler)

        # Erstelle und konfiguriere den Usage Logger
        usage_logger = logging.getLogger("usage_logger")
        if not usage_logger.hasHandlers():
            usage_handler = logging.FileHandler(os.path.join(log_directory, "using_logs.log"))
            usage_handler.setLevel(logging.INFO)
            usage_format = logging.Formatter('%(asctime)s %(message)s')
            usage_handler.setFormatter(usage_format)
            usage_logger.setLevel(logging.INFO)
            usage_logger.addHandler(usage_handler)
    
    def log_error(self, message: str):
        error_logger = logging.getLogger("error_logger")
        error_logger.error(message)

    def log_using(self, message: str):
        usage_logger = logging.getLogger("usage_logger")
        usage_logger.info(message)

    @staticmethod
    def clean_logs():
        log_directory = "logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
        open(os.path.join(log_directory, "error_logs.log"), "w").write("")
        open(os.path.join(log_directory, "using_logs.log"), "w").write("")

