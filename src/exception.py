import sys       # Control the python runtime environment, strong interaction with the interpreter - https://docs.python.org/3/library/sys.html
import logging
import os
os.system ('python3 src/logger.py')

# Function for sharing the error information
def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()                # exc_info() gives 3 information, the third one gives information about
                                                        # what is the exception and at which line the exception has happened             
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
                    file_name, exc_tb.tb_lineno, str(error))   # Error message shared in this format

    return error_message

    
# Creating own exception class which is inhering the error meesage and detail 
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):    # Error detail is tracked by sys, overridden init function on error meesage
        super().__init__(error_message)                     # inheriting the __init__ function
        self.error_message = error_message_detail(error_message, error_detail = error_detail)
    
    # Raising the exception - error message
    def __str__(self):
        return self.error_message
    

# Checking if the exception handling is workig fine or not
# if __name__ == '__main__':
#     try:
#         var = 1/0
#     except Exception as e:
#         logging.info('Divide by zero error')
#         raise CustomException(e, sys)
    