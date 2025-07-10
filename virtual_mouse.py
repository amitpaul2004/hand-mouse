import cv2
import mediapipe as mp
import pyautogui
import math
import time

class VirtualMouse:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.hands = mp.solutions.hands.Hands(max_num_hands=1)
        self.draw = mp.solutions.drawing_utils
        self.screen_w, self.screen_h = pyautogui.size()
        self.last_click_time = 0  # for cooldown

    def get_frame(self):
        success, frame = self.cap.read()
        if not success:
            return None, None

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                lm = handLms.landmark
                index_tip = lm[8]
                thumb_tip = lm[4]

                # Cursor coordinates
                x, y = int(index_tip.x * w), int(index_tip.y * h)
                screen_x = int(index_tip.x * self.screen_w)
                screen_y = int(index_tip.y * self.screen_h)
                pyautogui.moveTo(screen_x, screen_y)

                # Distance for pinch
                tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)
                distance = math.hypot(tx - x, ty - y)

                # Visualize pointer
                cv2.circle(frame, (x, y), 15, (0, 255, 255), -1)

                # Click with cooldown
                if distance < 40:
                    if time.time() - self.last_click_time > 0.7:
                        pyautogui.click()
                        self.last_click_time = time.time()
                        cv2.circle(frame, ((x + tx)//2, (y + ty)//2), 20, (0, 255, 0), -1)

                self.draw.draw_landmarks(frame, handLms, mp.solutions.hands.HAND_CONNECTIONS)

        return frame, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    def release(self):
        self.cap.release()
