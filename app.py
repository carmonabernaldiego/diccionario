import re
from flask import Flask, render_template, request

app = Flask(__name__)

antonyms = {
    "grande": "pequeño",
    "alto": "bajo",
    "fácil": "difícil",
    "rápido": "lento",
    "fuerte": "débil",
    "nuevo": "viejo",
    "caliente": "frío",
    "luminoso": "oscuro",
    "feliz": "triste",
    "rico": "pobre",
    "bueno": "malo",
    "joven": "viejo",
    "duro": "blando",
    "lleno": "vacío",
    "corto": "largo",
    "claro": "oscuro",
    "delgado": "grueso",
    "amable": "grosero",
    "seguro": "peligroso",
    "simple": "complejo"
}

symbols = {';', '"', '+', '=', ',', '(', ')', '{', '}'}
identifiers = set()


def analyze_code(code):
    lines = code.split('\n')
    tokens = []

    for i, line in enumerate(lines, start=1):
        words = re.findall(r'\b\w+\b|[\(\){};"+=,]', line)
        for word in words:
            token = {
                'token': word,
                'line': i,
                'antonym': antonyms.get(word, ''),
                'symbol': 'x' if word in symbols else '',
                'number': 'x' if word.isdigit() else '',
                'identifier': 'x' if word in identifiers else '',
            }
            tokens.append(token)

    return tokens


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code']
        tokens = analyze_code(code)
        return render_template('index.html', tokens=tokens, code=code)
    return render_template('index.html', tokens=[], code='')


if __name__ == '__main__':
    app.run(debug=True)
