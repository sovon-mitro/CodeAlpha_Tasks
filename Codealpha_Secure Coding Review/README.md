# Secure Coding Review – Python Flask Web Application

## Overview

This project presents a security review of a Python Flask web application developed for educational purposes.

The application provides user registration and login functionality using SQLite.

The project demonstrates how common web application vulnerabilities were identified, analyzed, and remediated.

---

## Technologies

- Python
- Flask
- SQLite
- Werkzeug
- Bandit

---

## Vulnerabilities Identified

- Cross-Site Scripting (XSS)
- SQL Injection
- Plaintext Password Storage
- Password Disclosure
- Flask Debug Mode Enabled

---

## Security Review Process

The application was reviewed using:

- Manual source code inspection
- Manual security testing
- Static analysis using Bandit

---

## Remediation

The following secure coding techniques were applied:

- Parameterized SQL queries
- Password hashing
- HTML escaping with Jinja2
- Secure Flask configuration
- Removal of password disclosure

---

## Final Result

After remediation, the application was tested again.

Bandit reported:

**No issues identified**

---

## Repository Structure

```
secure-coding-review
│
├── report
├── secure_app
├── vulnerable_app
├── README.md
└── requirements.txt
```

---

## Disclaimer

The vulnerable application is included only for educational purposes and should not be deployed in production.