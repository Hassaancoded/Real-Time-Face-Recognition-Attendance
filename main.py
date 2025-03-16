import cv2
import numpy as np
import face_recognition
import os

# Load images and names from the "Images" folder
path = 'Images/Images'
images = []
names = []
roll_numbers = {
    "Ali": "21-SE-100",
    "Hassan": "090",  
    "Sara": "21-SE-102"
}


image_list = os.listdir(path)

for img in image_list:
    cur_img = cv2.imread(f'{path}/{img}')
    images.append(cur_img)
    names.append(os.path.splitext(img)[0])  # Extract name from filename

# Function to encode faces
def encode_faces(images):
    encode_list = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list

known_encodings = encode_faces(images)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # Resize for faster processing
    small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    faces_in_frame = face_recognition.face_locations(small_frame)
    encodings_in_frame = face_recognition.face_encodings(small_frame, faces_in_frame)

    # Create a blank canvas (black) for displaying details
    canvas_height = frame.shape[0]
    canvas_width = 300  # Adjust width based on text size
    canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

    recognized_name = "Unknown"
    recognized_roll = "----"

    for face_encoding, face_location in zip(encodings_in_frame, faces_in_frame):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            recognized_name = names[best_match_index]
            recognized_roll = roll_numbers.get(recognized_name, "Unknown")

            # Draw rectangle around the face
            y1, x2, y2, x1 = face_location
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4  # Scale back up
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Display recognized person's details on the canvas
    cv2.putText(canvas, "Recognized:", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(canvas, f"Name: {recognized_name}", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(canvas, f"Roll No: {recognized_roll}", (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(canvas, "Status: Present", (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # Concatenate frame and canvas
    combined_frame = np.hstack((frame, canvas))

    cv2.imshow('Face Recognition', combined_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
