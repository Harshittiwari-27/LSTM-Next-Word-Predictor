from flask import Flask, render_template, request
from lstm_model import predict_seq
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    text = request.form['d1']
    result = predict_seq(text)
    return render_template('resultt.html', result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)