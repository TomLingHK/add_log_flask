import os
from flask import Flask, jsonify, request

from add_log import add_log

app = Flask(__name__)

SERVICE_NAME = "add_log"
# BASE_PATH = "./test_log/"
BASE_PATH = os.getenv("BASE_PATH") or "/nas_data/"

if not (os.path.isdir(BASE_PATH) and os.access(BASE_PATH, os.R_OK)):
    BASE_PATH = "/app/nas_data/"

print('BASE_PATH: ', BASE_PATH)


APP_CONST = {
    'BASE_PATH': BASE_PATH,
}

@app.route("/run", methods=['POST'])
def main():
    """
        dir_name(string): "abc_project/debug/"
        file_name(string): "log_20260228.txt"
        content(string): "[20260228][INFO] Validate job complete without error."
    """
    print(f"BACKGROUND TASK STARTED for endpoint: /")
    data = request.get_json(silent=True) or {}
    dir_name = data.get('dir_name', '')
    file_name = data.get('file_name', '')
    content = data.get('content', '')
    
    if (len(file_name) == 0):
        print(f"Empty file_name provided, returning error response.")
        return jsonify({"error": "No file_name provided. Expect file name with extension."}), 400
    if (len(content) == 0):
        print(f"Empty content provided, returning error response.")
        return jsonify({"error": "No content provided."}), 400
    
    return jsonify(add_log(APP_CONST, dir_name, file_name, content)), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)