

# 🎬 YouTube Video Downloader (GUI)
A lightweight, user-friendly **YouTube video downloader** built with **Tkinter GUI** and powered by 'yt-dlp'. Download your favorite videos in the best quality with real-time progress feedback and a clean graphical interface.


## 📌 Features
- GUI interface using **Tkinter**
- Downloads YouTube videos in **best available quality**
- Real-time **progress bar** and percentage display
- Folder picker for custom save locations
- Threaded download to prevent GUI freezing



## 🛠 Requirements
- Python 3.7+
- Modules:
  - `yt-dlp`
  - `tkinter` *(comes with standard Python)*

### 📦 Install Dependencies

pip install yt-dlp



## ▶️ How to Run
Save the code as `main.py`, then run:

python main.py


1. Enter the **YouTube URL**.
2. Choose the **download folder**.
3. Click **Download**.
4. Watch progress — enjoy your video!

---

## 💻 How to Build an Executable (.exe)
Convert this into a standalone desktop app using **PyInstaller**:

### 🔧 Step-by-Step
1. **Install PyInstaller**:

pip install pyinstaller


2. **Build the Executable**:

pyinstaller --onefile --windowed downloader.py


- `--onefile`: Create a single `.exe` file
- `--windowed`: Hides the terminal window (good for GUI apps)

3. Find the `.exe` in the `dist/` directory:

dist/
└── downloader.exe


4. 🎉 Share it with friends — no Python required on their end!



## 🧠 Notes
- Avoid closing the app mid-download; progress updates are threaded.
- Handles basic network errors and malformed URLs.
- Downloads are saved using video title as filename.


> "Simplify your downloads. One click. One video. Done."
