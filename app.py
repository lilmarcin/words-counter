from flask import Flask, render_template, request
from word_counter_text import count_words_and_characters
import easyocr
from PIL import Image
import os
import tempfile
import base64
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Left box (write.html)
@app.route('/write')
def write():
    return render_template('write.html')

# Result left box (result_write.html)
@app.route('/result_write', methods=['POST'])
def result_write():
    if request.method == 'POST':
        text = request.form['text']
        word_counter = len(text.split())
        character_counter = len(text)
        return render_template('result_write.html', text=text, word_counter=word_counter, character_counter=character_counter)

# Right box (upload.html)
@app.route('/upload')
def upload():
    return render_template('upload.html')

# Result right box (result_upload_url.html)
@app.route('/result_upload_url', methods=['POST'])
def result_upload_url():
    if request.method == 'POST':
        image_url = request.form['image_url']
        headers = {
            'User-Agent': 'Mozilla/5.0 Chrome/58.0.3029.110 Safari/537.3', 
            'Accept': 'image/jpeg, image/png'
        }

        try:
            response = requests.get(image_url)
            response.raise_for_status()
            image_data = response.content
        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except requests.exceptions.RequestException as req_err:
            return f"Request error occurred: {req_err}"

        reader = easyocr.Reader(['en'])
        result = reader.readtext(image_data, detail=0)

        word_counter, character_counter = count_words_and_characters(result)
        encoded_img = base64.b64encode(image_data).decode("utf-8")

        return render_template('result_upload_url.html', image_url=image_url, word_counter=word_counter, character_counter=character_counter, encoded_img=encoded_img)

# Result left box (result_upload_file.html)
@app.route('/result_upload_file', methods=['POST'])
def result_upload_file():
    if request.method == 'POST':
        if 'image_file' not in request.files:
            return "No file part"
        image_file = request.files['image_file']
        if image_file.filename == '':
            return "No selected file"

        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            image_file.save(temp_file.name)

            with Image.open(temp_file.name) as img:
                reader = easyocr.Reader(['en'])
                result = reader.readtext(temp_file.name, detail=0)

        word_counter, character_counter = count_words_and_characters(result)

        with open(temp_file.name, "rb") as img_file:
            encoded_img = base64.b64encode(img_file.read()).decode("utf-8")
        os.remove(temp_file.name)

        return render_template('result_upload_file.html', word_counter=word_counter, character_counter=character_counter, encoded_img=encoded_img)

if __name__ == '__main__':
    app.run(debug=True)
