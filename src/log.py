import sys


from loguru import logger


def configure_logger():
    logger.remove()
    logger.add(sys.stderr, level="INFO", format="{time:YYYY-MM-DD at HH:mm:ss} - <level>{level}</level> - {message}")
