import os
from blur import apply_gaussian_blur

def test_blur():
    input_image = "input_image.jpg"  # Change this to your actual test image path
    output_image = "test_blurred.jpg"
    
    apply_gaussian_blur(input_image, output_image)

    # Check if the output file was created
    if os.path.exists(output_image):
        print("Test passed: Blurred image saved successfully.")
    else:
        print("Test failed: Blurred image not found.")

if __name__ == "__main__":
    test_blur()
