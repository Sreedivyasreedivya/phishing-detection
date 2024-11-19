# app.py
from flask import Flask, render_template, request, jsonify
from utils.url_utils import is_phishing_url
from utils.ssl_utils import check_ssl_certificate
from utils.form_utils import check_for_suspicious_forms

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to process phishing detection
@app.route('/check', methods=['POST'])
def check_phishing():
    url = request.form['url']

    # Call utility functions to check for phishing, SSL, and suspicious forms
    phishing_url = is_phishing_url(url)
    ssl_valid = check_ssl_certificate(url)
    suspicious_forms = check_for_suspicious_forms(url)

    result = {
        'url': url,
        'is_phishing': phishing_url,
        'ssl_valid': ssl_valid,
        'has_suspicious_forms': suspicious_forms
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
