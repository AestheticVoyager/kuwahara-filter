import numpy as np
import cv2
from numba import jit, prange

@jit(nopython=True)
def kuwahara_color(orig_img, radius=3, sigma=None):
    if orig_img.ndim != 3:
        raise TypeError("Incorrect number of dimensions (expected 3)")
    if not isinstance(radius, int):
        raise TypeError('`radius` must be int')
    if radius < 1:
        raise ValueError('`radius` must be greater or equal to 1')
    image = orig_img.astype(np.float32)
    h, w, c = image.shape
    output = np.empty_like(image)
    for i in range(c):
        for y in prange(radius, h - radius):
            for x in prange(radius, w - radius):
                # Extract the region around the current pixel
                region = image[y - radius:y + radius + 1, x - radius:x + radius + 1, i]
                # Calculate the variance for each quadrant
                quadrants = [
                    region[:radius + 1, :radius + 1],
                    region[:radius + 1, radius:],
                    region[radius:, :radius + 1],
                    region[radius:, radius:]
                ]
                variances = [np.var(q) for q in quadrants]
                # Find the index of the quadrant with the minimum variance
                min_index = 0
                min_variance = variances[0]
                for j in range(1, 4):
                    if variances[j] < min_variance:
                        min_variance = variances[j]
                        min_index = j
                # Take the mean of the pixels in the selected quadrant as the filtered value
                output[y, x, i] = np.mean(quadrants[min_index])
    return output.astype(orig_img.dtype)

if __name__ == "__main__":
    import cv2
    # Load the image
    image_path = './test.JPG'
    orig_img = cv2.imread(image_path)
    # Apply Kuwahara filter
    kuwahara_filtered = kuwahara_color(orig_img)
    # Save the Kuwahara filtered image
    kuwahara_output_path = './kuwahara_filtered.jpg'
    cv2.imwrite(kuwahara_output_path, kuwahara_filtered)
    print("Image saved successfully!")

