import time
from datetime import datetime
from typing import Callable, Any
import logging

class Timer:
    """A context manager for timing code execution and logging results."""
    
    def __init__(self, operation_name: str = "operation"):
        self.operation_name = operation_name
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None
        
        # Configure logging
        logging.basicConfig(
            filename='logs/performance.log',
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter()
        self.elapsed_time = self.end_time - self.start_time
        
        # Format the message
        message = f"{self.operation_name} completed in {self.elapsed_time:.4f} seconds"
        
        # Print to console
        print(message)
        
        # Log to file
        logging.info(message)
        
        return False
    
    @staticmethod
    def time_it(func: Callable) -> Callable:
        """Decorator to time a function execution."""
        def wrapper(*args, **kwargs) -> Any:
            with Timer(func.__name__):
                return func(*args, **kwargs)
        return wrapper