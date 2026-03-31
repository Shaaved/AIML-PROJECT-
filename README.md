
## Overview

SecureVault is a simple, high-security Python utility designed to demonstrate how real-time encryption works.

The standout feature of this program is its "In-Memory" security model. Unlike many apps that store keys in files on your computer, SecureVault generates a unique Master Key that lives only in your computer's RAM. Once you close the program or hit "Exit," that key is permanently destroyed, making the session's data impossible to recover even if someone has access to your hard drive.


## Features

Ephemeral Key Management: Session keys are generated on startup and never saved to disk.

Symmetric Encryption: Utilizes the cryptography library to ensure data integrity and confidentiality.

Visual Stack Trace: Shows the user exactly what a "hacker" would see (the encrypted token) versus the decrypted result.

Automatic Cleanup: Clears the terminal screen for a clean UI and handles keyboard interrupts (Ctrl+C) to wipe sessions safely.

Human-Centric Design: Simple interactive loop for testing messages in real-time.


## Tools & Technologies

Language: Python 3.x

Libraries: * cryptography: Specifically the Fernet module for AES-based encryption.

os: For cross-platform terminal management.

time: For simulating processing delays.


## Steps to Run

Follow these steps to get the environment ready and run the program:

Install Python: Ensure you have Python 3.8 or higher installed.

Install Dependencies: Open your terminal and run the following command to install the required library: pip install cryptography.

Download the Script: Save the code as secure_messenger.py.

Execute : Run the program.



## Test Cases for SecureVault


# Basic Message Success

Action: Type a simple sentence like This is a secret message.

Expected Result: The program displays a scrambled "Stack Trace" (the token) and successfully restores the original text in the "Recipient View."

# Handling Special Characters

Action: Enter symbols and numbers, such as Admin_Pass!@#2026.

Expected Result: The encryption engine should process these without errors, and the decryption should return the exact same symbols.

# Empty Input Test

Action: Press the Enter key without typing any text.

Expected Result: The program should not crash. It should generate an encrypted token for an empty string and show a blank "Recipient View."

# Session Exit Command

Action: Type the word exit (case-insensitive).

Expected Result: The loop should break immediately, the message "Destroying session keys... Goodbye!" should appear, and the program should close.

# Forceful Termination (Panic Button)

Action: Press Ctrl + C on your keyboard while the program is waiting for input.

Expected Result: The program should catch the interruption and print "Process interrupted by user. Keys wiped." instead of showing a messy Python error.

# Key Volatility (Security Check)

Action: Run the program, encrypt a word, then exit. Restart the program and try to think if the old message could be read.

Expected Result: Every time you restart, a new session_key is generated. This proves that messages from a previous session are now impossible to decrypt, confirming the "In-Memory" security feature works.

# Screenshot  1
<img width="1920" height="1080" alt="Screenshot 2026-03-28 152944" src="https://github.com/user-attachments/assets/52aa5b17-b6e5-4f05-acc7-b763606edca2" />

# Screenshot  2
<img width="1920" height="1080" alt="Screenshot 2026-03-28 152956" src="https://github.com/user-attachments/assets/313a55f5-0a03-4dc1-83c7-524e8e3575fe" />
