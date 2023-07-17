# Log all the details inot text file
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # The information will be stored with this datatime format
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)           # Path will be created in the current working folder(src) with folder name logs and the extension with datatime
os.makedirs(logs_path, exist_ok=True)                             # Keep on appending the log files to the folder 

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Whenever we are going to print the log_file or import logging, we will be using the below format
logging.basicConfig(
                    filename = LOG_FILE_PATH,
                    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
                    level = logging.INFO
                    )


# if __name__ == '__main__':
#     logging.info('Logging has started')
