from blur_image import apply_gaussian_blur

def test_blur():
    """
    Test the Gaussian blur function with a sample image.
    """
    input_image_path = "path_to_your_image.jpg"  # Replace with your test image path
    output_image_path = "test_blurred_image.jpg"
    try:
        apply_gaussian_blur(input_image_path, output_image_path)
        print("Test passed: Blurred image saved successfully.")
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    test_blur()
