# 🖱️ Virtual Mouse using Hand Tracking

Control your mouse using just your fingers and a webcam!  
This project uses **OpenCV**, **MediaPipe**, and **PyAutoGUI** to track your hand in real time and lets you move your mouse cursor or click with a simple pinch gesture.

![image](https://github.com/user-attachments/assets/a7eb78a3-7714-4740-8163-6c1757d8f64d)

![image](https://github.com/user-attachments/assets/4444c200-0434-4091-b96a-52946dcfdc08)



---

## 🚀 Features

✅ Real-time hand tracking using [MediaPipe](https://mediapipe.dev/)  
🖐️ Move your index finger to control the cursor  
🤏 Pinch your thumb and index finger to simulate a mouse click  
🖼️ GUI interface built with Tkinter  
🎯 Visual feedback for pointer and click gesture  
🛑 Start and Stop controls to safely exit

---

---

## 🧠 How It Works

- Captures webcam feed using **OpenCV**
- Detects hand and fingertips using **MediaPipe**
- Converts fingertip positions to screen coordinates using **PyAutoGUI**
- Clicks when thumb and index are close together (with cooldown buffer)

---

## 🛠️ Tech Stack

| Tool          | Description                         |
|---------------|-------------------------------------|
| Python        | Core programming language           |
| OpenCV        | Webcam and image processing         |
| MediaPipe     | Real-time hand landmark detection   |
| PyAutoGUI     | Cursor movement & mouse click       |
| Tkinter       | GUI interface                       |
| Pillow        | Image handling in GUI               |

---

## 📦 Installation

```bash
git clone https://github.com/your-username/virtual-mouse-hand-tracking.git
cd virtual-mouse-hand-tracking
pip install -r requirements.txt
python app.py
