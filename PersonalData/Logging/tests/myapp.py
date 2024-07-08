import logging

# Step 1: Create a logger
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)  # Set the lowest-severity log message that the logger will handle

# Step 2: Create a console handler and set its log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Step 3: Create a file handler and set its log level
file_handler = logging.FileHandler('example.log')
file_handler.setLevel(logging.ERROR)

# Step 4: Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Step 5: Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Step 6: Log messages with different severity levels
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
