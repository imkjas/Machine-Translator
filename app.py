from flask import Flask, render_template, request
from translate import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    target_lang = request.form['target_lang']
    translator = Translator(to_lang=target_lang, from_lang='en')
    translated = translator.translate(text)
    return render_template('index.html', text=text, translated=translated)

if __name__ == '__main__':
    app.run(debug=True)
