# 🌐 Django Unit Converter

A simple and aesthetic **Unit Converter Web App** built with **Python, Django, HTML, and CSS**.  
It supports conversions for **Length, Weight, and Temperature** using styled pages.

---

## ✨ Features
- ✅ Welcome page with navigation
- ✅ Convert **Length** (mm, cm, m, km, in, ft, yd, mi)
- ✅ Convert **Weight** (mg, g, kg, ton, oz, lb, st)
- ✅ Convert **Temperature** (Celsius, Fahrenheit, Kelvin)
- ✅ Clean and modern UI (dark theme, gradient headings)
- ✅ Results rounded to 2 decimals
- ✅ Built with **Django forms** and custom logic

---

## 🛠 Tech Stack
- **Backend:** Python 3, Django
- **Frontend:** HTML, CSS (Google Fonts, gradients)
- **Templates:** Django template engine

---

## 📂 Project Structure


unit_converter/
│
├── converter/ # Django app
│ ├── forms.py # Django forms for conversions
│ ├── views.py # Views with conversion logic
│ ├── urls.py # App-specific URLs
│ └── templates/
│ ├── welcome.html # Home page
│ ├── length.html # Length converter page
│ ├── weight.html # Weight converter page
│ └── temperature.html# Temperature converter page
│
├── unit_converter/ # Project settings
│ ├── settings.py
│ ├── urls.py # Root URL routing
│ └── wsgi.py
│
├── manage.py # Django management script
└── README.md # This file


---

## ⚡ Installation & Setup

### 1. Clone repository
```bash
git clone https://github.com/yourusername/unit-converter.git
cd unit-converter

2. Create virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. Install dependencies
pip install django

4. Run migrations
python manage.py migrate

5. Start development server
python manage.py runserver

6. Open in browser

Navigate to:
👉 http://127.0.0.1:8000/

🔢 Examples

Length: 1 km → m = 1000

Weight: 2 lb → g = 907.18

Temperature: 32 F → C = 0.00

🎨 UI Preview

Dark theme background

Gradient headings

Centered cards for forms

Responsive design

📌 Notes

Results are rounded to 2 decimal places.

Conversion logic:

Length & Weight → based on base unit factors

Temperature → uses formula conversion (Celsius as pivot)

https://roadmap.sh/projects/unit-converter
