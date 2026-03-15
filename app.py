from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app) # Bu satır o meşhur CORS hatasını öldürür!

@app.route('/indir', methods=['POST'])
def indir():
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({"error": "Link nerede baba?"}), 400

    try:
        # yt-dlp ile videonun gerçek linkini ayıklıyoruz
        ydl_opts = {'format': 'best', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.get('url')
            title = info.get('title')

        return jsonify({"success": True, "download_url": video_url, "title": title})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
