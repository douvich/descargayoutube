import yt_dlp

def download_video(url, quality):
    ydl_opts = {
        'format': quality,  # Puedes elegir la calidad aquí
        'outtmpl': 'downloads/%(title)s.%(ext)s'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    video_url = data.get('videoUrl')
    quality = data.get('quality')
    
    ydl_opts = {
        'format': quality,
        'outtmpl': 'downloads/%(title)s.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            download_link = f"/downloads/{info_dict['title']}.{info_dict['ext']}"
            return jsonify({"downloadLink": download_link})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
