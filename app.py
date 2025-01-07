from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"detail": "Текст для анализа отсутствует"}), 400

    text = data['text']
    anxiety_score = len(text) / 100

    return jsonify({"anxiety_score": round(anxiety_score, 2)})

if __name__ == '__main__':
    app.run(port=8000, debug=True)
