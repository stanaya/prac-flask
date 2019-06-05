from flask import Flask, jsonify, request
import json
from d2c.tokenizer import tokenizer as tk
app = Flask(__name__)

@app.route('/validation',methods=["POST"])
def validation():
    data = json.loads(request.data)
    tokenizer = tk.Tokenizer()
    out = tokenizer.run(data["text"])
    return out

## おまじない
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
