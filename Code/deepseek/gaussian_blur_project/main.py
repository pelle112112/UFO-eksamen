from pathlib import Path
from image_processing.blue_processor import ImageBlurProcessor
from image_processing.timer import Timer

def main():
    """Main function to execute the image blurring process."""
    # Configuration - you should update these paths as needed
    input_image_path = Path("data/input/test_image.jpg")
    output_image_path = Path("data/output/blurred_image.jpg")
    
    # Initialize the blur processor with optimized parameters
    # Larger kernel size and sigma will produce more blur
    blur_processor = ImageBlurProcessor(kernel_size=(15, 15), sigma_x=10)
    
    # Time the entire operation
    with Timer("Image blurring and saving"):
        try:
            # Apply Gaussian blur
            blurred_image = blur_processor.apply_gaussian_blur(input_image_path)
            
            # Save the blurred image
            blur_processor.save_image(blurred_image, output_image_path)
            
            print(f"Successfully processed and saved blurred image to {output_image_path}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()