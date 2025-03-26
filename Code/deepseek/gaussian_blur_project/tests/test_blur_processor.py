import unittest
from pathlib import Path
import cv2
import numpy as np

from image_processing.blur_processor import ImageBlurProcessor

class TestImageBlurProcessor(unittest.TestCase):
    """Test cases for the ImageBlurProcessor class."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures."""
        # You should place your test image in data/input/ before running tests
        cls.test_image_path = Path("data/input/test_image.jpg")
        cls.output_path = Path("data/output/blurred_image.jpg")
        cls.blur_processor = ImageBlurProcessor(kernel_size=(15, 15), sigma_x=10)
    
    def test_apply_gaussian_blur(self):
        """Test that Gaussian blur is correctly applied."""
        # Ensure the test image exists
        if not self.test_image_path.exists():
            self.skipTest(f"Test image not found at {self.test_image_path}")
        
        # Apply blur
        blurred_image = self.blur_processor.apply_gaussian_blur(self.test_image_path)
        
        # Verify the output
        self.assertIsInstance(blurred_image, np.ndarray)
        self.assertEqual(blurred_image.ndim, 3)  # Should be a color image
        
    def test_save_image(self):
        """Test that the image can be saved successfully."""
        if not self.test_image_path.exists():
            self.skipTest(f"Test image not found at {self.test_image_path}")
        
        # Get a blurred image
        blurred_image = self.blur_processor.apply_gaussian_blur(self.test_image_path)
        
        # Save the image
        self.blur_processor.save_image(blurred_image, self.output_path)
        
        # Verify the file was created
        self.assertTrue(self.output_path.exists())
        
        # Clean up
        self.output_path.unlink()

if __name__ == "__main__":
    unittest.main()