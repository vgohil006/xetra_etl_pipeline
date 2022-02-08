"""
Running the Xetra ETL application
"""

from distutils.command.config import config
import logging
import logging.config
from pathlib import Path

import yaml

def main():
    """
    entry point to run the Xetra ETL Job
    """
    # parse the YAML file
    config_path = Path("configs/xetra_report1_config.yml")
    config = yaml.safe_load(open(config_path))
    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is a test.")

if __name__ == '__main__':
    main()