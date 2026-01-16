import customtkinter as ctk
from customtkinter import CTkLabel
from pytubefix import YouTube
import os
class Youtube_Downloader(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Audio / Video Downloader")
        self.geometry("800x500")
        self.configure(fg_color="#2E2A2A")
        self.grid_columnconfigure(0, weight=1)
        self.entry = ctk.CTkEntry(self, placeholder_text="Enter the video link you want to download", justify="center", fg_color="#3C3C3C", placeholder_text_color="white", height=50, font=("Arial", 17, "normal"))
        self.entry.grid(row=1, column=0, padx=40, pady=10, sticky="ew")
        self.button = ctk.CTkButton(self, text = "Download", command=self.ytb_converter, fg_color="#F7F7F7", text_color="black", font= ("Arial", 12, "bold"), hover_color="#D6D6D6", width=200, height=40)
        self.button.grid(padx=25, pady=20)
        self.download_choice = ctk.StringVar(value="audio")
        self.radio_audio = ctk.CTkRadioButton(self, text="Audio", variable=self.download_choice, value="audio")
        self.radio_audio.grid(padx=20, pady=5)
        self.radio_audio.configure(corner_radius=8, hover_color="#E0E0E0", text_color="white", fg_color="white", border_width_unchecked = 2, border_width_checked=5, font=("Arial", 15, "bold"))
        self.radio_video = ctk.CTkRadioButton(self, text="Video", variable=self.download_choice, value="video")
        self.radio_video.grid(padx=20, pady=5)
        self.radio_video.configure(corner_radius=8, hover_color="#E0E0E0", text_color="white", fg_color="white", border_width_unchecked = 2, border_width_checked=5, font=("Arial", 15, "bold"))
        self.label = ctk.CTkLabel(self, text="", fg_color="transparent")
        self.label.grid(padx=20, pady=30)

    def ytb_converter(self):
        choice = self.download_choice.get()

        link = self.entry.get()
        self.label.configure(text="Downloading...", text_color="#FAF000", font=("Arial", 20, "bold"))
        self.update_idletasks()
        if choice == "audio":
            try:
                yt = YouTube(link, use_oauth=False, allow_oauth_cache=True)
                stream = yt.streams.filter(only_audio=True).first()
                download_path = os.path.join(os.path.expanduser('~'), "Downloads")
                stream.download(output_path=download_path, filename=f"{yt.title}.mp3")

                self.label.configure(text=f"Download Completed! - {yt.title}.mp3", text_color="green", font=("Arial", 20, "bold"), wraplength= 300)
            except Exception as e:
                self.label.configure(text=f"An error occurred. Try again!", text_color="red", font=("Arial", 20, "bold"))
        elif choice == "video":
            try:
                yt = YouTube(link, use_oauth=False, allow_oauth_cache=True)
                stream = yt.streams.get_highest_resolution()
                download_path = os.path.join(os.path.expanduser('~'), "Downloads")
                stream.download(output_path=download_path, filename=f"{yt.title}.mp4")

                self.label.configure(text=f"Download Completed! - {yt.title}.mp4", text_color="#07E81A", font=("Arial", 20, "bold"), wraplength= 300)
            except Exception as e:
                self.label.configure(text=f"An error occurred. Try again!", text_color="#E80707", font=("Arial", 20, "bold"))
if __name__ == "__main__":
    app = Youtube_Downloader()
    app.mainloop()
