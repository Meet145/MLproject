import logging
import os
from datetime import datetime

# Define the log file name using the current date and time
LOG_FILE = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".log"

# Define the path where logs will be stored
logs_path = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it does not exist
os.makedirs(logs_path, exist_ok=True)

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s %(lineno)d %(name)s %(levelname)s %(message)s',
    level=logging.INFO,
)   

 
