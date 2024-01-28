from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def handle_request():
    if request.method == "POST":
        # Run stress_cpu.py in a separate process
        subprocess.Popen(["python3", "stress_cpu.py"])
        return "Stressing CPU in a separate process"

    elif request.method == "GET":
        # Get the private IP address of the EC2 instance
        private_ip = socket.gethostbyname(socket.gethostname())
        return private_ip

if __name__ == "__main__":
    # Replace 5000 with your desired port number
    app.run(host="0.0.0.0", port=5000)
