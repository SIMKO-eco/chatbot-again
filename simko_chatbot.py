<<<<<<< HEAD
<<<<<<< HEAD
from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# OpenRouter API key (replace with your real key)
OPENROUTER_API_KEY = "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"
MODEL = "openai/gpt-3.5-turbo"

# Simko personality prompt
SYSTEM_PROMPT = (
    "You are the official AI assistant of Simko. "
    "Simko does not have an investor yet. "
    "Your role is to explain Simko's vision, approach, and innovations in a clear, friendly, and technically accurate way. "
    "Simko is redefining electric vehicles by reducing weight, cost, and environmental impact through custom motors, compact drivetrains, and lightweight design. "
    "Help visitors understand how Simko achieves 30–50% EV weight savings, and supports a carbon-negative future. "
    "Always answer all questions the user asks, even if they include multiple questions in a single message."
)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        return jsonify({"response": reply})
    else:
        print(response.status_code)
        print(response.text)
        return jsonify({"response": f"Error: {response.status_code}, {response.text}"}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# OpenRouter API key (replace with your real key)
OPENROUTER_API_KEY = "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"
MODEL = "openai/gpt-3.5-turbo"

# Simko personality prompt
SYSTEM_PROMPT = (
    "You are the official AI assistant of Simko. "
    "Simko does not have an investor yet. "
    "Your role is to explain Simko's vision, approach, and innovations in a clear, friendly, and technically accurate way. "
    "Simko is redefining electric vehicles by reducing weight, cost, and environmental impact through custom motors, compact drivetrains, and lightweight design. "
    "Help visitors understand how Simko achieves 30–50% EV weight savings, and supports a carbon-negative future. "
    "Always answer all questions the user asks, even if they include multiple questions in a single message."
)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        return jsonify({"response": reply})
    else:
        print(response.status_code)
        print(response.text)
        return jsonify({"response": f"Error: {response.status_code}, {response.text}"}), response.status_code

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
>>>>>>> b506e534c287cc817aad1b625d34f411caa23f48
=======
from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
from datetime import datetime
import openpyxl
import os

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = "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"
MODEL = "openai/gpt-3.5-turbo"

SYSTEM_PROMPT = (
    "You are the official AI assistant of Simko. "
    "Simko does not have an investor yet. "
    "Your role is to explain Simko's vision, approach, and innovations in a clear, friendly, and technically accurate way. "
    "Simko is redefining electric vehicles by reducing weight, cost, and environmental impact through custom motors, compact drivetrains, and lightweight design. "
    "Help visitors understand how Simko achieves 30–50% EV weight savings, and supports a carbon-negative future. "
    "Always answer all questions the user asks, even if they include multiple questions in a single message."
)

LOG_FILE = "chat_log.xlsx"

if not os.path.exists(LOG_FILE):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Chat Log"
    ws.append(["Timestamp", "User Question", "Bot Response"])
    wb.save(LOG_FILE)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]

        wb = openpyxl.load_workbook(LOG_FILE)
        ws = wb["Chat Log"]
        ws.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_input, reply])
        wb.save(LOG_FILE)

        return jsonify({"response": reply})
    else:
        return jsonify({"response": f"Error: {response.status_code}, {response.text}"}), response.status_code

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
>>>>>>> df6ca99be8c14135225de6e0e5fe6b42f88f08ec
