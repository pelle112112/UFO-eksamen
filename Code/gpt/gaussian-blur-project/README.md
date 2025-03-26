# Gaussian Blur Project

This project implements the Gaussian blur technique to blur images using Python. It is structured to provide a clear and maintainable codebase, with a focus on readability and efficiency.

## Project Structure

```
gaussian-blur-project
├── src
│   ├── main.py          # Entry point of the application
│   ├── blur.py          # Contains the Gaussian blur function
│   ├── utils
│   │   └── timer.py     # Timer utility for measuring execution time
├── tests
│   └── test_blur.py     # Unit tests for the blur function
├── images
│   ├── input.jpg        # Input image to be blurred (replace with your own)
│   └── output.jpg       # Output image after applying Gaussian blur
├── logs
│   └── execution.log     # Log file for execution time
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd gaussian-blur-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application and apply Gaussian blur to an image, execute the following command:

```
python src/main.py
```

Make sure to replace `images/input.jpg` with your own image file that you want to blur. The blurred image will be saved as `images/output.jpg`.

## Logging

The execution time of the application will be logged in `logs/execution.log`. This file will contain the start time, end time, and total elapsed time for the blurring process.

## Gaussian Blur Technique

Gaussian blur is a widely used image processing technique that smooths images by reducing noise and detail. It works by averaging the pixels around a target pixel, weighted by a Gaussian function. This results in a softening effect that can be useful for various applications, such as background blurring in photography or image preprocessing in computer vision tasks.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.