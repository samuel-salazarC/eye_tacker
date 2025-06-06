import cv2
import mediapipe as mp
import csv
import time

# Initialize MediaPipe Face Mesh with refine_landmarks=True for iris points
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Start webcam capture
cap = cv2.VideoCapture(0)

# Open CSV file to save data
csv_file = open('generated_mockup_data.csv', mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['x', 'y', 'time'])

# Indices for left and right iris landmarks
LEFT_IRIS_LANDMARK = 468
RIGHT_IRIS_LANDMARK = 473

print("Press 'q' to stop recording...")

start_time = time.time()

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Failed to capture frame.")
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            height, width, _ = frame.shape
            landmarks = face_landmarks.landmark

            # Check if landmarks include iris points
            if len(landmarks) > RIGHT_IRIS_LANDMARK:
                left_iris = landmarks[LEFT_IRIS_LANDMARK]
                right_iris = landmarks[RIGHT_IRIS_LANDMARK]

                left_x, left_y = int(left_iris.x * width), int(left_iris.y * height)
                right_x, right_y = int(right_iris.x * width), int(right_iris.y * height)

                elapsed_time = round(time.time() - start_time, 2)

                # Save positions and time to CSV
                csv_writer.writerow([left_x, left_y, elapsed_time])
                csv_writer.writerow([right_x, right_y, elapsed_time])

                # Draw circles on screen at iris positions
                cv2.circle(frame, (left_x, left_y), 3, (255, 0, 0), -1)   # Blue circle for left iris
                cv2.circle(frame, (right_x, right_y), 3, (0, 255, 0), -1) # Green circle for right iris

    cv2.imshow('Eye Tracker', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
csv_file.close()
cv2.destroyAllWindows()
