import sys
from ..logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self):
        return "Error occurred in python name[{0}] line no. [{1}] error msg [{2}]".format(
            self.file_name, self.lineno, str(self.error_message)
        )
    
if __name__ == "__main__":
    try:
        logger.logging.info("Entered try block")
        print("This")
    except Exception as e:
        raise NetworkSecurityException(e, sys)