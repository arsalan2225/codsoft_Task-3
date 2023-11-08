import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)  # 0 represents the default camera (you can change it if you have multiple cameras)

if not cap.isOpened():
    print("Error: Camera not found.")
else:
    # Capture a single frame
    ret, frame = cap.read()

    if ret:
        # Save the captured image to a file
        cv2.imwrite("captured_image.jpg", frame)
        print("Image captured and saved as 'captured_image.jpg'")

    # Release the camera
    cap.release()
