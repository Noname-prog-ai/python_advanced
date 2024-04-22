import logging
import logging.config
import sys


class ASCIIFilter(logging.Handler):
    def filter(self, record: logging.LogRecord) -> bool:
        if record.msg.isascii():
            return True
        else:
            return False


dict_config = {
    "version": 1.0,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(Lineno)s | %(message)s",
        }
    },
    "filters": {
        'ascii_filter': {
            '()': ASCIIFilter,
        }
    },
    "handlers": {
        "console": {
            "class": "Logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filters": ['ascii_filter', ],
        },

    },
    "loggers": {
        "my_logger": {
            "level": "DEBUG",
            "handlers": ["console"],
        }
    }
}