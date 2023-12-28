#!/usr/bin/python3

import logging

# logging.basicConfig(filename='mod.log', filemode='r+',
#                     format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
# logging.warning('file will be logged to a file')

# logging.basicConfig(filemode='r+')

# logging.basicConfig(filename='mod.log', filemode='a+', format='%(process)d-%(levelname)s-%(message)s')
# logging.warning('This is a Warning')

# logging.basicConfig(filename='mod.log', filemode='a+',
#                     format='%(asctime)s - %(message)s - %(name)s', 
#                     datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
# print()
# logging.info('Admin logged in')

a = 5
b = 0

try:
    result = a / b
except Exception as error:
    logging.exception("Exception occurred")
logging.basicConfig(filename='mod.log', filemode='a+')
# logging.ERROR