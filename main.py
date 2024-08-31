import smartscan_registration_module as srm

# Path to the SmartScan Code image
image_path = 'pylab3/multiple_users_qr_code.png'

# Register users from the SmartScan Code
srm.RegisterUsersFromSmartScan(image_path)
