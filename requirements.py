"""
Gerekli kütüphaneleri otomatik kurar ve günceller.

Kullanım:
    python requirements.py
"""

import subprocess
import sys

PACKAGES = [
    "customtkinter>=5.2.2",
    "yt-dlp>=2024.8.6",
    "imageio-ffmpeg>=0.5.1",
]


def main():
    print("Kütüphaneler kuruluyor, lütfen bekleyin...\n")
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--upgrade", *PACKAGES]
        )
    except subprocess.CalledProcessError:
        print("\nKurulum sırasında hata oluştu. İnternet bağlantınızı kontrol edip tekrar deneyin.")
        sys.exit(1)

    print("\nTüm kütüphaneler başarıyla kuruldu!")
    print("Şimdi programı başlatabilirsiniz: python video_indirici.py")


if __name__ == "__main__":
    main()
