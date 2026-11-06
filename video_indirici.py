"""
AI Universal Video Downloader
-----------------------------
Kurulum:
    pip install customtkinter yt-dlp imageio-ffmpeg

Çalıştırma:
    python video_indirici.py
"""

import os
import re
import shutil
import threading
from pathlib import Path
from tkinter import filedialog

import customtkinter as ctk
import yt_dlp


ANSI_RE = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
URL_RE = re.compile(r"^https?://", re.IGNORECASE)


def get_ffmpeg_path():
    """Sistemde kurulu ffmpeg'i, yoksa imageio-ffmpeg ile gelen ffmpeg'i döndürür."""
    system_ffmpeg = shutil.which("ffmpeg")
    if system_ffmpeg:
        return system_ffmpeg
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


def detect_platform(url):
    u = url.lower()
    if "youtube.com/shorts" in u:
        return "YouTube Shorts"
    if "youtube.com" in u or "youtu.be" in u:
        return "YouTube"
    if "instagram.com" in u:
        return "Instagram"
    if "tiktok.com" in u:
        return "TikTok"
    return "Bilinmeyen platform"


def default_download_dir():
    downloads = Path.home() / "Downloads"
    if downloads.exists():
        return str(downloads)
    return str(Path.home())


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title("AI Universal Video Downloader")
        self.geometry("720x520")
        self.minsize(640, 500)

        self.save_dir = default_download_dir()
        self.is_downloading = False

        self.build_ui()

    # ------------------------------------------------------------------ UI
    def build_ui(self):
        self.grid_columnconfigure(0, weight=1)

        # Başlık
        self.title_label = ctk.CTkLabel(
            self,
            text="AI Universal Video Downloader",
            font=ctk.CTkFont(size=30, weight="bold"),
        )
        self.title_label.grid(row=0, column=0, padx=30, pady=(30, 4))

        self.subtitle_label = ctk.CTkLabel(
            self,
            text="YouTube  •  Shorts  •  Instagram  •  TikTok",
            font=ctk.CTkFont(size=13),
            text_color="gray65",
        )
        self.subtitle_label.grid(row=1, column=0, padx=30, pady=(0, 22))

        # URL alanı
        url_frame = ctk.CTkFrame(self, fg_color="transparent")
        url_frame.grid(row=2, column=0, padx=40, sticky="ew")
        url_frame.grid_columnconfigure(0, weight=1)

        self.url_entry = ctk.CTkEntry(
            url_frame,
            placeholder_text="Video veya Shorts linkini buraya yapıştırın...",
            height=50,
            corner_radius=14,
            font=ctk.CTkFont(size=14),
        )
        self.url_entry.grid(row=0, column=0, sticky="ew")

        self.paste_button = ctk.CTkButton(
            url_frame,
            text="Yapıştır",
            width=90,
            height=50,
            corner_radius=14,
            fg_color="gray25",
            hover_color="gray35",
            command=self.paste_from_clipboard,
        )
        self.paste_button.grid(row=0, column=1, padx=(10, 0))

        # Format seçimi (yan yana butonlar)
        self.format_button = ctk.CTkSegmentedButton(
            self,
            values=["MP4 (Video)", "MP3 (Ses)"],
            height=44,
            corner_radius=14,
            font=ctk.CTkFont(size=14, weight="bold"),
        )
        self.format_button.set("MP4 (Video)")
        self.format_button.grid(row=3, column=0, padx=40, pady=(20, 0), sticky="ew")

        # Kaydetme yeri
        folder_frame = ctk.CTkFrame(self, fg_color="transparent")
        folder_frame.grid(row=4, column=0, padx=40, pady=(20, 0), sticky="ew")
        folder_frame.grid_columnconfigure(0, weight=1)

        self.folder_label = ctk.CTkLabel(
            folder_frame,
            text=self.short_path(self.save_dir),
            anchor="w",
            font=ctk.CTkFont(size=13),
            text_color="gray70",
        )
        self.folder_label.grid(row=0, column=0, sticky="ew")

        self.folder_button = ctk.CTkButton(
            folder_frame,
            text="Klasör Seç",
            width=110,
            height=36,
            corner_radius=12,
            fg_color="gray25",
            hover_color="gray35",
            command=self.choose_folder,
        )
        self.folder_button.grid(row=0, column=1, padx=(10, 0))

        # İlerleme çubuğu
        self.progress_bar = ctk.CTkProgressBar(self, height=14, corner_radius=8)
        self.progress_bar.set(0)
        self.progress_bar.grid(row=5, column=0, padx=40, pady=(26, 6), sticky="ew")

        self.status_label = ctk.CTkLabel(
            self,
            text="Hazır",
            font=ctk.CTkFont(size=14),
            text_color="gray70",
            wraplength=600,
        )
        self.status_label.grid(row=6, column=0, padx=40, pady=(0, 10))

        # İNDİR butonu
        self.download_button = ctk.CTkButton(
            self,
            text="İNDİR",
            height=58,
            corner_radius=16,
            font=ctk.CTkFont(size=20, weight="bold"),
            fg_color="#1f8f4e",
            hover_color="#27ae60",
            command=self.start_download,
        )
        self.download_button.grid(row=7, column=0, padx=40, pady=(6, 30), sticky="ew")

    # ------------------------------------------------------------ Yardımcılar
    @staticmethod
    def short_path(path, limit=60):
        text = "Kaydedilecek yer: " + path
        if len(text) > limit + 18:
            text = text[: 18 + 10] + "..." + text[-(limit - 10):]
        return text

    def set_status(self, text, color="gray70"):
        self.status_label.configure(text=text, text_color=color)

    def paste_from_clipboard(self):
        try:
            text = self.clipboard_get()
        except Exception:
            return
        self.url_entry.delete(0, "end")
        self.url_entry.insert(0, text.strip())

    def choose_folder(self):
        if self.is_downloading:
            return
        selected = filedialog.askdirectory(
            title="Kaydedilecek klasörü seçin", initialdir=self.save_dir
        )
        if selected:
            self.save_dir = selected
            self.folder_label.configure(text=self.short_path(self.save_dir))

    def lock_ui(self, locked):
        state = "disabled" if locked else "normal"
        self.download_button.configure(
            state=state, text="İNDİRİLİYOR..." if locked else "İNDİR"
        )
        self.url_entry.configure(state=state)
        self.paste_button.configure(state=state)
        self.folder_button.configure(state=state)
        self.format_button.configure(state=state)

    # ------------------------------------------------------------- İndirme
    def start_download(self):
        if self.is_downloading:
            return

        url = self.url_entry.get().strip()
        if not url or not URL_RE.match(url):
            self.set_status("Lütfen geçerli bir link girin (http:// veya https://).", "#e74c3c")
            return

        if not os.path.isdir(self.save_dir):
            self.set_status("Seçilen klasör bulunamadı, lütfen yeni bir klasör seçin.", "#e74c3c")
            return

        is_mp3 = self.format_button.get() == "MP3 (Ses)"
        platform = detect_platform(url)

        self.is_downloading = True
        self.lock_ui(True)
        self.progress_bar.set(0)
        self.set_status(f"{platform} bağlantısı hazırlanıyor...", "#3498db")

        thread = threading.Thread(
            target=self.download_worker, args=(url, is_mp3), daemon=True
        )
        thread.start()

    def build_options(self, is_mp3):
        ffmpeg_path = get_ffmpeg_path()
        outtmpl = os.path.join(self.save_dir, "%(title).100s [%(id)s].%(ext)s")

        opts = {
            "outtmpl": outtmpl,
            "noplaylist": True,
            "quiet": True,
            "no_warnings": True,
            "noprogress": True,
            "windowsfilenames": True,
            "retries": 5,
            "fragment_retries": 5,
            "progress_hooks": [self.progress_hook],
            "postprocessor_hooks": [self.postprocessor_hook],
        }

        if ffmpeg_path:
            opts["ffmpeg_location"] = ffmpeg_path

        if is_mp3:
            if not ffmpeg_path:
                raise RuntimeError(
                    "MP3 dönüştürme için FFmpeg gerekli. "
                    "Terminale 'pip install imageio-ffmpeg' yazıp programı yeniden başlatın."
                )
            opts["format"] = "bestaudio/best"
            opts["postprocessors"] = [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ]
        else:
            if ffmpeg_path:
                opts["format"] = (
                    "bv*[vcodec^=avc1]+ba[ext=m4a]/bv*[ext=mp4]+ba[ext=m4a]/"
                    "b[ext=mp4]/bv*+ba/b"
                )
                opts["merge_output_format"] = "mp4"
            else:
                opts["format"] = "b[ext=mp4]/b"

        return opts

    def download_worker(self, url, is_mp3):
        try:
            opts = self.build_options(is_mp3)
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
            title = ""
            if isinstance(info, dict):
                title = info.get("title") or ""
            self.after(0, self.on_success, title)
        except Exception as exc:
            message = ANSI_RE.sub("", str(exc)).strip()
            self.after(0, self.on_error, message)

    def progress_hook(self, d):
        status = d.get("status")
        if status == "downloading":
            total = d.get("total_bytes") or d.get("total_bytes_estimate")
            downloaded = d.get("downloaded_bytes", 0)
            if total:
                fraction = max(0.0, min(downloaded / total, 1.0))
            else:
                fraction = 0.0
            speed = d.get("speed")
            speed_text = f" • {speed / 1024 / 1024:.1f} MB/s" if speed else ""
            text = f"İndiriliyor... %{fraction * 100:.0f}{speed_text}"
            self.after(0, self.update_progress, fraction, text, "#3498db")
        elif status == "finished":
            self.after(0, self.update_progress, 1.0, "İndirme bitti, dosya işleniyor...", "#f39c12")

    def postprocessor_hook(self, d):
        if d.get("status") == "started":
            self.after(0, self.update_progress, 1.0, "Dönüştürülüyor / birleştiriliyor...", "#f39c12")

    def update_progress(self, fraction, text, color):
        self.progress_bar.set(fraction)
        self.set_status(text, color)

    def on_success(self, title):
        self.is_downloading = False
        self.lock_ui(False)
        self.progress_bar.set(1)
        name = f"\n{title}" if title else ""
        self.set_status(f"Tamamlandı! ✔{name}", "#2ecc71")

    def on_error(self, message):
        self.is_downloading = False
        self.lock_ui(False)
        self.progress_bar.set(0)
        if len(message) > 220:
            message = message[:220] + "..."
        self.set_status(f"Hata: {message}", "#e74c3c")


if __name__ == "__main__":
    app = App()
    app.mainloop()
