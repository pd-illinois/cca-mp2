from flask import Flask, request, jsonify

app = Flask(__name__)
seed = 0

@app.route("/", methods=["GET", "POST"])
def handle_request():
    global seed

    if request.method == "POST":
        data = request.get_json()
        if "num" in data and isinstance(data["num"], int):
            seed = data["num"]
            return jsonify({"message": "Seed updated successfully"})

    elif request.method == "GET":
        return str(seed)

if __name__ == "__main__":
    # Replace 5000 with your desired port number
    app.run(host="0.0.0.0", port=5000)
