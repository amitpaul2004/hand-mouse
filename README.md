# 🖱️ Virtual Mouse using Hand Tracking

Control your mouse using just your fingers and a webcam!  
This project uses **OpenCV**, **MediaPipe**, and **PyAutoGUI** to track your hand in real time and lets you move your mouse cursor or click with a simple pinch gesture.

![Demo Banner](https://i.imgur.com/JMbkS1I.gif)

---

## 🚀 Features

✅ Real-time hand tracking using [MediaPipe](https://mediapipe.dev/)  
🖐️ Move your index finger to control the cursor  
🤏 Pinch your thumb and index finger to simulate a mouse click  
🖼️ GUI interface built with Tkinter  
🎯 Visual feedback for pointer and click gesture  
🛑 Start and Stop controls to safely exit

---

## 📸 Demo Preview

https://github.com/your-username/virtual-mouse-hand-tracking/assets/demo-video.mp4  
*(Insert your demo video or GIF link above)*

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
