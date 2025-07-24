import exifread
import os

def convert_to_degrees(value):
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)
    return d + (m / 60.0) + (s / 3600.0)

def extract_gps(tags):
    try:
        lat_ref = tags["GPS GPSLatitudeRef"].values
        lat = convert_to_degrees(tags["GPS GPSLatitude"])
        if lat_ref != "N":
            lat = -lat

        lon_ref = tags["GPS GPSLongitudeRef"].values
        lon = convert_to_degrees(tags["GPS GPSLongitude"])
        if lon_ref != "E":
            lon = -lon

        return lat, lon
    except:
        return None, None

def main():
    os.system("clear")
    print("🔍 ALIM FACE TRACKER - Lacak Lokasi dari Foto\n")

    path = input("📁 Masukkan path foto (misal: /sdcard/Download/foto.jpg): ")

    if not os.path.exists(path):
        print("❌ File tidak ditemukan.")
        return

    with open(path, 'rb') as f:
        tags = exifread.process_file(f)

    if not tags:
        print("⚠️ Tidak ada metadata ditemukan.")
        return

    print("\n📄 Metadata:")
    for tag in ["Image Make", "Image Model", "EXIF DateTimeOriginal"]:
        if tag in tags:
            print(f"{tag} : {tags[tag]}")

    lat, lon = extract_gps(tags)
    if lat and lon:
        print(f"\n📍 Koordinat: {lat}, {lon}")
        print(f"🌐 Maps: https://maps.google.com/?q={lat},{lon}")
    else:
        print("\n📍 Koordinat tidak tersedia di metadata.")

    with open("hasil-face-tracker.txt", "a") as file:
        file.write(f"\nFoto: {path}\nGPS: {lat}, {lon}\n------\n")

    print("\n✅ Selesai. Hasil disimpan di hasil-face-tracker.txt")

if __name__ == "__main__":
    main()
