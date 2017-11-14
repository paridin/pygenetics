import logging, loggin.handlers
from django.conf import settings

LOGGING_INITIATED = False

def init_logging():
    logger = logging.getLogger('pygenetics_logger')
    logger.setLevel(logging.INFO)
    
    handler = logging.handlers.TimedRoatingFileHandler(settings.LOG_FILENAME, when='midnight')
    formatter = logging.Formatter(LOG_MSG_FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

if not LOGGING_INITIATED:
    LOGGING_INITIATED = True
    init_logging()
