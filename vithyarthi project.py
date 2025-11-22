import random
from datetime import datetime

# Apartment types and base prices (in lakhs)
apartment_prices = {
    "2BHK": 40,
    "3BHK": 70,
    "4BHK": 100,
    "penthouse": 200
}

# Special club benefits for early registrants
early_registration_benefit = 10  # Token money in lakhs

# Function to generate a unique token number
def generate_token():
    return random.randint(10000, 99999)

# Main booking function
def book_apartment():
    print("Welcome to the Apartment Booking System!")
    print("Available Apartments: 2BHK, 3BHK, 4BHK, penthouse")
    
    # Get user input
    name = input("Enter your name: ")
    apartment_type = input("Enter apartment type (2BHK/3BHK/4BHK/penthouse): ").strip().lower()
    is_corner = input("Is it a corner apartment? (yes/no): ").strip().lower() == "yes"
    is_early = input("Are you an early registrant? (yes/no): ").strip().lower() == "yes"
    payment_method = input("Enter payment method (cheque/cash/online): ").strip().lower()
    
    # Validate apartment type
    if apartment_type not in apartment_prices:
        print("Invalid apartment type!")
        return
    
    # Calculate base price
    base_price = apartment_prices[apartment_type]
    
    # Add corner apartment premium
    if is_corner:
        base_price += 5  # ₹5 lakhs extra for corner apartments
    
    # Add early registration token money
    total_price = base_price
    if is_early:
        total_price += early_registration_benefit
    
    # Generate token number
    token_number = generate_token()
    
    # Print bill receipt
    print("\n" + "="*50)
    print("           APARTMENT BOOKING RECEIPT")
    print("="*50)
    print(f"Name: {name}")
    print(f"Apartment Type: {apartment_type.upper()}")
    print(f"Corner Apartment: {'Yes' if is_corner else 'No'}")
    print(f"Early Registration: {'Yes' if is_early else 'No'}")
    print(f"Base Price: ₹{base_price} lakhs")
    if is_early:
        print(f"Token Money: ₹{early_registration_benefit} lakhs")
    print(f"Total Amount: ₹{total_price} lakhs")
    print(f"Payment Method: {payment_method.upper()}")
    print(f"Token Number: {token_number}")
    print(f"Booking Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if payment_method == "cheque":
        print("\nPayment Instructions:")
        print(f"Please pay ₹{total_price} lakhs by cheque within 3 working days.")
    else:
        print("\nPayment successful! Thank you for booking.")
    print("="*50)


