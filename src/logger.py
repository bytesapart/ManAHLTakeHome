import os
import logging
import tempfile
import datetime


def init_logger():
    """
    Initializes the logger
    Returns
    -------
    Logger object
    """
    tempdir = tempfile.mkdtemp(
        prefix=f'random_pick_{os.getpid()}__{datetime.datetime.now().strftime("%H_%M_%S")}')
    logger = logging.getLogger('random_pick')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(os.path.join(tempdir, 'logfile.log'))
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(filename)s:%(lineno)s - %(funcName)20s() - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
