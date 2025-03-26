import unittest
from PIL import Image
from src.blur import apply_gaussian_blur
import os

class TestGaussianBlur(unittest.TestCase):
    def setUp(self):
        self.input_image_path = os.path.join('images', 'input.jpg')
        self.output_image_path = os.path.join('images', 'output.jpg')

    def test_apply_gaussian_blur(self):
        # Apply Gaussian blur to the input image
        apply_gaussian_blur(self.input_image_path, self.output_image_path)

        # Check if the output image was created
        self.assertTrue(os.path.exists(self.output_image_path))

        # Load the original and blurred images
        original_image = Image.open(self.input_image_path)
        blurred_image = Image.open(self.output_image_path)

        # Ensure the blurred image is not the same as the original
        self.assertNotEqual(original_image.tobytes(), blurred_image.tobytes())

if __name__ == '__main__':
    unittest.main()