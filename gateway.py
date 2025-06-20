# gateway.py
import os
import csv

def check_user_file(file_path='users.csv'):
    if not os.path.exists(file_path):
        print("User file not found. Creating a new one...")
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'password'])
        print("User file created successfully.")
        return

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader, None)
        if header != ['username', 'password']:
            raise ValueError("Invalid user file format. Expected header: username, password")
    print("Gateway: User file validated ")

