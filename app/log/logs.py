import logging


def configureLogging(name):
    #Formato
    logFormatter = logging.Formatter(
        '[%(asctime)s.%(msecs)d]\t%(levelname)s [\t%(name)s.%(funcName)s:%(lineno)d]\t %(message)s')

    #Logger
    logger = logging.getLogger(name)
    #Level de errores
    logger.setLevel(logging.INFO)

    #Ficheros
    fileHandler = logging.FileHandler("logs.log")
    fileHandler.setFormatter(logFormatter)
    logger.addHandler(fileHandler)

    #Consola
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)

    return logger