import logging
import os

"""
    create logger
"""
log = logging.getLogger("onepoint")


def init_log():
    log_level = getattr(logging, "DEBUG")
    log.setLevel(log_level)

    """
        create console handler and set level to debug
    """
    f_handler = logging.StreamHandler()
    f_handler.setLevel(log_level)
    f_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_handler.setFormatter(f_format)
    log.addHandler(f_handler)
