import cv2
import time
import logging
from pathlib import Path

# Setting up logging
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
logging.basicConfig(filename=log_dir / "execution_time.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def apply_gaussian_blur(input_path: str, output_path: str, kernel_size: int = 15):
    """
    Apply Gaussian blur to the input image and save the result.
    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the blurred image.
        kernel_size (int): Size of the Gaussian kernel (must be odd and positive).
    """
    # Start the timer
    start_time = time.time()
    
    # Read the image
    image = cv2.imread(input_path)
    if image is None:
        raise ValueError(f"Image not found at path: {input_path}")

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    
    # Save the blurred image
    cv2.imwrite(output_path, blurred_image)

    # End the timer
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Print and log the execution time
    print(f"Execution Time: {execution_time:.2f} seconds")
    logging.info(f"Execution Time: {execution_time:.2f} seconds")

if __name__ == "__main__":
    input_image_path = "example_image.jpg"  # Replace with your image path
    output_image_path = "blurred_image.jpg"
    apply_gaussian_blur(input_image_path, output_image_path)
