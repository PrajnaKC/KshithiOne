# KshithiOne

KshithiOne is a geo-enabled project that integrates the **Google Maps API** and the **Google Earth Engine (GEE) API** to visualize, analyze, and present geospatial information through a web interface powered by Python + HTML/CSS/JavaScript.

## Key Capabilities
- Interactive maps and location-based visualization (Google Maps API)
- Geospatial/remote-sensing analysis and data layers (Google Earth Engine)
- Web UI built with HTML, CSS, and JavaScript
- Python backend / scripts for data processing and API integration

## Tech Stack
- **Python** (core logic / backend / automation)
- **HTML / CSS / JavaScript** (frontend)
- **Google Maps Platform** (Maps JavaScript API and related services)
- **Google Earth Engine** (geospatial datasets + analysis)

## Prerequisites
- Python 3.10+ recommended
- A Google Cloud project with **Google Maps API** enabled
- A Google Earth Engine account enabled for the Google account you’ll use
- API credentials:
  - Google Maps API Key
  - Earth Engine authentication (OAuth / service account depending on approach)

## Setup

### 1) Clone and create a virtual environment
```bash
git clone https://github.com/PrajnaKC/KshithiOne.git
cd KshithiOne

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 2) Install Python dependencies
If the repo includes `requirements.txt`:
```bash
pip install -r requirements.txt
```

If not, add one later once dependencies are finalized.

### 3) Configure Environment Variables
Create a `.env` file (or configure your environment) with values like:

```env
GOOGLE_MAPS_API_KEY=your_maps_api_key_here
# Optional / if used by your code:
GCP_PROJECT_ID=your_gcp_project_id
```

### 4) Authenticate Google Earth Engine
Depending on how your code is written, one common local setup is:
```bash
earthengine authenticate
```

Then initialize in Python (example):
```python
import ee
ee.Initialize()
```

## Running
Because projects vary in structure, use the command that matches your entrypoint:

- If you have a Python entry file:
```bash
python main.py
```

- If this is a Flask app:
```bash
flask run
```

- If this is a FastAPI app:
```bash
uvicorn app:app --reload
```

## Contributing
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-change`
3. Commit: `git commit -m "Add: my change"`
4. Push: `git push origin feature/my-change`
5. Open a Pull Request
