import cv2
import numpy as np

def nothing(x):
    pass
# Read the TIFF image
img = cv2.imread('H:/VSCODE/1.tiff')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Reduce the noise in the image
img_blur = cv2.GaussianBlur(img_gray, (3, 3), 1.5)  
img_contrast = cv2.convertScaleAbs(img_blur, alpha=1.5, beta=50)  

#use canny to detect edges
edges = cv2.Canny(img_contrast, 255, 0)#use adjusted parameters

# Find contours in the edge-detected image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
    # Create a blank image to draw the filtered contours
edges_cleaned = np.zeros_like(edges)
        
    # Filter and draw contours based on their length
min_length = 50  # Minimum length of contours to keep
for contour in contours:
        if cv2.arcLength(contour, False) > min_length:
            cv2.drawContours(edges_cleaned, [contour], -1, 255, 1)
        

# segmentation of the edges image
contours, _ = cv2.findContours(edges_cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
segmented_image = cv2.drawContours(img, contours, -1, (255, 255, 0), 2)

# Save the segmented image
cv2.imwrite('H:/VSCODE/segmented.tiff', segmented_image)
cv2.destroyAllWindows()


    