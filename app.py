from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"detail": "Текст для анализа отсутствует"}), 400

    # Логика анализа текста (замените на вашу нейросеть)
    text = data['text']
    anxiety_score = len(text) / 100  # Простая логика для примера

    return jsonify({"anxiety_score": round(anxiety_score, 2)})

if __name__ == '__main__':
    app.run(port=8000, debug=True)
