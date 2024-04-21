import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

# This is the default source code from YouTube: https://www.youtube.com/watch?v=0hEmxOEeVO0 
# Which is my project reference

def download_video():
    url = entry_url.get()   
    resolution = resolution_var.get()
    progress_label.pack(padx=10, pady=5)
    progress_bar.pack(padx=10, pady=5)
    status_label.pack(padx=10, pady=5)
    
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(res=resolution).first()
        
        #Download the video into a specific path
        os.path.join("downloads", f"{yt.title}.mp4")
        stream.download(output_path="downloads")
        
        status_label.configure(text="Downloaded!", text_color="white", fg_color="green")
    except Exception as e:
        status_label.configure(text=f"Error {str(e)}", text_color="white", fg_color="red")


def convert_next():
    # Reset entry fields
    entry_url.delete(0, ctk.END)
    # Reset combobox
    resolution_combobox.set("720p")
    # Reset status labels
    status_label.configure(text="", fg_color="transparent")
    # Reset progress bar
    progress_label.configure(text="")
    progress_bar.pack_forget()

    

def on_progress(stream, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = bytes_downloaded / total_size * 100   
    
    progress_label.configure(text= str(int(percentage_completed)) + "%")
    progress_label.update()
    
    progress_bar.set(float(percentage_completed / 100))
#Create a root window
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#Title of the window
root.title("YouTube Downloader!")

#Set min and max width and the height
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

#Create a frame to hold the content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

#Create a label and the entry widget for the video url
url_label = ctk.CTkLabel(content_frame, text="Enter the youtube url here: ")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(padx=10, pady=5)
entry_url.pack(padx=10, pady=5)

#Create a download button
download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)
download_button.pack(padx=10, pady=5)

#Create a convert next button
convert_next_button = ctk.CTkButton(content_frame, text="Convert Next", command=convert_next)
convert_next_button.pack(padx=10, pady=5)


#Create a resolution combo box
resolutions = ["720p", "360p", "240p"]
resolution_var = ctk.StringVar()
resolution_combobox = ttk.Combobox(content_frame, values=resolutions, textvariable=resolution_var, state="readonly")
resolution_combobox.pack(padx=10, pady=5)
resolution_combobox.set("720p")

#Create a lable and the progress bar to display the download progress
progress_label = ctk.CTkLabel(content_frame, text="0%")
progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0)

#Create the status label
status_label = ctk.CTkLabel(content_frame, text="")
#To start the app
root.mainloop()