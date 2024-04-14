import cv2 
import numpy as np
  
# Reads image.
img = cv2.imread('balls.jpg', cv2.IMREAD_COLOR) 

# Converts image to grayscale.
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blurs image
img2 = cv2.medianBlur(img2, 7)

# Applies Hough transform on the blurred image
rows = img2.shape[0]
detected_circles = cv2.HoughCircles(img2,  
                                    cv2.HOUGH_GRADIENT,
                                    1,
                                    (rows / 8),
                                    param1 = 100, 
                                    param2 = 70,
                                    minRadius = 0,
                                    maxRadius = 0) 
  
# Draws circles that are detected
if detected_circles is not None: 
  
    # Converts the circle parameters a, b and r to integers 
    detected_circles = np.uint16(np.around(detected_circles)) 
  
    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2]
  
        # Draws the circles
        cv2.circle(img, (a, b), r, (0, 255, 0), -1)
        cv2.circle(img, (a, b), r, (0, 0, 0), 5) 
  
        # Draws circle coordinates
        cv2.putText(img, "{0}, {1}".format(a, b), (round(a - r * 0.66), b), cv2.FONT_HERSHEY_SIMPLEX, round(r * 0.01), (0, 0, 255), round(r * 0.01)) 

# Shows image and waits for input to close
cv2.imshow("Detected Circles", img)
cv2.waitKey(0)