
## 🛡️ User Authentication System

A secure and user-friendly **User Authentication System** built with **Flask**, featuring:

* User registration and login
* Password hashing
* Real-time password strength checker
* Clean, responsive UI with custom CSS
* SQLite database integration

---

### 📌 Features

* ✅ User registration with validation
* ✅ Login/logout with session management
* ✅ Passwords stored securely (hashed using PBKDF2)
* ✅ Password strength meter (JavaScript)
* ✅ Prevents duplicate usernames
* ✅ Flash messages for feedback
* ✅ Modern UI with animated, curved background design

---

### 🖼️ Screenshots

<details>
<summary>Click to expand</summary>

* 🖼️ **Register Page**: Stylish form with live strength feedback
* 🖼️ **Login Page**: Consistent UI for returning users
* 🖼️ **Dashboard**: Shows logged-in username and logout option

</details>

---

### 🧰 Tech Stack

| Technology     | Usage                         |
| -------------- | ----------------------------- |
| **Python 3**   | Core programming language     |
| **Flask**      | Web framework                 |
| **SQLite**     | Lightweight database          |
| **Werkzeug**   | Secure password hashing       |
| **HTML/CSS**   | Frontend structure & styling  |
| **JavaScript** | Password strength checker     |
| **Bootstrap**  | (Optional) responsive styling |

---

### 📁 Project Structure

```
user-auth-system/
│
├── app.py               # Main Flask application
├── users.db             # SQLite database (auto-generated)
├── templates/
│   ├── base.html
│   ├── register.html
│   ├── login.html
│   └── dashboard.html
├── static/
│   └── style.css        # Custom CSS styling
├── view_users.py        # Script to view registered users
└── README.md            # Project documentation
```

---

### 🚀 Getting Started

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/user-auth-system.git
cd user-auth-system
```

#### 2. Install Dependencies

```bash
pip install flask
```

> Flask includes Jinja2, Werkzeug, and MarkupSafe.

#### 3. Run the App

```bash
python app.py
```

Go to: `http://127.0.0.1:5000/`

---

### 🔒 Security Features

* Passwords are never stored in plaintext.
* Minimum password length: 6 characters.
* Password strength validation with live feedback.
* Input sanitization and basic error handling.

---

### 🧪 Testing

Use `view_users.py` to view all registered users:

```bash
python view_users.py
```

Or inspect `users.db` using DB Browser for SQLite.

---

### 🧱 Future Improvements

* Role-based access (Admin/User)
* Email verification
* Password reset feature
* Two-factor authentication (2FA)
* OAuth or JWT integration for API support

---

### 📚 License

This project is open-source and free to use for learning or extension. Credit appreciated!

---

### 🙌 Acknowledgments

* Flask Documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
* OWASP: [https://owasp.org/](https://owasp.org/)
* SQLite Docs: [https://sqlite.org/docs.html](https://sqlite.org/docs.html)

---
