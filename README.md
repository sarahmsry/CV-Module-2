# CV-Module-2
Computer Vision Spring 2026 Week 2 Module 2 Assignment

# Camera Calibration & Perspective Projection 

This project provides tools for camera calibration and real-world measurement using perspective projection. It allows you to calibrate your camera with chessboard images, select object corners in your own photos, and compute real-world dimensions of objects from images.

## Features

- **Camera Calibration:**  
  Calibrate camera using chessboard images to obtain intrinsic parameters and distortion coefficients.

- **Interactive Corner Selection:**  
  Select two corners of an object in your image using a simple click interface.

- **Real-World Measurement:**  
  Calculate the real-world width and height of objects in your images using perspective projection equations.

## Requirements

- Python 3.x  
- OpenCV (`opencv-python`)
- NumPy

Install dependencies with:
```sh
pip install opencv-python numpy
```

## Usage

### 1. Camera Calibration

1. Place chessboard calibration images in the `calibration_images/` folder.
2. Run the calibration script:
    ```sh
    python camera_calibration.py
    ```
   This will generate a `calibration_data.npz` file with your camera parameters.

### 2. Measure an Object in Your Image

1. Place your test image (e.g., `test.jpg`) in the project folder.
2. Run the test script:
    ```sh
    python test.py
    ```
3. A window will open. Click on two opposite corners of the object you want to measure.
4. Enter the distance from the camera to the object (in mm, matching your calibration).
5. The script will print the real-world width and height of the object.

### 3. Functions

- `select_corners_from_image(image_path)`:  
  Opens an image and lets you click two corners, returning their pixel coordinates.

- `calculate_object_dimensions(corner1, corner2, Z_distance, fx, fy, cx, cy)`:  
  Calculates real-world width and height from pixel coordinates and camera parameters.

## File Overview

- `camera_calibration.py` — Calibrates the camera using chessboard images.
- `perspective_projection.py` — Contains projection and measurement functions.
- `find_corner_pixels.py` — Interactive tool for selecting object corners in an image and finding the pixel coordinates.
- `test.py` — Example script to measure an object in your image.

## Notes

- Make sure your calibration and measurement units match (e.g., millimeters).
- For best results, use undistorted images for measurement.
- The object should be flat and parallel to the image plane for accurate results.

