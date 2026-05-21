# 🔐 Secure Login System

A Secure Login System built using Python, Flask, SQLite, and Bcrypt that provides secure user authentication with hashed passwords, session management, and protection against common web attacks like SQL Injection.

---

## 🚀 Features

- 🔑 User Registration and Login  
- 🔒 Password Hashing using Bcrypt  
- 🛡️ SQL Injection Protection  
- ✅ Input Validation for Secure Authentication  
- 🍪 Session Management with Logout  
- 💾 SQLite Database Integration  
- 🌐 Simple Flask Web Interface  
- ⚠️ Prevents Unauthorized Access  

---

## 🧠 How It Works

1. User registers with username and password  
2. Password is securely hashed using Bcrypt  
3. User data is stored safely in SQLite database  
4. During login:
   - User credentials are validated
   - Password hash is verified  
5. Session is created after successful login  
6. Protected dashboard is accessible only to authenticated users  
7. Logout destroys active session securely  

---

## 🛠️ Tech Stack

- Python  
- Flask  
- SQLite  
- Flask-Bcrypt  
- HTML  
- CSS  
- JavaScript  

---

## 📁 Project Structure

```bash
secure_login_system/
│
├── app.py
├── requirements.txt
├── .env
│
├── database/
│   └── users.db
│
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
└── utils/
    └── db.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/vrxayush/secure-login-system.git

cd secure-login-system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

#### Windows

```bash
.\venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run Flask App

```bash
python app.py
```

---

## 🌐 Open in Browser

```bash
http://127.0.0.1:5000
```

---

## 🔒 Security Features

The system includes:

- ✅ Password Hashing using Bcrypt  
- ✅ Session-Based Authentication  
- ✅ Secure Logout System  
- ✅ SQL Injection Protection using Parameterized Queries  
- ✅ Input Validation  
- ✅ Protected Routes for Logged-in Users  

---

## 🔑 Example Credentials

### 👤 Register Example

```text
Username: admin
Password: admin123
```

---

## ⚠️ Important Notes

- Never store plain text passwords  
- Use strong secret keys in production  
- Enable HTTPS for deployment  
- Change debug mode to False before production  
- Always validate user inputs  

---

## 📈 Future Improvements

- 📲 Two-Factor Authentication (2FA)  
- 📧 Email Verification  
- 🔁 Forgot Password System  
- 🔐 JWT Authentication  
- 🚫 Login Attempt Limiter  
- 🤖 CAPTCHA Protection  
- ☁️ Cloud Deployment Support  
- 🗄️ MySQL/PostgreSQL Integration  

---

## 🎯 Use Case

This project demonstrates:

- Secure Authentication Systems  
- Password Hashing Techniques  
- Session Management  
- Flask Web Development  
- Cyber Security Concepts  
- Database Handling with SQLite  
- Secure User Access Control  

---

## 👨‍💻 Author

Ayush Shah  
Computer Science Engineering Student  
Interest: Cyber Security, AI, IoT & Software Development
