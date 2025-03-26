class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        from time import time
        self.start_time = time()

    def stop(self):
        from time import time
        self.end_time = time()

    def elapsed_time(self):
        if self.start_time is None or self.end_time is None:
            raise ValueError("Timer has not been started and stopped properly.")
        return self.end_time - self.start_time

    def log_time(self, log_file_path):
        elapsed = self.elapsed_time()
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"Elapsed time: {elapsed:.2f} seconds\n")
        print(f"Elapsed time: {elapsed:.2f} seconds")