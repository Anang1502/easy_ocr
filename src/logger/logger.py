import os
import logging
import logging.config
import json
from logging.handlers import TimedRotatingFileHandler
import config as cf

log_path = os.path.join(cf.BASE_PATH, "configs", "timed_logging.json")



def load_log():
    with open(log_path, 'r') as logging_configuration_file:
        config_dict = json.load(logging_configuration_file)

    config_dict["handlers"]["file_handler"]["filename"] = os.path.join(cf.BASE_PATH, "logs", "request.log")
    config_dict["handlers"]["error_file_handler"]["filename"] = os.path.join(cf.BASE_PATH, "logs", "error.log")

    logging.config.dictConfig(config_dict)

    # Log that the logger was configured
    logger = logging.getLogger(__name__)
    return logger


# def load_log():
#     logger = logging.getLogger("SFNLUEntry")
#     logger.setLevel(logging.DEBUG)
#     log_format = (
#         '%(asctime)s - '
#         '%(name)s - '
#         '%(filename)s - '
#         '%(lineno)s - '
#         '%(funcName)s - '
#         '%(levelname)s - '
#         '%(message)s'
#     )
#
#     # Output full log
#     fh = TimedRotatingFileHandler(os.path.join(cf.BASE_PATH, "logs", "request.log"), when="M", interval=4,
#                                   backupCount=5)
#     fh.setLevel(logging.INFO)
#     formatter = logging.Formatter(log_format)
#     fh.setFormatter(formatter)
#     logger.addHandler(fh)
#
#     # Output error log
#     fh = TimedRotatingFileHandler(os.path.join(cf.BASE_PATH, "logs", "error.log"), when="M", interval=4, backupCount=5)
#     fh.setLevel(logging.ERROR)
#     formatter = logging.Formatter(log_format)
#     fh.setFormatter(formatter)
#     logger.addHandler(fh)
#
#     return logger
