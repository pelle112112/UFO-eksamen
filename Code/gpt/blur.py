import cv2
import time
import logging
from pathlib import Path

def apply_gaussian_blur(image_path: str, output_path: str, kernel_size: tuple = (15, 15)):
    """
    Applies Gaussian blur to an image and saves the output.
    
    :param image_path: Path to the input image
    :param output_path: Path to save the blurred image
    :param kernel_size: Kernel size for Gaussian blur (default is (15,15))
    """
    # Start timer
    start_time = time.time()
    
    # Set up logging
    logging.basicConfig(filename="blur_log.txt", level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        logging.error(f"Failed to load image: {image_path}")
        print("Error: Unable to load image.")
        return
    
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
    
    # Save the blurred image
    cv2.imwrite(output_path, blurred_image)
    
    # End timer
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Print and log execution time
    print(f"Blurring completed in {execution_time:.4f} seconds.")
    logging.info(f"Blurring completed in {execution_time:.4f} seconds. Output saved to {output_path}")

if __name__ == "__main__":
    input_image = "input_image.jpg"  # Change this to the actual image path
    output_image = "blurred_output.jpg"
    apply_gaussian_blur(input_image, output_image)
