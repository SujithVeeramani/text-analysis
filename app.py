from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def analyze_text():
    if request.method == 'POST':
        text = request.form['text']

        character_count = len(text)
        digit_count = sum(c.isdigit() for c in text)
        uppercase_count = sum(c.isupper() for c in text)
        lowercase_count = sum(c.islower() for c in text)

        return render_template('result.html', character_count=character_count,
                           digit_count=digit_count, uppercase_count=uppercase_count,
                           lowercase_count=lowercase_count, text=text)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
