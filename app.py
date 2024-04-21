import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

class VideoDownloaderFrame(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.create_widgets()

    def create_widgets(self):
        # Create a label and the entry widget for the video url
        url_label = ctk.CTkLabel(self, text="Enter the YouTube URL here: ")
        url_label.pack(padx=10, pady=5)
        self.entry_url = ctk.CTkEntry(self, placeholder_text="Paste YouTube Link Here...", corner_radius=16, width=400, height=40)
        self.entry_url.pack(padx=10, pady=5)

        # Create a download button
        download_button = ctk.CTkButton(self, text="Download Video", font=("Arial", 12), corner_radius=32, fg_color="transparent", border_color="blue", border_width=2, command=self.download_video)
        download_button.pack(padx=10, pady=5)

        # Create a convert next button
        convert_next_button = ctk.CTkButton(self, text="Convert Next", font=("Arial", 12), corner_radius=32, fg_color="transparent", border_color="Blue", border_width=2, command=self.convert_next)
        convert_next_button.pack(padx=10, pady=20)
        
        # Create a resolution combo box
        resolutions = ["720p", "360p", "240p"]
        self.resolution_var = ctk.StringVar()
        resolution_combobox = ttk.Combobox(self, values=resolutions, textvariable=self.resolution_var, state="readonly")
        resolution_combobox.pack(padx=10, pady=5)
        resolution_combobox.set("720p")

        # Create the progress bar to display the download progress
        self.progress_label = ctk.CTkLabel(self, text="0%")
        self.progress_bar = ctk.CTkProgressBar(self, width=400)
        self.progress_bar.set(0)

        # Create the status label
        self.status_label = ctk.CTkLabel(self, text="")

    def download_video(self):
        url = self.entry_url.get()
        resolution = self.resolution_var.get()
        self.progress_label.pack(padx=10, pady=5)
        self.progress_bar.pack(padx=10, pady=5)
        self.status_label.pack(padx=10, pady=5)

        try:
            yt = YouTube(url, on_progress_callback=self.on_progress)
            stream = yt.streams.filter(res=resolution).first() # Pytube functions to download Video

            # Download the video into a specific path
            os.path.join("downloads", f"{yt.title}.mp4")
            stream.download(output_path="downloads")

            self.status_label.configure(text="Downloaded!", corner_radius=16, text_color="white", fg_color="green")
        except Exception as e:
            self.status_label.configure(text=f"Error {str(e)}", corner_radius=16, text_color="white", fg_color="red")

    def on_progress(self, stream, chunk, bytes_remaining):
        # Calculating the downloaded percentage
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_completed = bytes_downloaded / total_size * 100

        # Setting up the progress bar
        self.progress_label.configure(text=str(int(percentage_completed)) + "%")
        self.progress_label.update()

        self.progress_bar.set(float(percentage_completed / 100))

    def convert_next(self):
        # Reset entry fields
        self.entry_url.delete(0, ctk.END)
        # Reset combobox
        self.resolution_var.set("720p")
        # Reset status labels
        self.status_label.configure(text="", fg_color="transparent")
        # Reset progress bar
        self.progress_label.configure(text="")
        self.progress_bar.pack_forget()

class AudioDownloaderFrame(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.create_widgets()

    def create_widgets(self):
        # Create a label and the entry widget for the video url
        url_label = ctk.CTkLabel(self, text="Enter the YouTube URL here: ")
        url_label.pack(padx=10, pady=5)
        self.entry_url = ctk.CTkEntry(self, width=400, height=40, corner_radius=16, placeholder_text="Paste YouTube Link Here...")
        self.entry_url.pack(padx=10, pady=5)

        # Create a download button for MP3
        download_mp3_button = ctk.CTkButton(self, text="Download MP3", corner_radius=32, fg_color="transparent", border_color="blue", border_width=2, command=self.download_mp3)
        download_mp3_button.pack(padx=10, pady=5)
        
        # Create a convert next button
        convert_next_button = ctk.CTkButton(self, text="Convert Next", font=("Arial", 12), corner_radius=32, fg_color="transparent", border_color="Blue", border_width=2, command=self.convert_next)
        convert_next_button.pack(padx=10, pady=20)
        
        # Create an audio quality combo box
        audio_qualities = ["160kbps", "128kbps", "70kbps", "50kbps"]
        self.audio_quality_var = ctk.StringVar()
        audio_quality_combobox = ttk.Combobox(self, values=audio_qualities, textvariable=self.audio_quality_var, state="readonly")
        audio_quality_combobox.pack(padx=10, pady=5)
        audio_quality_combobox.set("160kbps")
        
        # Create the progress bar to display the download progress
        self.progress_label = ctk.CTkLabel(self, text="0%")
        self.progress_bar = ctk.CTkProgressBar(self, width=400)
        self.progress_bar.set(0)

        # Create the status label
        self.status_label = ctk.CTkLabel(self, text="")

    def download_mp3(self):
        url = self.entry_url.get()
        audio_quality = self.audio_quality_var.get()
        self.progress_label.pack(padx=10, pady=5)
        self.progress_bar.pack(padx=10, pady=5)
        self.status_label.pack(padx=10, pady=5)

        try:
            yt = YouTube(url, on_progress_callback=self.on_progress)
            stream = yt.streams.filter(only_audio=True, abr=audio_quality).first() # Pytube function to download Audio

            # Download the audio into a specific path
            os.path.join("audios", f"{yt.title}.mp3")
            stream.download(output_path="audios")
            

            self.status_label.configure(text="Downloaded!", corner_radius=16, text_color="white", fg_color="green")
        except Exception as e:
            self.status_label.configure(text=f"Error {str(e)}", corner_radius=16, text_color="white", fg_color="red")
            
    def on_progress(self, stream, chunk, bytes_remaining):
        # Calculating the downloaded percentage
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_completed = bytes_downloaded / total_size * 100

        # Setting up the progress bar
        self.progress_label.configure(text=str(int(percentage_completed)) + "%")
        self.progress_label.update()

        self.progress_bar.set(float(percentage_completed / 100))
        
    def convert_next(self):
        # Reset entry fields
        self.entry_url.delete(0, ctk.END)
        # Reset status labels
        self.status_label.configure(text="", fg_color="transparent")
        # Reset progress bar
        self.progress_label.configure(text="")
        self.progress_bar.pack_forget()

class MyTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create tabs
        self.add("Video")
        self.add("Audio")

        # Add video downloader frame on video tab
        self.video_downloader_frame = VideoDownloaderFrame(master=self.tab("Video"))
        self.video_downloader_frame.pack(padx=90, pady=50)

        # Add audio downloader frame on audio tab
        self.audio_downloader_frame = AudioDownloaderFrame(master=self.tab("Audio"))
        self.audio_downloader_frame.pack(padx=90, pady=50)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.tab_view = MyTabView(master=self)
        self.tab_view.pack(padx=200, pady=300)

app = App()
app.title("MP34tube Downloader")
app.mainloop()
