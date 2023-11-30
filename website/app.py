from flask import Flask
from flask import request
from flask.templating import render_template
from flask import jsonify
import eng2tok
import json

app = Flask(__name__)

# загружаем словарь из файла dictionary.json
with open("dictionary.json", "r", encoding="utf-8") as file:
    dictionary_data = json.load(file)["data"]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/phrasebook')
def phrasebook():
    return render_template('phrasebook.html')


@app.route('/translate', methods=['post', 'get'])
def translate():
    input_text = ""
    translation = ""
    target_language = "tokipona"  # по умолчанию переводим с английского на токипона

    if request.method == "POST":
        input_text = request.form.get("inputText")
        target_language = request.form.get("languageSelect")
        translation = eng2tok.translate(text=input_text, target_language=target_language)
        # print(input_text)

    return render_template('translate.html', input=input_text, translation=translation, target_language=target_language)


@app.route('/dictionary', methods=['post', 'get'])
def dictionary():
    results = []
    
    if request.method == "POST":
        english_word = request.form.get("englishWord").lower()
        results = [item["translation"] for item in dictionary_data if english_word in item["translation"]["en"].lower()]

    return render_template('dictionary.html', results=results)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
