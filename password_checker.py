import re
import math
import string
from zxcvbn import password_strength

class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password
        self.min_length = 8
        self.max_length = 16
        self.strength_score = 0
        self.errors = []

    def validate_length(self):
        if len(self.password) < self.min_length or len(self.password) > self.max_length:
            self.errors.append(f"Password must be between {self.min_length} and {self.max_length} characters.")
        else:
            self.strength_score += 1

    def validate_character_diversity(self):
        if not re.search(r'[A-Z]', self.password):
            self.errors.append("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', self.password):
            self.errors.append("Password must contain at least one lowercase letter.")
        if not re.search(r'[0-9]', self.password):
            self.errors.append("Password must contain at least one digit.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', self.password):
            self.errors.append("Password must contain at least one special character.")
        else:
            self.strength_score += 2

    def check_common_passwords(self):
        common_passwords = ["123456", "password", "qwerty", "abc123"]
        if self.password.lower() in common_passwords:
            self.errors.append("Password is too common.")
        else:
            self.strength_score += 1

    def calculate_entropy(self):
        # Estimate password entropy
        unique_characters = len(set(self.password))
        entropy = math.log2(unique_characters ** len(self.password))
        if entropy < 40:
            self.errors.append("Password entropy is too low.")
        else:
            self.strength_score += 2
        return entropy

    def evaluate_strength(self):
        self.validate_length()
        self.validate_character_diversity()
        self.check_common_passwords()
        entropy = self.calculate_entropy()

        # Use zxcvbn to get a more advanced password strength score
        strength = password_strength(self.password)
        print(f"Strength according to zxcvbn: {strength['score']}")
        
        if len(self.errors) == 0:
            return f"Password is strong (Score: {self.strength_score}, Entropy: {entropy:.2f} bits)."
        else:
            return f"Weak password: {'; '.join(self.errors)}"
