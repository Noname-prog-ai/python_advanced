import logging.config
from config import dict_config


logging.config.dictConfig(dict_config)
app_logger = logging.getLogger('appLogger')

app_logger.debug("app message level DEBUG")
app_logger.info("app message level INFO")
app_logger.warning("app message level WARNING") 
