from flask import Flask, render_template, request, flash
import os
from generator import generate_secure_password

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure cryptographically random key for flash tracking

# NIST 2024 Guideline Constants
MIN_LENGTH = 15
MAX_LENGTH = 64

@app.route("/", methods=["GET", "POST"])
def index():
    password = None
    error_message = None
    
    if request.method == "POST":
        # Phase 1: Input Gathering & Strict Data Validation
        raw_length = request.form.get("length", "").strip()
        
        # Rigorous input phase checking to prevent backend type errors or system vulnerabilities
        if not raw_length.isdigit():
            error_message = "Data validation error: Password length must be a valid positive integer."
        else:
            length_integer = int(raw_length)
            
            # Enforcing NIST SP 800-63-4 high-security context lengths
            if length_integer < MIN_LENGTH:
                error_message = f"Security Violation: NIST 2024 guidelines require a minimum length of {MIN_LENGTH} characters."
            elif length_integer > MAX_LENGTH:
                error_message = f"System Restriction: Maximum allowable length is {MAX_LENGTH} characters to maintain memory efficiency."
            else:
                # Phase 2 & 3: Execution of transformation engine and provision delivery
                try:
                    password = generate_secure_password(length_integer)
                except Exception as e:
                    error_message = f"An internal processing error occurred: {str(e)}"
                    
    return render_template("index.html", password=password, error=error_message)

if __name__ == "__main__":
    app.run(debug=True) 