import logging
'''
5 Levels:
========
DEBUG      10 
INFO       20
WARNING    30
ERROR      40
CRITICAL   50
'''
log_format="%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="output.log",
    level=logging.DEBUG,
                    format=log_format)
log=logging.getLogger()
log.debug("Debug message")
log.info("This is an information")
log.warning("There is a warning")
log.error("There is a error should be fixed")
log.critical("CRITICAL ISSUE! ACT ON IT.")


