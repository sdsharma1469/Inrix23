from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add")
def add():
    num2 = request.args.get("num2", type=int)
    num1 = request.args.get("num1", type=int)

    if num1 is not None and num2 is not None:
        result = num1 + num2
        return jsonify(sum=result)
    else:
        return jsonify(error="Invalid input. Please provide valid 'num1' and 'num2' parameters."), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)