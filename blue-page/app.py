from flask import Flask, send_file, jsonify
import redis
import os

app = Flask(__name__)
# WSL의 IP 주소를 환경변수로 받음
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_client = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/count", methods=["POST"])
def increment_count():
    redis_client.incr("blue_visits")
    return "OK"

@app.route("/count")
def get_count():
    visits = int(redis_client.get("blue_visits") or 0)
    return jsonify({"visits": visits})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
