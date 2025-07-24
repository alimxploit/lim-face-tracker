# lim-face-tracker
Tools OSINT lacak lokasi dari metadata foto (EXIF).
# 🛰 ALIM FACE TRACKER

Tools OSINT edukatif buatan AlimXploit untuk melacak lokasi dari metadata (EXIF) pada foto.

## 🔍 Fitur:
- Ekstrak koordinat GPS dari foto
- Deteksi waktu dan kamera yang digunakan
- Buat link Google Maps dari lokasi
- Simpan hasil pelacakan ke file `.txt`
- Bisa dijalankan di Termux & Python PC

## 📦 Instalasi (di Termux):
GIT CLONE:
https://github.com/alimxploit/alim-face-tracker

pkg update && pkg upgrade -y
pkg install git python -y
git clone https://github.com/alimxploit/alim-face-tracker
cd alim-face-tracker
python alim-face-tracker.py
