import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import yt_dlp
import threading
import os

download_folder = ""

def choose_folder():
    global download_folder
    folder = filedialog.askdirectory()
    if folder:
        download_folder = folder
        folder_label.config(text=f"Selected Folder: {folder}")

def download_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return
    if not download_folder:
        messagebox.showerror("Error", "Please choose a download folder.")
        return

    progress_bar['value'] = 0
    progress_label.config(text="Starting download...")

    def progress_hook(d):
        if d['status'] == 'downloading':
            try:
                percent = float(d.get('_percent_str', '0').strip().replace('%', ''))
                progress_bar['value'] = percent
                progress_label.config(text=f"Downloading: {percent:.1f}%")
            except:
                pass
        elif d['status'] == 'finished':
            progress_bar['value'] = 100
            progress_label.config(text="Download finished!")

    def run_download():
        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
                'progress_hooks': [progress_hook],
                'socket_timeout': 30
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            messagebox.showinfo("Success", "Download completed!")
        except Exception as e:
            progress_label.config(text="Download failed.")
            messagebox.showerror("Download Failed", str(e))

    threading.Thread(target=run_download).start()

# GUI Setup
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x300")
root.resizable(False, False)

label = tk.Label(root, text="Enter YouTube URL:")
label.pack(pady=10)

url_entry = tk.Entry(root, width=58)
url_entry.pack(pady=5)

choose_btn = tk.Button(root, text="Choose Download Folder", command=choose_folder)
choose_btn.pack(pady=10)

folder_label = tk.Label(root, text="No folder selected", fg="gray")
folder_label.pack()

progress_bar = ttk.Progressbar(root, length=350, mode='determinate')
progress_bar.pack(pady=15)

progress_label = tk.Label(root, text="", fg="blue")
progress_label.pack()

download_btn = tk.Button(root, text="Download", command=download_video, bg="green", fg="white", width=20)
download_btn.pack(pady=15)

root.mainloop()
