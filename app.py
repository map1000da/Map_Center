from flask import Flask, request, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# 選択された場所を所得するためのエンドポイント
@app.route("/locations/", methods=["POST"])
def locations():
    data = request.json
    locations = data["locations"]
    lats = [location[0] for location in locations]
    lngs = [location[1] for location in locations]
    center_lat = sum(lats) / len(lats)
    center_lng = sum(lngs) / len(lngs)
    center = [center_lat, center_lng]

    return jsonify(center=center)