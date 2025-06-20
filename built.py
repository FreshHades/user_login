# built.py
import csv
import hashlib
from datetime import datetime

USER_FILE = 'users.csv'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    with open(USER_FILE, 'r') as file:
        reader = csv.DictReader(file)
        return {row['username']: row['password'] for row in reader}

def register():
    username = input("Choose a username: ")
    password = input("Choose a password: ")

    users = load_users()
    if username in users:
        print("Username already exists.")
        return

    with open(USER_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, hash_password(password)])
    print("Registration successful ")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    users = load_users()
    if username not in users:
        print("Username not found.")
        return

    if users[username] == hash_password(password):
        print(f"Welcome back, {username}! ")
        log_session(username)
    else:
        print("Incorrect password ")

def log_session(username):
    with open('logins.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, datetime.now().isoformat()])
    print("Login logged.")
