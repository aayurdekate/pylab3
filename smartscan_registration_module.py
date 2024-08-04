# smartscan_registration_module.py

from pyzbar.pyzbar import decode
from PIL import Image

# In-Memory Storage
user_records = []

# Lambda functions for managing user records
create_user_record = lambda name, email: {"name": name, "email": email}
insert_user_record = lambda record: user_records.append(record)
fetch_all_user_records = lambda: user_records

# SmartScan Code Scanning
def decode_smartscan_image(image_path):
    image = Image.open(image_path)
    decoded_objects = decode(image)
    for obj in decoded_objects:
        return obj.data.decode("utf-8")
    return None

# User Registration Function
def RegisterUserFromSmartScan(image_path):
    # Extract user data from the SmartScan Code
    user_data = decode_smartscan_image(image_path)
    if user_data:
        name, email = user_data.split(',')
        # Create a new user record
        new_user = create_user_record(name, email)
        # Insert the new user record into the in-memory list
        insert_user_record(new_user)
        # Print all registered users
        all_users = fetch_all_user_records()
        print("Registered Users:")
        for user in all_users:
            print(f"Name: {user['name']}, Email: {user['email']}")
    else:
        print("No user data found in the SmartScan Code.")
