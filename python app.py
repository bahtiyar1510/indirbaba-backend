from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS desteği

# Ana sayfa
@app.route('/')
def home():
    return jsonify({"message": "İndirBaba API çalışıyor!"})

# HEALTH CHECK ENDPOINT - RAILWAY İÇİN ÇOK ÖNEMLİ!
@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

# İndirme endpoint'i
@app.route('/download')
def download():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL gerekli"}), 400
    
    # BU KISMA VİDEO İNDİRME KODUNU YAZ
    # Örnek: video_url = fetch_video(url)
    
    return jsonify({
        "success": True,
        "video_url": "https://example.com/video.mp4"  # GERÇEK LİNKİ DÖNDÜR
    })
