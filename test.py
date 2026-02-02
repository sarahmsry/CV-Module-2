from perspective_projection import calculate_object_dimensions, fx, fy, cx, cy
from find_corner_pixels import select_corners_from_image

image_path = 'test.jpg' 

# Select corners in pop-up window
corners = select_corners_from_image(image_path)
corner1, corner2 = corners[0], corners[1]

Z_distance = 2000    # distance from camera to object plane in mm

width, height = calculate_object_dimensions(corner1, corner2, Z_distance, fx, fy, cx, cy)
print(f"Real-world width: {width:.2f} mm, height: {height:.2f} mm")