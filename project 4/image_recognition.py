import cv2

# Load the image
image = cv2.imread("sample.jpg")

if image is None:
    print("Error: sample.jpg not found.")
else:
    print("Image loaded successfully!")

    # Original Image
    cv2.imshow("Original Image", image)

    # Convert to Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray)

    # Edge Detection
    edges = cv2.Canny(gray, 100, 200)
    cv2.imshow("Edge Detection", edges)

    print("Image Recognition Completed Successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()