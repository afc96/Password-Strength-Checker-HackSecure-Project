Password Strength Checker
Description
A Python script developed as part of the Hack Secure Cyber Security Internship (Red Teaming Batch 2025). This tool evaluates the strength of a given password based on multiple criteria:

Length

Presence of uppercase letters

Presence of lowercase letters

Presence of digits

Presence of special characters

Common sequences (alphabetical, numerical)

Character repetitions

It provides a rating (Very Weak, Weak, Moderate, Strong, Very Strong) and specific feedback to help users create stronger passwords.

Features
Multi-Criteria Analysis: Checks length, character variety, simple sequences, and repetitions.

Scoring System: Assigns points for positive attributes (length, character types) and deducts penalties for weaknesses (sequences, repetitions). Special characters are weighted slightly higher.

Granular Feedback: Provides five strength levels (Very Weak to Very Strong).

Specific Suggestions: Offers hints on how to improve weak or moderate passwords by listing missing character types, suggesting increased length, or warning about detected patterns.

Secure Input: Uses Python's getpass module to attempt to hide password input in the terminal.

Continuous Checking: Runs in a loop, allowing multiple passwords to be evaluated in one session until the user chooses to quit.

Configurable: Uses constants at the beginning of the script for easy adjustment of length requirements, scoring points, penalties, and strength thresholds.

How to Run / Usage
Prerequisites: Ensure you have Python 3 installed.

Save the Code: Save the script as a Python file (e.g., password_checker.py).

Execute: Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script using:

python password_checker.py

Interact:

The script will prompt you to "Enter the password to evaluate:". Type the password and press Enter (input may or may not be hidden depending on your terminal).

The script will output the calculated "Password Strength:" rating and feedback.

It will then ask "Check another password? (y/n):". Type 'y' to check another, or 'n' to quit.

Configuration
Key parameters for evaluation can be easily modified by changing the constant values defined near the top of the password_checker.py script:

MIN_LENGTH, GOOD_LENGTH: Adjust length requirements.

POINTS_...: Change scoring weights for different criteria.

PENALTY_...: Modify penalties for sequences/repetitions.

THRESHOLD_...: Adjust the score ranges for strength categories.

special_characters (defined within check_password_strength function): Customize the set of characters considered special.

Limitations
This script provides a basic heuristic evaluation and does not perform advanced checks such as:

Checking against dictionaries of common or breached passwords.

Detecting complex patterns (e.g., keyboard walks like 'qwerty').

Calculating cryptographic entropy.

A "Strong" or "Very Strong" rating indicates compliance with the script's rules but is not an absolute guarantee of security against all attack methods.

License
"This project is licensed under the MIT License."

Author
Anesuishe F Chinhoyi
