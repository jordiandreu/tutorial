import logging
import traceback
from logging.handlers import RotatingFileHandler
# see also TimedRotatingFileHandler and JsonLogging


logger = logging.getLogger(__name__)
logger.debug('hello from helper file')

# Add handlers

stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')
rot_file_h = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)
rot_file_h.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s --- %(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)
rot_file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)
logger.addHandler(rot_file_h)

logger.warning('This is a warning')
logger.error('This is an error')


# Test rotating file handler
for _ in range(10000):
    logger.debug('This is an info message')

# Adding the stack trace on Exception

a = [1, 2, 3]
try:
    a[4]
except IndexError as e:
    logger.error(e, exc_info=True)

# Without using Exception class
try:
    a[4]
except:
    logger.error('An exception occurred, %s' % traceback.format_exc())

