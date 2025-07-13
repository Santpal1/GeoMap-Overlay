import os
import random
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont
from geopy.geocoders import Nominatim
from staticmap import StaticMap, CircleMarker

# ─── CONFIG ──────────────────────────────────────────────────────────────
INPUT_FOLDER  = "input_images"
OUTPUT_FOLDER = "output_images"
LATITUDE      = 25.5807287
LONGITUDE     = 85.2496650
MAP_ZOOM      = 18
# ──────────────────────────────────────────────────────────────────────────

def reverse_geocode(lat, lon):
    geo = Nominatim(user_agent="geo_overlay_osm")
    loc = geo.reverse((lat, lon), timeout=10)
    return loc.address if loc else "Unknown Location"

def make_osm_thumbnail(lat, lon, size_px, zoom):
    m = StaticMap(size_px, size_px,
                  url_template='https://a.tile.openstreetmap.org/{z}/{x}/{y}.png')
    m.add_marker(CircleMarker((lon, lat), 'red', 12))
    return m.render(zoom=zoom)

def get_random_morning_time():
    hour = random.randint(8, 10)      # 08:00 to 10:59
    minute = random.randint(0, 59)
    return timedelta(hours=hour, minutes=minute)

def get_timestamp_for_filename(filename):
    filename = filename.lower()
    base_time = None

    if "ngo1" in filename or "ngo2" in filename:
        base_time = datetime(2025, 6, 30)
    elif "ngo3" in filename:
        base_time = datetime(2025, 7, 1)
    elif "ngo4" in filename:
        base_time = datetime(2025, 7, 2)
    elif "ngo5" in filename:
        base_time = datetime(2025, 7, 3)
    elif "ngo6" in filename:
        base_time = datetime(2025, 7, 4)
    elif "ngo7" in filename:
        base_time = datetime(2025, 7, 5)
    elif "ngo8" in filename:
        base_time = datetime(2025, 7, 7)
    else:
        base_time = datetime(2025, 6, 30) + timedelta(days=random.randint(0, 7))

    random_time = get_random_morning_time()
    full_dt = base_time + random_time
    return full_dt.strftime('%d/%m/%y %I:%M %p GMT +05:30')


def apply_overlay(image_path, output_path, lat, lon):
    img = Image.open(image_path).convert("RGB")
    W, H = img.size

    map_w = max(100, min(300, W // 4))
    thumb = make_osm_thumbnail(lat, lon, map_w, MAP_ZOOM)

    try:
        f_bold = ImageFont.truetype("arialbd.ttf", 28)
        f_reg  = ImageFont.truetype("arial.ttf", 24)
    except:
        f_bold = f_reg = ImageFont.load_default()

    address = reverse_geocode(lat, lon)
    timestamp = get_timestamp_for_filename(os.path.basename(image_path))
    lines = [address, f"Lat {lat:.6f}°", f"Long {lon:.6f}°", timestamp]

    line_h = 36
    pad = 16
    text_block_h = line_h * len(lines) + 2 * pad
    overlay_h = max(text_block_h, map_w + pad)

    banner = Image.new("RGBA", (W, overlay_h), (0, 0, 0, 200))
    d = ImageDraw.Draw(banner)

    x_text = map_w + pad
    y_text = pad
    for i, line in enumerate(lines):
        font = f_bold if i == 0 else f_reg
        d.text((x_text, y_text), line, font=font, fill=(255, 255, 255))
        y_text += line_h

    img.paste(banner, (0, H - overlay_h), banner)
    img.paste(thumb, (0, H - overlay_h + pad // 2))

    img.save(output_path)
    print("✅ Saved:", output_path)

def batch_process_folder(input_folder, output_folder, lat, lon):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    valid_exts = (".jpg", ".jpeg", ".png")
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_exts):
            in_path = os.path.join(input_folder, filename)
            out_path = os.path.join(output_folder, f"overlay_{filename}")
            try:
                apply_overlay(in_path, out_path, lat, lon)
            except Exception as e:
                print("❌ Failed for:", filename, "→", e)

if __name__ == "__main__":
    batch_process_folder(INPUT_FOLDER, OUTPUT_FOLDER, LATITUDE, LONGITUDE)
