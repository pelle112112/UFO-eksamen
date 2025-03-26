def apply_gaussian_blur(image_path: str, output_path: str, blur_radius: int = 5) -> None:
    from PIL import Image, ImageFilter
    import logging

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Apply Gaussian blur
            blurred_image = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))
            # Save the blurred image
            blurred_image.save(output_path)
            logging.info(f"Blurred image saved to {output_path}")
    except Exception as e:
        logging.error(f"An error occurred while processing the image: {e}")