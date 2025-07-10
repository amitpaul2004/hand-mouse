import tkinter as tk
from PIL import Image, ImageTk
from virtual_mouse import VirtualMouse
import threading

class VirtualMouseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🖱️ Virtual Mouse Controller")
        self.root.geometry("900x720")
        self.root.configure(bg="#1e1e2f")

        self.video_label = tk.Label(self.root)
        self.video_label.pack(pady=10)

        self.title = tk.Label(self.root, text="Virtual Mouse with Hand Tracking",
                              font=("Helvetica", 20, "bold"), fg="#00f7ff", bg="#1e1e2f")
        self.title.pack()

        self.instruction = tk.Label(self.root, text="👉 Move index finger to control mouse\n🤏 Pinch index & thumb to click\n❌ Press 'Stop' to exit webcam",
                                    font=("Arial", 14), fg="white", bg="#1e1e2f")
        self.instruction.pack(pady=10)

        self.start_btn = tk.Button(self.root, text="▶ Start", font=("Arial", 14),
                                   bg="#33c1ff", fg="black", width=10, command=self.start)
        self.start_btn.pack(side=tk.LEFT, padx=60, pady=20)

        self.stop_btn = tk.Button(self.root, text="⛔ Stop", font=("Arial", 14),
                                  bg="#ff4b5c", fg="white", width=10, command=self.stop)
        self.stop_btn.pack(side=tk.RIGHT, padx=60, pady=20)

        self.vm = None
        self.running = False

    def start(self):
        if not self.running:
            self.vm = VirtualMouse()
            self.running = True
            threading.Thread(target=self.update_frame).start()

    def stop(self):
        self.running = False
        if self.vm:
            self.vm.release()

    def update_frame(self):
        while self.running:
            frame, rgb = self.vm.get_frame()
            if rgb is not None:
                img = Image.fromarray(rgb)
                img = img.resize((800, 600))
                imgtk = ImageTk.PhotoImage(image=img)
                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)

        self.video_label.configure(image="")

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualMouseApp(root)
    root.mainloop()
