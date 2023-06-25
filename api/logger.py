import logging 

logging.basicConfig(
    level=logging.DEBUG,
    format='%(module)s - %(asctime)s - %(levelname)s : %(message)s',
    handlers=[logging.StreamHandler()],
)

def get_logger(name: str = __name__):
    return logging.getLogger(name=name)
