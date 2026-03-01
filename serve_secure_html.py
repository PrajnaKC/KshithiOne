import os
from flask import Flask, render_template
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__, template_folder="Frontend/k10741/farmer_VA page")

@app.route("/farmer_dashboard")
def farmer_dashboard():
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    return render_template("farmer_dashboard.html", GOOGLE_MAPS_API_KEY=api_key)

# Add more routes as needed for other HTML files
# Example for va_dashboard.html:
@app.route("/va_dashboard")
def va_dashboard():
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    return render_template("../va page/va_dashboard.html", GOOGLE_MAPS_API_KEY=api_key)

# Example for marketplace
@app.route("/marketplace")
def marketplace():
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    return render_template("../marketplace/market-index.html", GOOGLE_MAPS_API_KEY=api_key)

if __name__ == "__main__":
    app.run(debug=True, port=5050)
