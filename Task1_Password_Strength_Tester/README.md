# 🔐 Password Strength Checker

A real-time password strength checker web application built using **Python (Flask)** and **HTML/CSS**, developed as part of a cybersecurity project for **CloudCredits Technology Pvt. Ltd.**

## 📌 Project Objective

This project helps users create strong and secure passwords by providing:
- Real-time strength evaluation
- Security suggestions
- Visual color-coded feedback
- Detection of weak/common passwords

## 🧠 Features

- ✅ Server-side password analysis (no client-side logic)
- ✅ Scoring system based on complexity (length, case, numbers, symbols)
- ✅ Common password detection
- ✅ Password visibility toggle
- ✅ Clean and responsive user interface

## 🚀 Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, minimal JavaScript
- **Tools**: VS Code, Postman, Git

## 🛠️ How It Works

1. User types a password in the input field.
2. Frontend sends password to Flask backend via `fetch()` (AJAX).
3. Server evaluates password strength using regex and rules.
4. Response contains:
   - Strength label (Weak, Moderate, Strong, Very Strong)
   - Color for UI
   - Suggestions to improve
5. Results are displayed dynamically without page reload.

## 📂 Project Structure

📁 project-root/
├── app.py # Flask backend
├── templates/
│ └── index.html # Main UI
├── README.md # Project info


## ▶️ How to Run

1. **Clone the repository**
```bash
git clone https://github.com/your-username/cloudcredits-password-checker.git
cd cloudcredits-password-checker

2.#install dependencies
pip install flask

3.run application
python app.py

4. open in browser
http://localhost:5000/


Sample password 
| Password        | Strength    | Reason                                 |
| --------------- | ----------- | -------------------------------------- |
| `123456`        | Weak        | Common, short, no complexity           |
| `Qwerty2024`    | Moderate    | Medium length, no special characters   |
| `P@ssw0rd2024!` | Very Strong | Long, mixed case, number, special char |

