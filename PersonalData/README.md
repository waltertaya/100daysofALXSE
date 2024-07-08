# Personal Data

## Contents

1. [What is PII, non-PII and personal data](www.google.com)
2. [Logging - Logging facility for Python](https://docs.python.org/3/library/logging.html)


## Table of Contents

1. [Logging facility for python](#logging-facility-for-python)

## Logging facility for Python

- Built-in module that allows to track events and messages when the code runs. 
- It provides a way to record events, which can be used for debugging, troubleshooting, or monitoring purposes.
- The main use of the logging module is to log messages at different levels of severity, including:

    1. Debug: Provides detailed information about the code execution flow.
    2. Info: Logs general information about the code execution flow.
    3. Warning: Logs potential issues or unexpected events.
    4. Error: Logs unexpected errors or exceptions.
    5. Critical: Logs critical errors or exceptions that can cause the program to terminate.

- The logging module provides a hierarchy of log levels, allowing you to control the level of detail and importance of the logged messages. You can also configure the logging module to log messages to different destinations, such as files, console, or network sockets.

- `Main Components of the Logging Module`

   1. Logger: This is the entry point for the logging system. You can have multiple loggers in your application, each identified by a unique name. Loggers provide methods to log messages at different severity levels (DEBUG, INFO, WARNING, ERROR, and CRITICAL).

    2. Handler: Handlers are used to direct log messages to appropriate destinations, such as the console, files, or remote servers. A logger can have multiple handlers, and each handler can direct messages to a different destination.

    3. Formatter: Formatters specify the layout of the log messages. They define the structure of the log output, including things like the timestamp, log level, and message content.

    4. Log Level: Log levels are used to categorize the severity of log messages. The available log levels are DEBUG, INFO, WARNING, ERROR, and CRITICAL.

## Author

- **@waltertaya**
