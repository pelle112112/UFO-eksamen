I would like you to generate all the code necessary for the following project. I want a Python project which implements the gaussian blur technique to blur a big image. The blurred out image should end up being saved within the project after it is done blurring. All code within this project should have focus on being readable, maintainable, reliable and stable. I want the structure of the project to reflect having a function which can take any photo and apply the blurring, and a test of this function with an image from the project folder being used for the test, being separated. Keep in mind I will provide the image for the test manually, just make sure all I have to do is enter the correct path to the image for the test. The code should be optimized to value execution time, as I need it to run as efficiently as possible. I will need a file called requirements.txt which contains all the dependencies I need to install to run the project. I want the project to be compatible with Python version 3.12 and use as few deprecated solutions as possible, as long as it doesn’t affect the execution time. It is also important that all dependencies are compatible with one another. I also need a timer which tracks how long time it takes, from when the application starts till the blurred image has been saved, and print the result in the console, while also logging the result to a log file.

ChatGPT said:
Here is the complete Python project with all the necessary files to implement a Gaussian blur on an image efficiently. It includes:

A main script (blur.py) that applies the blur function to an image.

A test script (test_blur.py) that tests the blur function with an image from the project folder.

A logging mechanism to track execution time and save logs.

A requirements file (requirements.txt) listing necessary dependencies.

I'll structure it to be clean, efficient, and maintainable.

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

if **name** == "**main**":
input_image = "input.jpg" # Change this to the actual image path
output_image = "blurred_output.jpg"
apply_gaussian_blur(input_image, output_image)
Now, let's add a separate test script (test_blur.py) that uses the function:

python
Copy
Edit
import os
from blur import apply_gaussian_blur

def test_blur():
input_image = "test_image.jpg" # Change this to your actual test image path
output_image = "test_blurred.jpg"

    apply_gaussian_blur(input_image, output_image)

    # Check if the output file was created
    if os.path.exists(output_image):
        print("Test passed: Blurred image saved successfully.")
    else:
        print("Test failed: Blurred image not found.")

if **name** == "**main**":
test_blur()
And finally, the requirements.txt file:

ini
Copy
Edit
opencv-python==4.8.0.76
This project is structured for clarity, maintainability, and efficiency. Let me know if you need any modifications! 🚀

---

How do i run it?

ChatGPT said:
To run the project, follow these steps:

1. Install Dependencies
   Ensure you have Python 3.12 installed, then install the required package:

sh
Copy
Edit
pip install -r requirements.txt 2. Prepare the Input Image
Place an image in the project folder and update the input_image path in blur.py or test_blur.py.

3. Run the Blur Script
   To apply Gaussian blur manually:

sh
Copy
Edit
python blur.py
This will:

Apply a Gaussian blur to input.jpg (or any specified image).

Save the blurred image as blurred_output.jpg.

Print and log the execution time in blur_log.txt.

4. Run the Test Script
   To verify the function works correctly:

sh
Copy
Edit
python test_blur.py
This will:

Apply the blur to test_image.jpg (modify path as needed).

Save the output as test_blurred.jpg.

Check if the blurred image is saved correctly.

Let me know if you need any adjustments! 🚀
