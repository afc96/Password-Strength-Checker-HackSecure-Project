import string
import getpass # To securely get password input without echoing
import datetime # To fix NameError for datetime.now()
import warnings # To suppress the GetPassWarning

# --- Suppress GetPassWarning ---
from getpass import GetPassWarning
warnings.filterwarnings("ignore", category=GetPassWarning)

# --- Constants for Configuration ---
MIN_LENGTH = 8
GOOD_LENGTH = 12 # Length considered for a higher base score

# Scoring points
POINTS_GOOD_LENGTH = 2
POINTS_MIN_LENGTH = 1
POINTS_LOWER = 1
POINTS_UPPER = 1
POINTS_DIGIT = 1
POINTS_SPECIAL = 2 # Increased weight for special characters

# Penalties
PENALTY_SEQUENCE = 1 # Penalty for finding sequences (abc, 123)
PENALTY_REPETITION = 1 # Penalty for finding repetitions (aaa, 111)

# Score thresholds for NEW strength categories
THRESHOLD_WEAK = 1       # Score > this threshold is Weak or better
THRESHOLD_MODERATE = 3   # Score > this threshold is Moderate or better
THRESHOLD_STRONG = 4     # Score > this threshold is Strong or better
THRESHOLD_VERY_STRONG = 5 # Score > this threshold is Very Strong

# --- Helper Functions for Weakness Detection ---

def detect_sequences(password, length=3):
    """
    Detects simple alphabetical (abc) and numerical (123) sequences.
    Checks for sequences of specified length (default 3).
    """
    if len(password) < length:
        return False
    password_lower = password.lower() # Case-insensitive check for alphabetical

    for i in range(len(password_lower) - length + 1):
        substring = password_lower[i:i+length]

        # Check for numerical sequence (e.g., '123')
        if substring.isdigit():
            is_num_seq = True
            for j in range(length - 1):
                if int(substring[j+1]) != int(substring[j]) + 1:
                    is_num_seq = False
                    break
            if is_num_seq:
                return True

        # Check for alphabetical sequence (e.g., 'abc')
        if substring.isalpha():
            is_alpha_seq = True
            for j in range(length - 1):
                 # Use ord() to check character codes
                if ord(substring[j+1]) != ord(substring[j]) + 1:
                    is_alpha_seq = False
                    break
            if is_alpha_seq:
                return True

    return False # No simple sequences found

def detect_repetitions(password, length=3):
    """
    Detects simple character repetitions (e.g., aaa, 111).
    Checks for repetitions of specified length (default 3).
    """
    if len(password) < length:
        return False

    for i in range(len(password) - length + 1):
        substring = password[i:i+length]
        first_char = substring[0]
        is_repetition = True
        for char in substring[1:]:
            if char != first_char:
                is_repetition = False
                break
        if is_repetition:
            return True
    return False # No simple repetitions found


# --- Main Strength Checking Function ---

def check_password_strength(password):
    """
    Evaluates the strength of a password based on predefined criteria,
    including penalties for sequences and repetitions.
    Provides more specific feedback and granular strength levels.

    Args:
        password (str): The password string to evaluate.

    Returns:
        str: A string indicating the password strength ("Very Weak", "Weak",
             "Moderate", "Strong", "Very Strong") along with specific feedback.
    """
    length = len(password)
    score = 0
    missing_criteria = []
    weakness_found = [] # Track detected weaknesses

    # --- Initial Length Check ---
    if length < MIN_LENGTH:
        return f"Very Weak (Too Short - minimum {MIN_LENGTH} characters recommended)"

    # --- Scoring Based on Criteria ---
    # 1. Length Score
    if length >= GOOD_LENGTH:
        score += POINTS_GOOD_LENGTH
    elif length >= MIN_LENGTH:
        score += POINTS_MIN_LENGTH

    # 2. Character Type Score & Check
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    special_characters = string.punctuation
    has_special = any(c in special_characters for c in password)

    # Add points and track missing criteria
    if has_lower: score += POINTS_LOWER
    else: missing_criteria.append("lowercase letters")
    if has_upper: score += POINTS_UPPER
    else: missing_criteria.append("uppercase letters")
    if has_digit: score += POINTS_DIGIT
    else: missing_criteria.append("numbers")
    if has_special: score += POINTS_SPECIAL
    else: missing_criteria.append("special characters (!@#...)")

    # 3. Penalties for Weaknesses
    penalty = 0
    if detect_sequences(password):
        penalty += PENALTY_SEQUENCE
        weakness_found.append("contains sequences (like 'abc' or '123')")
    if detect_repetitions(password):
        penalty += PENALTY_REPETITION
        weakness_found.append("contains repetitions (like 'aaa' or '111')")

    final_score = max(0, score - penalty) # Ensure score doesn't go below 0

    # --- Determine Strength Category and Feedback ---
    # Max score = 7. Penalties can reduce it.
    # Very Weak: <= 1, Weak: 2-3, Moderate: 4, Strong: 5, Very Strong: >= 6
    if final_score <= THRESHOLD_WEAK: # <= 1
        strength = "Very Weak"
    elif final_score <= THRESHOLD_MODERATE: # <= 3
        strength = "Weak"
    elif final_score <= THRESHOLD_STRONG: # <= 4
        strength = "Moderate"
    elif final_score <= THRESHOLD_VERY_STRONG: # <= 5
        strength = "Strong"
    else: # >= 6
        strength = "Very Strong"

    # Construct feedback message
    feedback = strength
    details = []
    if missing_criteria:
        details.append(f"consider adding: {', '.join(missing_criteria)}")
    if length < GOOD_LENGTH and strength not in ["Strong", "Very Strong"]:
        details.append(f"consider increasing length to {GOOD_LENGTH}+ characters")
    if weakness_found:
         details.append(f"avoid patterns like: {', '.join(weakness_found)}")

    if details:
        feedback += f" ({'; '.join(details)})"

    return feedback

# --- Main program execution ---
if __name__ == "__main__":
    print("--- Enhanced Password Strength Checker ---")
    print("Checks for length, character types, sequences, and repetitions.")
    print("Enter passwords to evaluate. Type 'n' when asked to continue to quit.")

    while True:
        try:
            user_password = getpass.getpass("\nEnter the password to evaluate: ")
        except Exception as e:
            print(f"\nError getting password input: {e}")
            user_password = None

        if not user_password:
            print("No password entered. Please try again.")
            continue

        strength = check_password_strength(user_password)
        print(f"Password Strength: {strength}")

        try:
            another = input("\nCheck another password? (y/n): ").strip().lower()
            if another.startswith('n'):
                break
        except EOFError:
             break

    print("\nExiting program.")
    # Adding context requested
    print("\n---")
    print(f"Session ended on Sunday, April 13, 2025 at {datetime.datetime.now().strftime('%I:%M %p')} CAT.")
    print("Location context: Zimbabwe.")

