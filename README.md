# secure-login-system
# 🔐 Secure Login System (Flask)

## 📌 Project Overview

The **Secure Login System** is a web-based authentication application developed using **Flask (Python)** that demonstrates secure coding practices for user authentication.

It is designed to protect user credentials and prevent common cyber threats such as:

* SQL Injection
* Password attacks
* Session hijacking (basic level)

This project is ideal for cybersecurity students, SOC analyst aspirants, and developers who want to understand **secure authentication mechanisms**.

---

## 🎯 Objectives

* Build a secure user authentication system
* Implement password hashing using **bcrypt**
* Protect against SQL Injection using parameterized queries
* Manage user sessions securely
* Implement optional **Two-Factor Authentication (2FA)**
* Demonstrate real-world secure coding practices

---

## 🚀 Features

### 🔑 Authentication System

* User Registration
* Secure Login
* Logout functionality
* Session-based authentication

### 🔐 Security Features

* Password hashing using **bcrypt**
* Protection against SQL Injection
* Input validation
* Secure session handling

### 📲 Two-Factor Authentication (Optional)

* TOTP-based OTP verification
* Compatible with apps like Google Authenticator

---

## 🛠️ Tech Stack

| Technology | Purpose          |
| ---------- | ---------------- |
| Python     | Backend logic    |
| Flask      | Web framework    |
| SQLite     | Database         |
| bcrypt     | Password hashing |
| pyotp      | OTP generation   |
| HTML/CSS   | Frontend         |

---

## 📁 Project Structure

```
secure-login-system/
│── app.py
│── config.py
│── requirements.txt
│── README.md
│── database.db
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│
├── static/
│   └── style.css
│
└── utils/
    ├── db.py
    ├── hash.py
    └── auth.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/secure-login-system.git
cd secure-login-system
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate:

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 🔐 Security Implementation Details

### 1. Password Hashing

* Uses **bcrypt hashing algorithm**
* Passwords are never stored in plain text
* Salt is automatically applied

### 2. SQL Injection Protection

* Uses **parameterized queries**
* Prevents malicious SQL execution

### 3. Session Management

* Flask session is used
* Stores user login state securely
* Session destroyed on logout

### 4. Two-Factor Authentication (2FA)

* Uses **TOTP (Time-based One-Time Password)**
* Secret key generated per user
* OTP verified during login

---

## 🔄 Application Flow

### 📝 Registration

1. User enters username & password
2. Password is hashed using bcrypt
3. User data stored securely in database

### 🔓 Login

1. User enters credentials
2. Password is verified against hashed value
3. If 2FA enabled → OTP verification
4. Session created

### 📊 Dashboard Access

* Only accessible if logged in
* Unauthorized users are redirected

### 🚪 Logout

* Session destroyed
* User redirected to login page

---

## 🧪 Testing Scenarios

You can test the system with:

* ✅ Valid login
* ❌ Invalid password
* ❌ SQL Injection attempt (`' OR 1=1 --`)
* ❌ Wrong OTP
* ✅ Session logout

---

## 📊 Expected Outcome

* Secure authentication system
* Protection against common web vulnerabilities
* Improved understanding of:

  * Password security
  * Authentication flows
  * Secure coding practices

---

## ⚠️ Limitations

* Basic UI (not production-ready)
* No HTTPS (local development only)
* No rate limiting
* No account lockout mechanism

---

## 🔮 Future Improvements

* 🔒 HTTPS deployment
* 🔁 Password reset via email
* 🔐 OAuth (Google/GitHub login)
* 🤖 CAPTCHA integration
* 📉 Rate limiting (prevent brute force)
* 🧾 Logging & monitoring

---

## 💡 Learning Outcomes

After completing this project, you will understand:

* Secure password storage
* Authentication workflows
* Session management
* Basic web security principles
* Implementation of 2FA

---

## 📷 Screenshots (Add Later)

* Registration Page
* Login Page
* Dashboard

---

## 🤝 Contribution

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Make changes
4. Submit a pull request

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Atharv Shinde**
📧 [4uatharv@gmail.com](mailto:4uatharv@gmail.com)

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share with others

---

##
