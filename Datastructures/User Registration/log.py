
import logging

def logger(text,user_name):
    
    log=logging.getLogger(user_name)
    logging.basicConfig(filename='logging.log',level=logging.INFO,format='%(levelname)s :%(name)s: %(asctime)s: %(message)s')
    log.info(text)
    
