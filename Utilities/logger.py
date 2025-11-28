import logging
import os

log_path = r"D:\\CAREER\\Pytest Practice\\CredKart 2025-26\\Logs"

# create folder if not exists
os.makedirs(log_path, exist_ok=True)

def get_logger():
    logger = logging.getLogger("automation")
    if not logger.handlers:            # Avoid duplicate logs
        logger.setLevel(logging.INFO)

        log_file = os.path.join(log_path, "automation.log")

        fileHandler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

    return logger