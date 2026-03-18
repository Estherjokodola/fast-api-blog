# FastAPI Blog

A full-featured blog web application built with **FastAPI (Python)**, featuring blog posts, user profiles, dark mode, and a REST API.

---

## Project Structure

```
FastAPI_blog/
├── .venv/                        # Virtual environment
│   └── Lib/
│       └── ...                   # Installed packages
├── static/
│   ├── css/
│   │   └── main.css              # Custom styles (light + dark mode)
│   ├── icons/
│   │   └── ...                   # Favicon and app icons
│   ├── js/
│   │   └── ...                   # JavaScript files
│   ├── profile_pics/             # User profile images
│   └── site.webmanifest          # Web app manifest (PWA support)
├── templates/
│   ├── layout.html               # Base layout (navbar, footer, dark mode toggle)
│   └── home.html                 # Home page (blog post listing)
├── .python-version               # Python version pinning
├── windows.py                    # Windows-specific entry point
├── pyproject.toml                # Project metadata and dependencies
├── README.md                     # This file
├── source                        # Source configuration
└── uv.lock                       # Dependency lock file (uv package manager)
```

---

## Features

- **Blog Posts & Articles** — Browse and read posts with author, date, and content
- **User Profiles** — Profile pictures and author display on each post
- **Dark Mode** — Toggle between Light, Dark, and Auto (follows system preference), persisted in `localStorage`
- **REST API** — JSON endpoints for programmatic access to posts
- **Responsive Design** — Mobile-friendly layout with Bootstrap 5
- **Jinja2 Templating** — Server-side HTML rendering with template inheritance

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, FastAPI |
| Templating | Jinja2 |
| Frontend | HTML, CSS, Bootstrap 5 |
| Fonts | Montserrat, Nunito (Google Fonts) |
| Package Manager | uv |
| Server | Uvicorn (ASGI) |

---

## Getting Started

### Prerequisites

- Python 3.8+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/FastAPI_blog.git
   cd FastAPI_blog
   ```

2. **Create and activate the virtual environment**

   Using `uv` (recommended):
   ```bash
   uv venv
   source .venv/bin/activate      # macOS / Linux
   .venv\Scripts\activate         # Windows
   ```

   Using pip:
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS / Linux
   .venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**

   Using `uv`:
   ```bash
   uv sync
   ```

   Using pip:
   ```bash
   pip install fastapi uvicorn jinja2 python-multipart
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

   The app will be available at `http://127.0.0.1:8000`

---

## REST API

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Home page (HTML) |
| `GET` | `/posts` | Posts page (HTML) |
| `GET` | `/api/posts` | Get all posts (JSON) |

### Example Request

```bash
curl http://127.0.0.1:8000/api/posts
```

### Example Response

```json
[
  {
    "id": 1,
    "author": "Corey Schafer",
    "title": "This framework is really easy to use and super fast",
    "content": "FastAPI is awesome",
    "date_posted": "April 20, 2025"
  },
  {
    "id": 2,
    "author": "Jane Doe",
    "title": "FastAPI is the best framework for building APIs",
    "content": "I love FastAPI",
    "date_posted": "April 21, 2025"
  }
]
```

---

## Dark Mode

Dark mode uses Bootstrap 5's `data-bs-theme` attribute with three options in the navbar dropdown:

| Option | Behaviour |
|--------|-----------|
| 🌝 Light | Always light theme |
| 🌚 Dark | Always dark theme |
| 🌗 Auto | Follows system preference |

The selected preference is saved in `localStorage` and restored on every page load.

---

## Static Files

| Path | Contents |
|------|----------|
| `static/css/main.css` | Custom Bootstrap overrides, CSS variables for light and dark themes |
| `static/icons/` | `favicon.ico`, `icon.svg`, `icon.png` for browser and PWA support |
| `static/js/` | JavaScript files |
| `static/profile_pics/` | User profile images (default: `default.jpg`) |
| `static/site.webmanifest` | Progressive Web App manifest |

---

## Templates

| File | Description |
|------|-------------|
| `layout.html` | Base template — navbar with dark mode toggle, sidebar, and footer |
| `home.html` | Extends `layout.html` — renders blog posts using a Jinja2 `for` loop |

---

## Known Issues & Fixes

### Content hidden behind fixed navbar

The navbar uses `position: fixed`, removing it from the normal document flow. Fix by updating `main.css`:

```css
main {
  padding-top: calc(56px + 1.5rem);
}
```

---

## License

This project is licensed under the MIT License.

---

## Author

Built by **Esther** — feel free to open an issue or submit a pull request.
