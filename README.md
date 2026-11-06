<div align="center">

# 🎬 AI Universal Video Downloader

### Download videos and audio from YouTube, Shorts, Instagram & TikTok, in one sleek dark-mode app.

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-1f6aa5)
![yt-dlp](https://img.shields.io/badge/Powered%20by-yt--dlp-red)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

**🌍 English** | [🇹🇷 Türkçe](README.tr.md)

</div>

---

## ✨ Features

| | Feature |
|---|---|
| 🌑 | Modern **dark mode** interface with rounded corners (CustomTkinter) |
| ▶️ | **YouTube** videos and **YouTube Shorts** |
| 📸 | **Instagram** Reels and videos |
| 🎵 | **TikTok** videos |
| 🎞️ | Choose **MP4 (Video)** or **MP3 (Audio only)** |
| 📁 | Pick your save folder (defaults to your **Downloads** folder) |
| ⚡ | Runs in the background with **threading**, so the window never freezes |
| 📊 | Live **progress bar**, speed and status messages |
| 🔧 | **FFmpeg included automatically** via `imageio-ffmpeg`, with no manual setup |

---

## 🚀 Quick Start

### 1️⃣ Requirements

- **Python 3.9 or newer** → [Download Python](https://www.python.org/downloads/)
  *(On Windows, tick **"Add Python to PATH"** during installation.)*

### 2️⃣ Get the project

```bash
git clone https://github.com/YOUR_USERNAME/ai-universal-video-downloader.git
cd ai-universal-video-downloader
```

Or click **Code → Download ZIP** on GitHub and extract it.

### 3️⃣ Install the dependencies

Choose **one** of these:

```bash
# Option A: automatic installer script
python requirements.py
```

```bash
# Option B: standard pip
pip install -r requirements.txt
```

### 4️⃣ Run the app

```bash
python video_indirici.py
```

That's it! 🎉

---

## 🖱️ How to Use

1. **Paste** a video link into the URL box (or press the **Paste** button).
2. Select **MP4 (Video)** or **MP3 (Audio)**.
3. Optionally click **Select Folder** to change where files are saved.
4. Press the big green **İNDİR** (Download) button.
5. Watch the progress bar. When you see **"Tamamlandı! ✔"**, your file is ready.

---

## 📂 Project Structure

```
ai-universal-video-downloader/
├── video_indirici.py    # Main application
├── requirements.txt     # Dependency list (pip)
├── requirements.py      # One-click dependency installer
├── README.md            # English documentation
└── README.tr.md         # Turkish documentation
```

---

## 🛠️ Tech Stack

- [**Python**](https://www.python.org/): core language
- [**CustomTkinter**](https://github.com/TomSchimansky/CustomTkinter): modern GUI
- [**yt-dlp**](https://github.com/yt-dlp/yt-dlp): downloading engine
- [**imageio-ffmpeg**](https://github.com/imageio/imageio-ffmpeg): bundled FFmpeg for MP3 conversion and merging video + audio

---

## ❓ Troubleshooting

| Problem | Solution |
|---|---|
| Download suddenly stops working | Platforms change often. Update the engine: `pip install -U yt-dlp` |
| `ModuleNotFoundError` | Dependencies are missing. Run `python requirements.py` again |
| Instagram says login required | Some Instagram content (especially private accounts) requires you to be logged in. This is a platform restriction |
| MP3 conversion error | Run `pip install -U imageio-ffmpeg`, or install FFmpeg system-wide |
| Linux: `No module named tkinter` | Run `sudo apt install python3-tk` |
| `python` not recognized | Try `python3`, or reinstall Python with **"Add to PATH"** checked |

---

## ⚠️ Disclaimer

This tool is intended for **personal use** with content you own or have permission to download. Respect the terms of service of each platform and applicable copyright laws. The developers are not responsible for any misuse.

---

## 🤝 Contributing

Ideas and pull requests are welcome! Found a bug? Open an **Issue**.

If you like this project, please give it a ⭐, it really helps!

---

<div align="center">

Made with ❤️ and a little help from AI

</div>
