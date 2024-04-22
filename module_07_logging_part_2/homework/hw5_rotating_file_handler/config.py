dict_config = {
    "version": 1.0,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "base",
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "h",
            "interval": 10,
            "backupCount": 3,
            "level": "INFO",
            "formatter": "base",
            "filename": "utils.log",
        }
    },
    "loggers": {
        "my_logger": {
            "level": "INFO",
            "handlers": ["file", "console"],
        }
    }
}