import os
import logging
from datetime import datetime

# Generate a timestamped log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define log directory and ensure it exists
LOGS_DIR = os.path.join(os.getcwd(), 'logs')
try:
    os.makedirs(LOGS_DIR, exist_ok=True)
except Exception as e:
    print(f"Error creating logs directory: {e}")

# Full log file path
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

# Configure logging: Log to file and console
logging.basicConfig(
    level=logging.INFO,  # Can be changed to DEBUG, WARNING, ERROR, etc.
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),  # Log to file
        logging.StreamHandler()  # Log to console
    ]
)

logging.info("Logging setup complete. Logs will be saved to %s", LOG_FILE_PATH)
