#!/usr/bin/env python3

import logging
import tests.mylib as mylib
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    mylib.do_something()
    logger.info('Finished')


if __name__ == '__main__':
    main()