import logging
import os
from datetime import datetime

# Create a timestamped log filename
timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
log_filename = f"{timestamp}.log"

# Define log directory and ensure it exists
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Full path for the log file
log_file_path = os.path.join(log_dir, log_filename)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] [Line: %(lineno)d] [%(name)s] - %(levelname)s - %(message)s",
    level=logging.INFO,
)