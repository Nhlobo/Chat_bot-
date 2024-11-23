from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Predefined responses
responses = {
    "process": "Our process includes an initial consultation, proposal, agreement, development, testing, delivery, and ongoing support.",
    "pricing": "Visit our pricing page for more details on our packages: Starter, Standard, Premium, and E-commerce.",
    "privacy policy": "For privacy-related queries, visit our Privacy Policy page.",
    "terms of service": "For information on our Terms of Service, visit our Terms page."
}

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower()

    # Determine response
    if "process" in user_input:
        response = responses["process"]
    elif "pricing" in user_input:
        response = responses["pricing"]
    elif "privacy policy" in user_input:
        response = responses["privacy policy"]
    elif "terms of service" in user_input:
        response = responses["terms of service"]
    else:
        response = "I'm sorry, I can only assist with questions about our process, pricing, privacy policy, and terms of service."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
