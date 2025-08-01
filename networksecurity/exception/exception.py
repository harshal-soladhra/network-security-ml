import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    """Base class for all network security exceptions."""
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in script: {self.file_name} at line number: {self.lineno} with message: {self.error_message}"
    
if __name__ == "__main__":
    try:
        logger.logging.info("Network security exception module initialized.") 
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
        raise NetworkSecurityException(error_message=e, error_details=sys) from e
        