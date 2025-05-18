import logging


def logger_function(loggername, loggfilename='server.log', level=logging.DEBUG):
    logger = logging.getLogger(loggername)
    logger.setLevel(level)
    logging.basicConfig()
    filehandler = logging.FileHandler(loggfilename)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    return logger
