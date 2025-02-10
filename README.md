# URL Shortener Project

## 📌 Overview

This is a simple URL shortener project that converts long URLs into short, shareable links using Python.

## 🚀 Features

- Shorten long URLs quickly.
- Copy the shortened URL to the clipboard.
- Uses `pyshorteners`, `Pillow`, and `clipboard` libraries.

## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-repo/url-shortener.git
cd url-shortener
```

### 2️⃣ Create and Activate a Virtual Environment

#### Windows

```sh
python -m venv .venv
.venv\Scripts\activate
```

#### macOS/Linux

```sh
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```sh
python -m pip install pillow pyshorteners clipboard
```

## ▶️ Running the Script

```sh
python url-shortner.py
```

## 🧪 Testing with a Sample URL

To test the script, use the following LinkedIn post URL:

```sh
https://www.linkedin.com/posts/shahid-shaikh-68993a214_webdevelopment-portfoliolaunch-frontend-activity-7294198631358750722-EV1d?utm_source=share&utm_medium=member_desktop&rcm=ACoAADY-ZkkB-9U-HGecVFrouk4Zabl28LSe8xs
```

## 🔍 Example Output

Original URL: <https://www.linkedin.com/posts/>...
Shortened URL: <https://bit.ly/xyz123>
Shortened URL copied to clipboard!

## 🛑 Troubleshooting

- If you get `ModuleNotFoundError: No module named 'PIL'`, ensure that `pillow` is installed in your virtual environment.
- If `pip` is not recognized, try `python -m pip install --upgrade pip`.
- Use `python -m pip list` to check installed packages.

## 📜 License

This project is open-source and available for modification and improvement.

---
💡 *Developed by Shahid Shaikh*
