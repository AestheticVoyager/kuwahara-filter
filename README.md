This repository contains Python code for performing image processing tasks using the Kuwahara filter.

## Kuwahara Filter

The Kuwahara filter is a non-linear filter used for image smoothing while preserving edges. It divides the image into overlapping square regions and computes the mean and variance of pixel values within each region. Then, it selects the region with the smallest variance and replaces all pixels within that region with the mean value of those pixels.

### Usage

To use the Kuwahara filter, simply call the `kuwahara_color` function with the input image as the argument. The function returns the filtered image.

Example usage:

```Python
import cv2
from kuwahara_filter import kuwahara_color

# Load the image
image_path = 'image.jpg'
orig_img = cv2.imread(image_path)

# Apply Kuwahara filter
kuwahara_filtered = kuwahara_color(orig_img)

# Display or save the filtered image
cv2.imshow('Kuwahara Filtered Image', kuwahara_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the filtered image
output_path = 'filtered_image.jpg'
cv2.imwrite(output_path, kuwahara_filtered)

```

## Requirements

- Python 3.x
- OpenCV (cv2)
- Numba

Install the required packages using pip:
```bash
pip install numpy opencv-python numba
```

## License

This code is provided under the MIT License.