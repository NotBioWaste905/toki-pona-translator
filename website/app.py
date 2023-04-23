from flask import Flask
from flask import request
from flask.templating import render_template
import eng2tok
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():

    return render_template('home.html')


@app.route('/translate', methods=['post', 'get'])
def translate():
    input_text = ""
    translation = ""
    if request.method == "POST":
        input_text = request.form.get("inputText")
        translation = eng2tok.translate(text=input_text)
        # print(input_text)

    return render_template('translate.html', input=input_text, translation=translation)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)