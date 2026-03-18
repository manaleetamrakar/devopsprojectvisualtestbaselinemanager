from flask import Flask, request, jsonify
from PIL import Image, ImageChops
import os

app = Flask(__name__)

BASELINE_DIR = "baselines"
NEW_DIR = "new"
DIFF_DIR = "diffs"

os.makedirs(BASELINE_DIR, exist_ok=True)
os.makedirs(NEW_DIR, exist_ok=True)
os.makedirs(DIFF_DIR, exist_ok=True)


@app.route("/")
def home():
    return "Visual Test Baseline Manager Running!"


@app.route("/compare", methods=["POST"])
def compare_images():
    baseline = request.files["baseline"]
    new = request.files["new"]

    baseline_path = os.path.join(BASELINE_DIR, baseline.filename)
    new_path = os.path.join(NEW_DIR, new.filename)

    baseline.save(baseline_path)
    new.save(new_path)

    img1 = Image.open(baseline_path)
    img2 = Image.open(new_path)

    diff = ImageChops.difference(img1, img2)

    if diff.getbbox():
        diff_path = os.path.join(DIFF_DIR, "diff_" + baseline.filename)
        diff.save(diff_path)
        return jsonify({"result": "Different", "diff": diff_path})
    else:
        return jsonify({"result": "Same"})


@app.route("/update-baseline", methods=["POST"])
def update_baseline():
    new = request.files["new"]

    baseline_path = os.path.join(BASELINE_DIR, new.filename)
    new.save(baseline_path)

    return jsonify({"message": "Baseline updated successfully"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)