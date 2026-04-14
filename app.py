from flask import Flask, jsonify
import requests
from datetime import datetime
import yaml
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path('.')

config = {}
with open(BASE_DIR / "config.local.yaml", "r") as f:
    config.update(yaml.safe_load(f) or {})

immmich_cfg = config.get("immmich", {})
api_key = immmich_cfg.get("api_key")

@app.route('/immich/random')
def immich_random():
    r = requests.post(
        'http://192.168.1.99:2283/api/search/random',
        json={"type": "IMAGE", "count": 1, "albumIds": ["e8fdcfb1-a176-488d-8e49-780bf86f94b8"]},
        headers={"x-api-key": api_key}
    )
    data = r.json()
    if data:
        asset = data[0]
        date = asset.get("fileCreatedAt", "")[:10]  # solo YYYY-MM-DD
        return jsonify({"id": asset["id"], "date": date})
    return jsonify({"id": asset["id"], "photo_date": date})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085, debug=False)