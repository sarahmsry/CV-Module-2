import cv2
import numpy as np

# Load camera calibration data
calib_data = np.load('calibration_data.npz')
camera_matrix = calib_data['camera_matrix']
dist_coeffs = calib_data['dist_coeffs']

# Extract intrinsic parameters
fx = camera_matrix[0, 0]  
fy = camera_matrix[1, 1]  
cx = camera_matrix[0, 2]  
cy = camera_matrix[1, 2] 

def pixel_to_world(x_pixel, y_pixel, Z_distance, fx, fy, cx, cy):
    """
    Converts pixel coordinates to real world coordinates at a given Z distance from the camera
    
    Input: 
        x_pixel: pixel x coordinate
        y_pixel: pixel y coordinate
        Z_distance: Distance from camera to object plane (in same units as camera calibration, mm in this case)
        fx: focal length x (in pixels)
        fy: focal length y (in pixels)
        cx: principal point x (in pixels)
        cy: principal point y (in pixels)
    
        Returns:
        X_world, Y_world: real world coordinates in same units as Z_distance (mm in this case)
    """
    X_world = (x_pixel - cx) * Z_distance / fx
    Y_world = (y_pixel - cy) * Z_distance / fy
    return X_world, Y_world


def calculate_object_dimensions(corner1, corner2, Z_distance, fx, fy, cx, cy):
    """
    Computes real world dimensions of object given its pixel coordinates.
    Assumes object is rectangular and lies flat on image plane at specific Z distance (must be known)

    Input: 
        corner1, corner2: (x_pixel, y_pixel) tuples for two opposite corners of the object
        Z_distance: Distance from camera to object plane (in same units as camera calibration, mm in this case)
        fx, fy, cx, cy: Camera intrinsic parameters

    Returns: 
        (width, height) in real-world units
    """
    x1, y1 = corner1
    x2, y2 = corner2
    # Convert both corners to world coordinates
    X1, Y1 = pixel_to_world(x1, y1, Z_distance, fx, fy, cx, cy)
    X2, Y2 = pixel_to_world(x2, y2, Z_distance, fx, fy, cx, cy)
    # Calculate dimensions
    width = abs(X2 - X1)
    height = abs(Y2 - Y1)
    return width, height

