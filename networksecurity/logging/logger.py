import logging
import os
from datetime import datetime

"""
logger.py

This module provides a simple logging setup for the network security project.
It configures logging to output messages to both the console and a log file.
"""


LOG_FILE=f"{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.log"

logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=LOG_FILE_PATH
)
