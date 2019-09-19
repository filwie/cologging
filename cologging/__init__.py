import logging
from sys import stdout, stderr

from datetime import datetime

from requestern import config
from requestern.color import in_color


class ColorFormatter(logging.Formatter):
    level_colors = {
        logging.DEBUG: 'blue',
        logging.INFO: 'green',
        logging.WARNING: 'yellow',
        logging.ERROR: 'red'
    }

    def format(self, record):
        s = super().format(record)
        color = ColorFormatter.level_colors.get(record.levelno, '')
        return in_color(color, s)


def get_stream_handler(output_stream, log_level: int) -> logging.Handler:
    handler = logging.StreamHandler(output_stream)
    handler.setLevel(log_level)
    handler.setFormatter(ColorFormatter(config.LOG_MSG_FORMAT))
    return handler


def get_file_handler(log_file: str, log_level: int) -> logging.Handler:
    handler = logging.FileHandler(log_file)
    handler.setLevel(log_level)
    handler.setFormatter(logging.Formatter(config.LOG_MSG_FORMAT))
    return handler


def get_logger(name, log_file=None, to_stderr=True, level=logging.WARNING):
    logger = logging.getLogger(name)

    output_stream = stderr if to_stderr else stdout
    handlers = [get_stream_handler(output_stream, level)]

    if log_file is not None:
        handlers.append(get_file_handler(log_file, level))

    for handler in handlers:
        logger.addHandler(handler)

    logger.setLevel(level)
    return logger
