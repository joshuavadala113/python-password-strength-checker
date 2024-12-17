# High-End Password Strength Checker

## Overview
This Python-based password strength checker evaluates passwords based on various criteria such as length, character diversity, entropy, and common password checks. The program also integrates advanced password strength estimation using the zxcvbn library.

## Features:
- **Password Length Validation**: Ensures the password is within a valid length range (e.g., 8 to 16 characters).
- **Character Diversity**: The password must include at least one uppercase letter, one lowercase letter, one digit, and one special character.
- **Common Password Check**: Checks if the password is too common (e.g., "password123", "123456").
- **Password Entropy Calculation**: Estimates the randomness and strength of the password based on entropy (higher entropy indicates stronger randomness).
- **Advanced Strength Scoring via zxcvbn**: Uses the `zxcvbn` library to estimate the password's strength with a detailed score.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/joshuavadala113/password-strength-checker.git
   cd password-strength-checker
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python password_checker.py
   ```

2. **Enter a password** when prompted. The script will evaluate the password based on the criteria outlined.

## Example Output:
```
Enter password to check its strength: Example123!
Password is strong (Score: 5, Entropy: 60.02 bits).
```

