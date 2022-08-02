import imp
import os
import sys

class PackageException(Exception):
    def __init__(self, error_message:Exception, error_detail:sys) -> None:
        super().__init__(error_message)
        self.error_message = PackageException.get_detailed_error_message(error_message=error_message, error_detail=error_detail)

    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_detail:sys) -> str:

        """
        input: 
            error_message: Exception object
            error_detail: object of the sys module

        Description: This function gives the Error message occured in the code
        
        return: It return the error message string with line and file
        """
        _, _, exc_tb = error_detail.exc_info()

        line_number = exc_tb.tb_frame.f_lineno
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message = f"Error occured in script: [{file_name} at line number: [{line_number}] error_message: [{error_message}]]"
        return error_message

    def __str__(self) -> str:
        return self.error_message

    def __repr__(self) -> str:
        return PackageException.__name__.str()