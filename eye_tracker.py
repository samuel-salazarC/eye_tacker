import cv2
import mediapipe as mp
import csv
import time

# Inicializa MediaPipe Face Mesh con refine_landmarks=True para puntos del iris
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Inicia la cámara
cap = cv2.VideoCapture(0)

# Archivo CSV para guardar datos
csv_file = open('datos_mockup_generado.csv', mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['x', 'y', 'time'])

# Índices para iris izquierdo y derecho
LEFT_EYE_LANDMARK = 468
RIGHT_EYE_LANDMARK = 473

print("Presiona 'q' para detener la grabación...")

start_time = time.time()

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("No se pudo capturar el frame.")
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            h, w, _ = frame.shape
            landmarks = face_landmarks.landmark

            # Verifica que existan los landmarks de los iris
            if len(landmarks) > RIGHT_EYE_LANDMARK:
                left = landmarks[LEFT_EYE_LANDMARK]
                right = landmarks[RIGHT_EYE_LANDMARK]

                lx, ly = int(left.x * w), int(left.y * h)
                rx, ry = int(right.x * w), int(right.y * h)

                elapsed_time = round(time.time() - start_time, 2)

                # Guardar posiciones y tiempo en CSV
                csv_writer.writerow([lx, ly, elapsed_time])
                csv_writer.writerow([rx, ry, elapsed_time])

                # Dibujar círculos en pantalla
                cv2.circle(frame, (lx, ly), 3, (255, 0, 0), -1)
                cv2.circle(frame, (rx, ry), 3, (0, 255, 0), -1)

    cv2.imshow('Eye Tracker', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
csv_file.close()
cv2.destroyAllWindows()
