Here’s a clean and concise `README.md` tailored to your project:

---

### 📄 `README.md`

````markdown
# 📍 Image Location Overlay Tool

This Python script processes a batch of images, overlays them with:
- a **map thumbnail** of a specified location,
- a **reverse geocoded address**,
- and a **timestamp** (fixed or randomized based on filename).

---

## ✨ Features

- Adds a **semi-transparent banner** at the bottom of each image.
- Displays:
  - OpenStreetMap thumbnail with location marker
  - Address from coordinates (via OpenStreetMap Nominatim)
  - Latitude & Longitude
  - Timestamp (based on filename or randomized)
- Automatically processes all images in a given folder.

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
````

### `requirements.txt`

```txt
Pillow==10.3.0
geopy==2.4.1
staticmap==0.5.4
```

---

## 🗂 Folder Structure

```
project/
├── input_images/         # Place your input images here
├── output_images/        # Processed images will be saved here
├── main.py               # Main script
├── requirements.txt
└── README.md
```

---

## 🔧 Usage

1. Place your `.jpg`, `.png`, or `.jpeg` images inside `input_images/`.
2. Customize coordinates and timestamp mapping if needed.
3. Run the script:

```bash
python main.py
```

Output images will be saved with the overlay in the `output_images/` folder.

---

## 🗓 Timestamp Mapping

Timestamps are assigned based on the filename:

| Filename Contains | Assigned Date                           |
| ----------------- | --------------------------------------- |
| `ngo1`, `ngo2`    | 30 June 2025                            |
| `ngo3`            | 1 July 2025                             |
| `ngo4`            | 2 July 2025                             |
| `ngo5`            | 3 July 2025                             |
| `ngo6`            | 4 July 2025                             |
| `ngo7`            | 5 July 2025                             |
| `ngo8`            | 7 July 2025                             |
| Other filenames   | Random date from 30 June to 7 July 2025 |

All timestamps use a **random morning time between 8:00 AM and 10:59 AM**.

---

## 🗺️ Default Coordinates

The script uses the following coordinates (you can change them in `main.py`):

```
Latitude:  12.956891
Longitude: 80.160323
Zoom:      18
```

---

## 🧩 Customization

* To change banner position (e.g. top instead of bottom), timestamp formats, or location source (e.g., EXIF), feel free to ask or tweak the code.
* Works well for field visit documentation, NGO site tagging, or geo-photologging.

---

## 📸 Sample Output

*Example images showing map + address + timestamp overlay.*

*(Add sample screenshots or outputs here)*

---

## 🧑‍💻 Author

Built by \[Your Name] – feel free to fork and customize!

```

---

Let me know if you want this personalized with your GitHub name, institution (e.g., SRM), or to add sample image previews in the markdown.
```
