from flask import Flask, jsonify, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Make your password at least 8 characters long.")

    # Upper and lower case
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Use both Upper Case and Lower Case alphabets.")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include numbers in your password.")

    # Special Characters
    if re.search(r"[!@#$%^&*()_?><:''/|,.{}]", password):
        score += 1
    else:
        suggestions.append("Include special characters (@, #, %, ^, &, etc).")

    # Common/dictionary words
    common_words = ["password", "12345678", "qwerty", "abcdefgh"]
    if any(word in password.lower() for word in common_words):
        suggestions.append("Avoid using common words or patterns.")
    else:
        score += 1

    # Strength decision
    if score >= 6:
        strength = "Very Strong"
        color = "darkgreen"
    elif score >= 4:
        strength = "Strong"
        color = "green"
    elif score >= 2:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"

    return strength, suggestions, color

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-password', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password', '')
    strength, suggestions, color = check_password_strength(password)
    return jsonify({
        'strength': strength,
        'suggestions': suggestions,
        'color': color
    })

if __name__ == '__main__':
    app.run(debug=True)
