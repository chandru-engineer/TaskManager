import logging
from logging.handlers import RotatingFileHandler

# Configure the root logger
logging.basicConfig(level=logging.DEBUG)

# Create a custom logger
logger = logging.getLogger('your_app_logger')
logger.setLevel(logging.DEBUG)

# Create a file handler and set the logging level
file_handler = RotatingFileHandler('TaskManagement.log', maxBytes=10240, backupCount=10)
file_handler.setLevel(logging.DEBUG)

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)