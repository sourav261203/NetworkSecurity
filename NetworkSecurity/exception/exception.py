import sys
import traceback
from NetworkSecurity.logging import logger


class NetworkSecurityException(Exception):
    """Custom exception for the Network Security project with detailed traceback info."""

    def __init__(self, error_message: str, error_details: sys):
        super().__init__(error_message)

        # Extract traceback information
        exc_type, exc_value, exc_tb = error_details.exc_info()
        if exc_tb is not None:
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = None
            self.file_name = None

        self.error_message = str(error_message)

    def __str__(self) -> str:
        if self.file_name and self.lineno:
            return (f"Error occurred in python script [{self.file_name}] "
                    f"at line [{self.lineno}] - Message: {self.error_message}")
        return f"Error: {self.error_message}"