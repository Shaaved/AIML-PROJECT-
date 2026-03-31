import time
import os
from cryptography.fernet import Fernet

class SecureMessenger:
    """
    A human-friendly class to handle the encryption and decryption
    of private conversations without needing external key files.
    """
    
    def __init__(self, user_name):
        self.user_name = user_name
        # We generate a unique 'Master Key' for this session only.
        # This stays in RAM and is never saved to your hard drive.
        self.session_key = Fernet.generate_key()
        self.cipher_engine = Fernet(self.session_key)
        self.conversation_history = []

    def clear_screen(self):
        """Clears the terminal to keep the chat looking clean."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def encrypt_data(self, plain_text):
        """
        Takes a human readable string and transforms it into 
        an unreadable cryptographic token.
        """
        # Step 1: Convert the string into bytes (0s and 1s)
        text_bytes = plain_text.encode()
        
        # Step 2: Use the AES algorithm to scramble those bytes
        encrypted_token = self.cipher_engine.encrypt(text_bytes)
        
        return encrypted_token

    def decrypt_data(self, secret_token):
        """
        Takes a scrambled token and uses the Master Key to
        bring back the original human words.
        """
        try:
            # The engine checks if the key matches and if the data was tampered with
            decrypted_bytes = self.cipher_engine.decrypt(secret_token)
            return decrypted_bytes.decode()
        except Exception as e:
            return f"Error: Could not unlock message. {e}"

    def run_demo(self):
        """The main loop that makes the code interactive."""
        self.clear_screen()
        print(f"--- Welcome to the SecureVault, {self.user_name}! ---")
        print("Everything you type here is encrypted instantly in memory.\n")

        while True:
            user_msg = input("Type a secret message (or 'exit' to quit): ")

            if user_msg.lower() == 'exit':
                print("\nDestroying session keys... Goodbye!")
                break

            print("\n[ACTION] Encrypting your words...")
            time.sleep(0.5) # Adding a small delay for visual effect
            
            # --- THE ENCRYPTION PHASE ---
            secret_package = self.encrypt_data(user_msg)
            
            print(f"STACK TRACE (What a hacker sees):")
            print(f"{secret_package.decode()}\n")
            
            print("[ACTION] Passing through secure tunnel...")
            time.sleep(0.8)

            # --- THE DECRYPTION PHASE ---
            final_result = self.decrypt_data(secret_package)
            
            print(f" RECIPIENT VIEW: {final_result}")
            print("-" * 50)

# --- STARTING THE PROGRAM ---
if __name__ == "__main__":
    # We name our 'human' user
    my_app = SecureMessenger(user_name="User1")
    
    try:
        my_app.run_demo()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Keys wiped.")