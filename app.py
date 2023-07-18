from flask import Flask, render_template, request

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

# Result right box (result_upload.html)
@app.route('/result_upload', methods=['GET', 'POST'])
def result_upload():
    if request.method == 'POST':
        image_url = request.form['image_url']
        return render_template('result_upload.html')

if __name__ == '__main__':
    app.run(debug=True)
