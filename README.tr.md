<div align="center">

# 🎬 AI Universal Video Downloader

### YouTube, Shorts, Instagram ve TikTok'tan video ve ses indirin: şık, karanlık modlu tek bir uygulamada.

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/Aray%C3%BCz-CustomTkinter-1f6aa5)
![yt-dlp](https://img.shields.io/badge/Altyap%C4%B1-yt--dlp-red)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/Lisans-MIT-green)

[🌍 English](README.md) | **🇹🇷 Türkçe**

</div>

---

## ✨ Özellikler

| | Özellik |
|---|---|
| 🌑 | Yuvarlatılmış köşeli, modern **karanlık mod** arayüz (CustomTkinter) |
| ▶️ | **YouTube** videoları ve **YouTube Shorts** |
| 📸 | **Instagram** Reels ve videoları |
| 🎵 | **TikTok** videoları |
| 🎞️ | **MP4 (Video)** veya **MP3 (Sadece Ses)** seçeneği |
| 📁 | Kaydetme klasörünü seçme (varsayılan: **İndirilenler** klasörü) |
| ⚡ | **Thread** ile arka planda çalışır, pencere asla donmaz |
| 📊 | Canlı **ilerleme çubuğu**, hız ve durum bilgisi |
| 🔧 | `imageio-ffmpeg` sayesinde **FFmpeg otomatik gelir**, elle kurulum gerekmez |

---

## 🚀 Hızlı Başlangıç

### 1️⃣ Gereksinimler

- **Python 3.9 veya üzeri** → [Python'u indir](https://www.python.org/downloads/)
  *(Windows'ta kurulum sırasında **"Add Python to PATH"** kutusunu işaretlemeyi unutmayın.)*

### 2️⃣ Projeyi indirin

```bash
git clone https://github.com/YOUR_USERNAME/ai-universal-video-downloader.git
cd ai-universal-video-downloader
```

Ya da GitHub'da **Code → Download ZIP** diyerek indirip klasöre çıkarın.

### 3️⃣ Kütüphaneleri kurun

Aşağıdakilerden **birini** seçin:

```bash
# Seçenek A: otomatik kurulum betiği (önerilen)
python requirements.py
```

```bash
# Seçenek B: standart pip
pip install -r requirements.txt
```

### 4️⃣ Programı çalıştırın

```bash
python video_indirici.py
```

Hepsi bu kadar! 🎉

---

## 🖱️ Nasıl Kullanılır?

1. Video linkini URL kutusuna **yapıştırın** (ya da **Yapıştır** butonuna basın).
2. **MP4 (Video)** veya **MP3 (Ses)** seçeneğini işaretleyin.
3. İsterseniz **Klasör Seç** butonuyla kaydedilecek yeri değiştirin.
4. Büyük yeşil **İNDİR** butonuna basın.
5. İlerleme çubuğunu izleyin. **"Tamamlandı! ✔"** yazısını gördüğünüzde dosyanız hazırdır.

---

## 📂 Proje Yapısı

```
ai-universal-video-downloader/
├── video_indirici.py    # Ana uygulama
├── requirements.txt     # Kütüphane listesi (pip)
├── requirements.py      # Tek tıkla kurulum betiği
├── README.md            # İngilizce dokümantasyon
└── README.tr.md         # Türkçe dokümantasyon
```

---

## 🛠️ Kullanılan Teknolojiler

- [**Python**](https://www.python.org/): ana programlama dili
- [**CustomTkinter**](https://github.com/TomSchimansky/CustomTkinter): modern arayüz
- [**yt-dlp**](https://github.com/yt-dlp/yt-dlp): indirme motoru
- [**imageio-ffmpeg**](https://github.com/imageio/imageio-ffmpeg): MP3 dönüştürme ve video + ses birleştirme için hazır FFmpeg

---

## ❓ Sık Karşılaşılan Sorunlar

| Sorun | Çözüm |
|---|---|
| İndirme birden çalışmayı bıraktı | Platformlar sık değişir. Motoru güncelleyin: `pip install -U yt-dlp` |
| `ModuleNotFoundError` hatası | Kütüphaneler eksik. `python requirements.py` komutunu tekrar çalıştırın |
| Instagram giriş istiyor | Bazı Instagram içerikleri (özellikle gizli hesaplar) giriş gerektirir. Bu platformun kısıtıdır |
| MP3 dönüştürme hatası | `pip install -U imageio-ffmpeg` çalıştırın ya da FFmpeg'i bilgisayara ayrıca kurun |
| Linux: `No module named tkinter` | `sudo apt install python3-tk` komutunu çalıştırın |
| `python` tanınmıyor | `python3` deneyin ya da Python'u **"Add to PATH"** işaretli olarak yeniden kurun |

---

## ⚠️ Yasal Uyarı

Bu araç; size ait olan veya indirme izniniz bulunan içerikler için, **kişisel kullanım** amacıyla hazırlanmıştır. Her platformun kullanım koşullarına ve geçerli telif hakkı yasalarına uyun. Geliştiriciler, aracın kötüye kullanımından sorumlu değildir.

---

## 🤝 Katkıda Bulunma

Fikirleriniz ve pull request'leriniz çok değerli! Bir hata mı buldunuz? **Issue** açın.

Projeyi beğendiyseniz bir ⭐ bırakmayı unutmayın, çok yardımcı olur!

---

<div align="center">

❤️ ile ve biraz yapay zeka desteğiyle yapıldı

</div>
