A real-time face recognition system using OpenCV and face_recognition. It detects faces via webcam, matches them with stored images, and displays the recognized name, roll number, and status. Ideal for attendance tracking and security applications. 🚀

Features
✅ Real-time face detection and recognition
✅ Automatic attendance marking
✅ Uses pre-stored images for identification
✅ Displays name, roll number, and status
✅ Simple UI with OpenCV

Installation

Clone the repository:
git clone https://github.com/your-username/Real-Time-Face-Recognition.git
cd Real-Time-Face-Recognition

Install dependencies:

pip install opencv-python numpy face-recognition

Ensure you have a folder named Images/Images inside the project directory, where each image filename corresponds to the person's name.

Usage
Run the script:

python face_recognition.py
The webcam will open and recognize faces from the stored dataset.

Press 'q' to exit.

Folder Structure

Real-Time-Face-Recognition/
│── Images/               # Folder containing images of known people
│   ├── Ali.jpg  
│   ├── Hassan.jpg  
│   ├── Sara.jpg  
│── face_recognition.py   # Main script
│── README.md  


How It Works
Loads images from the Images/Images folder and encodes faces.
Opens the webcam and detects faces in real-time.
Matches detected faces with stored encodings.
Displays recognized name and roll number.
Contributing
Pull requests are welcome. For major changes, please open an issue first.

License
This project is licensed under the MIT License.

