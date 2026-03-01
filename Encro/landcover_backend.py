import ee
import numpy as np
from flask import Flask, request, jsonify

# ✅ ADD THIS
from flask_cors import CORS


# -------------------------------
# Service Account Authentication
# -------------------------------

SERVICE_ACCOUNT = "prajna-earth-engine-service-ac@academic-script-473911-k4.iam.gserviceaccount.com"

# Modified to handle both local development and deployment environment variables
import os
import json

KEY_FILE = "keys/Google earth engine service account key.json"
EE_SERVICE_ACCOUNT_JSON = os.getenv("EE_SERVICE_ACCOUNT_JSON")

if EE_SERVICE_ACCOUNT_JSON:
    # Check if it's already a dictionary or needs parsing
    if isinstance(EE_SERVICE_ACCOUNT_JSON, dict):
        service_account_info = EE_SERVICE_ACCOUNT_JSON
    else:
        try:
            service_account_info = json.loads(EE_SERVICE_ACCOUNT_JSON)
        except Exception:
             # Fallback if parsing fails (maybe it's a file path?)
             service_account_info = None

    if service_account_info:
        credentials = ee.ServiceAccountCredentials(SERVICE_ACCOUNT, key_data=service_account_info)
    else:
        # Fallback to local file if env var exists but failed to parse/was path
        credentials = ee.ServiceAccountCredentials(SERVICE_ACCOUNT, KEY_FILE)
else:
    # Local development
    credentials = ee.ServiceAccountCredentials(SERVICE_ACCOUNT, KEY_FILE)

ee.Initialize(credentials)


# -------------------------------
# Flask App
# -------------------------------

app = Flask(__name__)

# ✅ ENABLE CORS
CORS(app)


FOREST_CLASS = 1
AGRI_CLASS = 4


@app.route("/analyze", methods=["POST"])
def analyze():

    try:

        geojson = request.json

        polygon = ee.Geometry.Polygon(geojson["coordinates"])


        image = (

            ee.ImageCollection("GOOGLE/DYNAMICWORLD/V1")

            .filterBounds(polygon)

            .sort("system:time_start", False)

            .first()

            .select("label")

        )


        stats = image.reduceRegion(

            reducer=ee.Reducer.frequencyHistogram(),

            geometry=polygon,

            scale=10,

            maxPixels=1e9

        ).getInfo()


        histogram = stats.get("label", {})

        total = sum(histogram.values()) if histogram else 0


        if total == 0:

            return jsonify({

                "forest_percent": 0,

                "agriculture_percent": 0,

                "other_percent": 0

            })


        forest = histogram.get(str(FOREST_CLASS), 0)

        agriculture = histogram.get(str(AGRI_CLASS), 0)

        other = total - forest - agriculture


        result = {

            "forest_percent": round(forest / total * 100, 2),

            "agriculture_percent": round(agriculture / total * 100, 2),

            "other_percent": round(other / total * 100, 2)

        }


        return jsonify(result)


    except Exception as e:

        return jsonify({"error": str(e)}), 500



# -------------------------------
# Run Server
# -------------------------------

if __name__ == "__main__":

    app.run(debug=True)