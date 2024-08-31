import cv2  # OpenCV for image processing
from pyzbar.pyzbar import decode  # pyzbar for barcode/QR code decoding
import re  # Regular expression for email validation

# In-memory storage simulated as a list of dictionaries
database = []

# Lambda functions for database operations
create_user_record = lambda name, email: {"name": name, "email": email}
insert_user_record = lambda record: database.append(record)
fetch_all_user_records = lambda: database

# Email validation function
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# Function to read and decode the SmartScan Code
def scan_smartscan_code(image_path):
    image = cv2.imread(image_path)
    barcodes = decode(image)
    if barcodes:
        barcode_data = barcodes[0].data.decode('utf-8')
        return barcode_data
    else:
        return None

# Function to register users from a SmartScan Code
def RegisterUsersFromSmartScan(image_path):
    user_data = scan_smartscan_code(image_path)
    if user_data:
        users = user_data.split(';')  # Split multiple users by semicolon
        for user in users:
            name, email = user.split(',')
            if is_valid_email(email):
                user_record = create_user_record(name, email)
                insert_user_record(user_record)
                print(f"User {name} registered successfully!")
            else:
                print(f"Invalid email format for {name}.")
    else:
        print("No valid SmartScan Code found in the image.")
    
    # Print all registered users
    print("All registered users:")
    for user in fetch_all_user_records():
        print(user)
