import logging.handlers
import logging


class Loggen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename="logs/loginNotificationLog.log", format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S', filemode='w')
        rotate_file = logging.handlers.RotatingFileHandler(
            "logs/loginNotificationLog.log", maxBytes=1024 * 1024 * 20, backupCount=3
        )
        logger = logging.getLogger()
        logger.addHandler(rotate_file)
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def home():
        logging.basicConfig(filename="logs/homeNotificationLog.log", format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S', filemode='w')
        rotate_file = logging.handlers.RotatingFileHandler(
            "logs/homeNotificationLog.log", maxBytes=1024 * 1024 * 20, backupCount=3
        )
        logger = logging.getLogger()
        logger.addHandler(rotate_file)
        logger.setLevel(logging.INFO)
        return logger


Loggen.loggen()