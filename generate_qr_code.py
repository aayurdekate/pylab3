import qrcode

def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_path)

# Multiple user information separated by semicolon
users = [
    "Ashvita Koli,ashvita.koli@example.com",
    "Shivangi Agarwal,shivangi.agarwal@example.com"
]
user_data = ";".join(users)

# File path to save the QR code
file_path = "multiple_users_qr_code.png"

# Generate QR code
generate_qr_code(user_data, file_path)

print(f"QR code generated and saved to {file_path}")
