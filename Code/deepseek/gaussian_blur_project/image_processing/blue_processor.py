import cv2
import numpy as np
from pathlib import Path
from typing import Union, Tuple
from .timer import Timer

class ImageBlurProcessor:
    """A class to handle Gaussian blur operations on images with performance optimization."""
    
    def __init__(self, kernel_size: Tuple[int, int] = (5, 5), sigma_x: float = 0):
        """
        Initialize the blur processor with Gaussian blur parameters.
        
        Args:
            kernel_size: Size of the Gaussian kernel (width, height). 
                        Both values should be positive and odd.
            sigma_x: Gaussian kernel standard deviation in X direction.
        """
        self.kernel_size = kernel_size
        self.sigma_x = sigma_x
    
    @Timer.time_it
    def apply_gaussian_blur(self, image_path: Union[str, Path]) -> np.ndarray:
        """
        Apply Gaussian blur to the image at the given path.
        
        Args:
            image_path: Path to the input image file.
            
        Returns:
            The blurred image as a NumPy array.
        """
        # Read the image
        image = cv2.imread(str(image_path))
        
        if image is None:
            raise ValueError(f"Could not read image from {image_path}")
            
        # Apply Gaussian blur
        blurred_image = cv2.GaussianBlur(
            image, 
            self.kernel_size, 
            self.sigma_x
        )
        
        return blurred_image
    
    @Timer.time_it
    def save_image(self, image: np.ndarray, output_path: Union[str, Path]) -> None:
        """
        Save the image to the specified path.
        
        Args:
            image: Image data as a NumPy array.
            output_path: Path where the image will be saved.
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        success = cv2.imwrite(str(output_path), image)
        if not success:
            raise RuntimeError(f"Failed to save image to {output_path}")