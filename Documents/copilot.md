I would like you to generate all the code necessary for the following project. I want a Python project which implements the gaussian blur technique to blur a big image. The blurred out image should end up being saved within the project after it is done blurring. All code within this project should have focus on being readable, maintainable, reliable and stable. I want the structure of the project to reflect having a function which can take any photo and apply the blurring, and a test of this function with an image from the project folder being used for the test, being separated. Keep in mind I will provide the image for the test manually, just make sure all I have to do is enter the correct path to the image for the test. The code should be optimized to value execution time, as I need it to run as efficiently as possible. I will need a file called requirements.txt which contains all the dependencies I need to install to run the project. I want the project to be compatible with Python version 3.12 and use as few deprecated solutions as possible, as long as it doesn’t affect the execution time. It is also important that all dependencies are compatible with one another. I also need a timer which tracks how long time it takes, from when the application starts till the blurred image has been saved, and print the result in the console, while also logging the result to a log file.
Here's a Python project that implements your requirements:

Project Structure
gaussian_blur_project/
│
├── blur_image.py # Main file with the blurring function and timer
├── test_blur.py # Test file
├── requirements.txt # Dependencies
├── logs/ # Folder to store logs
│ └── execution_time.log # Log file for execution time
blur_image.py
python
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
""" # Start the timer
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

if **name** == "**main**":
input_image_path = "path_to_your_image.jpg" # Replace with your image path
output_image_path = "blurred_image.jpg"
apply_gaussian_blur(input_image_path, output_image_path)
test_blur.py
python
from blur_image import apply_gaussian_blur

def test_blur():
"""
Test the Gaussian blur function with a sample image.
"""
input_image_path = "path_to_your_image.jpg" # Replace with your test image path
output_image_path = "test_blurred_image.jpg"
try:
apply_gaussian_blur(input_image_path, output_image_path)
print("Test passed: Blurred image saved successfully.")
except Exception as e:
print(f"Test failed: {e}")

if **name** == "**main**":
test_blur()
requirements.txt
opencv-python==4.5.5.64
Notes:
Performance: The use of cv2.GaussianBlur ensures efficiency for blurring operations, as OpenCV is highly optimized for such tasks.

Compatibility: The dependencies are aligned to be compatible with Python 3.12.

Logging: Logs are stored in logs/execution_time.log, ensuring easy access and maintainability.

Test: Place your test image in the project folder and provide the correct path in test_blur.py.

Let me know if you need any further customizations!

---

How do i run it?
Here’s how you can run the project step by step:

Install Python 3.12: Ensure you have Python 3.12 installed on your system. You can download it from the official Python website.

Install Dependencies:

Navigate to the project folder where requirements.txt is located.

Open a terminal or command prompt and run:

pip install -r requirements.txt
This will install the necessary libraries, including OpenCV.

Run the Main Script (blur_image.py):

Open the file blur_image.py in a text editor and update the input_image_path to point to your input image. For example:

python
input_image_path = "example_image.jpg" # Replace with your actual image file
In the same file, update output_image_path to define where the blurred image should be saved. For example:

python
output_image_path = "blurred_example.jpg"
Save the changes.

In the terminal, run the script with:

python blur_image.py
Test the Functionality (test_blur.py):

Open the test_blur.py file and update the input_image_path with the path to your test image. For example:

python
input_image_path = "test_image.jpg" # Replace with your test image file
Save the changes.

Run the test with:

python test_blur.py
Review Logs:

After running the main script or test, you’ll find the execution time logged in the logs/execution_time.log file.

You can open this file in any text editor to review the logged details.

Once everything is set up, the application should blur your image efficiently and save it in the location you specified. If you run into any issues or need further assistance, let me know!
