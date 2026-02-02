import cv2

def select_corners_from_image(image_path):
    """
    Allows user to click on two corners in the image and returns their pixel coordinates.
    
    Input:
        image_path: Path to the image file.
    """
    image_path = 'test.jpg'  
    img = cv2.imread(image_path)
    points = []

    # Resize for display if image is too large
    max_dim = 1000  # Max width or height for display
    h, w = img.shape[:2]
    scale = 1.0
    if max(h, w) > max_dim:
        scale = max_dim / max(h, w)
        display_img = cv2.resize(img, (int(w * scale), int(h * scale)))
    else:
        display_img = img.copy()

    # 
    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            # Scale coordinates back to original image size
            orig_x = int(x / scale)
            orig_y = int(y / scale)
            points.append((orig_x, orig_y)) 
            print(f"Point {len(points)}: ({orig_x}, {orig_y})")
            cv2.circle(display_img, (x, y), 5, (0, 255, 0), -1)
            cv2.imshow('image', display_img)

    cv2.imshow('image', display_img)
    cv2.setMouseCallback('image', click_event)

    print("Click on the two opposite corners of your object in the image window.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return points
    