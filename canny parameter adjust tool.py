import cv2

def nothing(x):
    pass
# Read the TIFF image
img = cv2.imread('H:/VSCODE/1.tiff')

# Check if the image was successfully loaded
if img is None:
    print("Error: Could not open or find the image.")
else:
    # Display the image
    cv2.imshow('TIFF Image', img)

# get adjusted canny parameters in windows
    lower_slider = 0
    upper_slider = 50
    slider_max = 255

    # Create a window
    cv2.namedWindow("my Window")

    # Create trackbars for Canny edge detection parameters
    cv2.createTrackbar("Lower Threshold", "my Window", lower_slider, slider_max, nothing)
    cv2.createTrackbar("Upper Threshold", "my Window", upper_slider, slider_max, nothing)

    while True:
        # Get current positions of the trackbars
        lower_val = cv2.getTrackbarPos("Lower Threshold", "my Window")
        upper_val = cv2.getTrackbarPos("Upper Threshold", "my Window")

        # Convert the image to grayscale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Reduce the noise in the image
        img_blur = cv2.GaussianBlur(img_gray, (3, 3), 1.5)
        
        #adjust contrast and brightness
        img_contrast = cv2.convertScaleAbs(img_blur, alpha=1.5, beta=50)
    
        # Use Canny to detect edges
        img_canny = cv2.Canny(img_contrast, lower_val, upper_val)

        # Display the edges
        cv2.imshow("my Window", img_canny)

        # Break the loop when any key is pressed
        if cv2.waitKey(30) >= 0:
            break

    cv2.destroyAllWindows()




