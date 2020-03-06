import logging, logging.handlers

'''
this model is name A_log.py so it gets loaded first
'''

def get_configured_logger(name):
    logger = logging.getLogger(name)
    if (len(logger.handlers) == 0):
        # This logger has no handlers, so we can assume it hasn't yet been configured
        # Create RotatingFileHandler
        import os
        formatter = "%(asctime)s %(levelname)s %(process)s %(thread)s %(filename)s %(funcName)s():%(lineno)d %(message)s"
        handler = logging.handlers.RotatingFileHandler(os.path.join(request.folder,'private/app.log'), maxBytes = 1024*1024*10, backupCount = 6)
        handler.setFormatter(logging.Formatter(formatter))
        handler.setLevel(logging.INFO)
        
        handler_d = logging.handlers.RotatingFileHandler(os.path.join(request.folder,'private/app_debug.log'), maxBytes = 1024*1024*10, backupCount = 2)
        handler_d.setFormatter(logging.Formatter(formatter))
        handler_d.setLevel(logging.DEBUG)        

        logger.addHandler(handler)
        logger.addHandler(handler_d)
        logger.setLevel(logging.DEBUG)

        # Test entry:
        #logger.debug(name + ' logger created')
    else:
        # Test entry:
        #logger.debug(name + ' already exists')
        pass
    return logger

# Assign application logger to a global var  
logger = get_configured_logger(request.application)

from gluon import current
current.logger = logger
