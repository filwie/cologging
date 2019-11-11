from logging import Formatter, DEBUG, INFO, WARNING, ERROR
from incolor import Color, incolor


class ColorFormatter(Formatter):
    level_colors = {
        DEBUG: Color.blue,
        INFO: Color.green,
        WARNING: Color.yellow,
        ERROR: Color.red
    }

    def format(self, record):
        s = super().format(record)
        color = ColorFormatter.level_colors.get(record.levelno, Color.white)
        return incolor(s, fg=color)
