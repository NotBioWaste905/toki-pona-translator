from flask import Flask
from flask import request
from flask.templating import render_template
from flask import jsonify
import translator
import json

app = Flask(__name__)

# загружаем словарь из файла dictionary.json
with open("website\dictionary.json", "r", encoding="utf-8") as file:
    dictionary_data = json.loads(file.read())


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
    print(request.form.get('_direction'))
    if request.method == "POST":
        input_text = request.form.get("inputWord")
        translation = translator.translate(text=input_text, target_language=target_language)
        

    return render_template('translate.html', orig_sentence=input_text, input=input_text, translation=translation, target_language=target_language)


@app.route('/dictionary', methods=['post', 'get'])
def dictionary():
    results = []
    toki_word = ''
    if request.method == "POST":
        toki_word = request.form.get("englishWord").lower()
        for i in dictionary_data:
            if i['word'] == toki_word.strip():
                results = i['meanings'][-1]
        # results = [item["translation"] for item in dictionary_data if english_word in item["translation"]["en"].lower()]

    return render_template('dictionary.html', orig_word=toki_word, results=results)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
