from flask import Flask, request, send_file, render_template
from download_youtube_mp3 import baixar_e_converter
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    nome_arquivo_mp3 = baixar_e_converter(url)
    if nome_arquivo_mp3 is None:
        return "Não foi possível baixar o vídeo. Por favor, verifique a URL e tente novamente.", 400
    return send_file(nome_arquivo_mp3, as_attachment=True, download_name=nome_arquivo_mp3, mimetype="audio/mp3")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)  # Altere o número da porta
