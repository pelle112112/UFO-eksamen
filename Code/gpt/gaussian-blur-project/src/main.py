from blur import apply_gaussian_blur
from utils.timer import Timer
import logging

def main():
    input_image_path = 'images/input.jpg'
    output_image_path = 'images/output.jpg'

    # Set up logging
    logging.basicConfig(filename='logs/execution.log', level=logging.INFO)

    # Start the timer
    timer = Timer()
    timer.start()

    # Apply Gaussian blur
    apply_gaussian_blur(input_image_path, output_image_path)

    # Stop the timer and log the execution time
    elapsed_time = timer.stop()
    logging.info(f'Execution time: {elapsed_time:.2f} seconds')
    print(f'Execution time: {elapsed_time:.2f} seconds')

if __name__ == '__main__':
    main()