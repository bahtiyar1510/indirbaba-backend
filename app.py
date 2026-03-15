from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "İndirBaba API Çalışıyor Hacı!"

@app.route('/indir', methods=['POST'])
def indir():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({"error": "Link nerde?"}), 400
    
    ydl_opts = {'format': 'best', 'quiet': True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return jsonify({"download_url": info.get('url')})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Railway'in istediği kritik ayar burası:
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
