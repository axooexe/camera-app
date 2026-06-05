import os
import time
import cv2
import customtkinter as ctk
from PIL import Image, ImageTk


class CozyCameraApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Configuration 
        self.title("✨ Cozy Camera ✨")
        self.geometry("700x600")
        self.configure(fg_color="#FFF8F0")  

        # Colors
        self.panel_color = "#F4EAE1"       
        self.button_color = "#8A7F81"      
        self.button_hover = "#D1B1B6"      
        self.text_color = "#604D4A"        

        # Camera Setup
        self.video_capture = cv2.VideoCapture(0)
        
        # output directory
        self.output_dir = "my_cozy_photos"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # UI 
        self.create_widgets()

        # Start Camera
        self.update_frame()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(
            self, 
            text="🌸 capture a lovely moment 🌸", 
            font=("Helvetica", 20, "italic"),
            text_color=self.text_color
        )
        self.title_label.pack(pady=15)

        self.feed_frame = ctk.CTkFrame(
            self, 
            width=500, 
            height=375, 
            fg_color=self.panel_color,
            corner_radius=20
        )
        self.feed_frame.pack(pady=10)
        self.feed_frame.pack_propagate(False)

        # where camera image goes
        self.video_label = ctk.CTkLabel(self.feed_frame, text="")
        self.video_label.pack(fill="both", expand=True, padx=10, pady=10)

        # capture button
        self.capture_button = ctk.CTkButton(
            self, 
            text="📸 Take Picture", 
            font=("Helvetica", 16, "bold"),
            fg_color=self.button_color,
            hover_color=self.button_hover,
            text_color="#FFFFFF",
            corner_radius=15,
            height=45,
            command=self.take_snapshot
        )
        self.capture_button.pack(pady=20)

        # Notification
        self.status_label = ctk.CTkLabel(
            self, 
            text="Camera is ready...", 
            font=("Helvetica", 12),
            text_color=self.text_color
        )
        self.status_label.pack(pady=5)

    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            frame = cv2.flip(frame, 1)
            
            frame = cv2.resize(frame, (480, 355))
            
            # Convert colors
            cv2_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(cv2_image)
            
            imgtk = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(480, 355))
            
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
            
        self.after(15, self.update_frame)

    def take_snapshot(self):
        ret, frame = self.video_capture.read()
        if ret:
            frame = cv2.flip(frame, 1)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = os.path.join(self.output_dir, f"cozy_{timestamp}.png")
            
            # Save image
            cv2.imwrite(filename, frame)
            
            # success message
            self.status_label.configure(text=f"✨ Saved to {filename}! ✨")
            
            # Reset message
            self.after(2000, lambda: self.status_label.configure(text="Camera is ready..."))

    def destroy(self):
        self.video_capture.release()
        super().destroy()


if __name__ == "__main__":
    app = CozyCameraApp()
    app.mainloop()
