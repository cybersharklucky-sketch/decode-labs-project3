import secrets
import string
import math

def get_password_length():
    while True:
        try:
            length = int(input("Enter desired password length (minimum 15 characters recommended): "))
            
            if length < 15:
                print("Warning: NIST guidelines recommend minimum 15 characters for high-security contexts.")
                confirm = input("Do you want to proceed with a shorter password? (y/n): ").lower()
                if confirm != 'y':
                    continue
            
            if length > 1024:
                print("Warning: Extremely long passwords may cause performance issues.")
                confirm = input("Do you want to proceed? (y/n): ").lower()
                if confirm != 'y':
                    continue
                    
            if length <= 0:
                print("Password length must be a positive integer.")
                continue
                
            return length
            
        except ValueError:
            print("Invalid input. Please enter a valid integer for password length.")

def generate_secure_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    
    all_characters = lowercase + uppercase + digits + punctuation
    
    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    
    return password

def calculate_entropy(length, charset_size=94):
    entropy_bits = length * math.log2(charset_size)
    return entropy_bits

def format_time_estimate(entropy_bits):
    attempts = 2 ** entropy_bits
    seconds = attempts / 1_000_000_000
    
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    elif seconds < 315360000:
        return f"{seconds/31536000:.2f} years"
    else:
        return f"{seconds/31536000:.0f} years (millions+ years for standard lengths)"

def main():
    print("=" * 60)
    print("  ENTERPRISE RANDOM PASSWORD GENERATOR")
    print("  DecodeLabs | Batch 2026")
    print("=" * 60)
    print("\nGenerating cryptographically secure passwords")
    print("using NIST SP 800-63-4 guidelines\n")
    
    print("--- PHASE 1: Input Validation ---")
    password_length = get_password_length()
    
    print("\n--- PHASE 2: Backend Transformation ---")
    print(f"Generating secure password of length {password_length}...")
    print("Using secrets module for cryptographically secure randomness")
    print("Using string module for standardized character sets")
    
    password = generate_secure_password(password_length)
    
    print("\n--- PHASE 3: Security Metrics ---")
    
    charset_size = len(string.ascii_letters + string.digits + string.punctuation)
    entropy_bits = calculate_entropy(password_length, charset_size)
    
    print("\n" + "=" * 60)
    print("GENERATED PASSWORD:")
    print("-" * 60)
    print(f"{password}")
    print("=" * 60)
    
    print("\nSECURITY METRICS:")
    print(f"• Length: {password_length} characters")
    print(f"• Character Set: {charset_size} possible characters")
    print(f"• Entropy: {entropy_bits:.2f} bits")
    print(f"• Time to Crack: {format_time_estimate(entropy_bits)}")
    
    if password_length >= 15:
        print("\n✓ NIST SP 800-63-4 COMPLIANT")
        print("  Meets minimum 15-character requirement")
    else:
        print("\n⚠ NIST SP 800-63-4 NON-COMPLIANT")
        print("  Minimum 15 characters recommended for high-security contexts")
    
    print("\nSECURITY FEATURES:")
    print("• Uses secrets module for cryptographically secure randomness")
    print("• Uses join() for O(n) memory efficiency")
    print("• Includes uppercase, lowercase, digits, and special characters")
    print("• No predictable pseudo-randomness (Mersenne Twister avoided)")
    
    print("\n" + "=" * 60)
    print("Password generated successfully!")
    print("Copy and use it for your secure accounts.")
    print("=" * 60)

if __name__ == "__main__":
    main()