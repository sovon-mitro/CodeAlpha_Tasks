# Secure Flask Application

## Overview

This directory contains the remediated version of the Python Flask web application after the Secure Coding Review.

The identified security vulnerabilities were corrected using secure coding practices.

## Security Improvements

The following security enhancements were implemented:

- Parameterized SQL queries to prevent SQL Injection
- Password hashing using Werkzeug
- HTML escaping using Jinja2 templates
- Removal of password disclosure
- Flask debug mode disabled

## Verification

The remediated application was verified using:

- Manual security testing
- Functional testing
- Bandit static analysis

The final Bandit scan reported:

**No issues identified.**

## Purpose

This version demonstrates how secure coding practices can significantly improve the security of a web application.