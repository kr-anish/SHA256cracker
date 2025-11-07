# SHA256cracker
A simple SHA-256 offline dictionary cracker that uses a wordlist (e.g. rockyou.txt) to try to find the plaintext for a given SHA-256 hash. Built with pwntools for progress logging and convenience.
# Features
1. Simple, focused CLI tool.

2. Uses pwntools progress logging for a live progress/status display.

3. Reads wordlist with latin-1 encoding to support common password files such as rockyou.txt.

4. Prints attempts count and the password when found.

# Requirements
• Operating System : Linux , Windows , MacOS

• Dependencies : python3 , pwntools

• A wordlist file (e.g. rockyou.txt) in the same directory
if you have rockyou.txt in your kali then copy it to the working directory
```
sudo cp -v /usr/share/wordlists/rockyou.txt <destination>
```

• Install dependencies with pip:
```
pip install pwntools
```

# Setup Instructions
1. Clone the repository to your local machine:
```
git clone https://github.com/kr-anish/SHA256cracker
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Check if you have the wordlist in the working directory. If not then you can create your own wordlist and edit the script.
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/f3796a6d-338f-42f3-885c-621d37f10326" />

4. Run the script from the command line.
```
python3 sha256cracker.py <SHA256sum>
```

# Usage
Run the script providing a SHA-256 hash as the only argument:
```
python3 sha256cracker.py <SHA256sum>
```
If not it will generate an error
<img width="1914" height="907" alt="Image" src="https://github.com/user-attachments/assets/e023b107-1fac-4540-a070-e0c14a8093bc" />

If the password is found in rockyou.txt, the script prints a success message with the plaintext and the number of attempts.

egs:
<img width="1914" height="907" alt="Image" src="https://github.com/user-attachments/assets/10842149-8c63-4cc6-bb65-8b27254c2478" />

If not found, it prints a failure message when the wordlist is exhausted.

egs:
<img width="1914" height="907" alt="Image" src="https://github.com/user-attachments/assets/54f98b9c-12d3-4c12-bf13-99d97b243cb6" />

# Troubleshooting
• ModuleNotFoundError: No module named 'pwn' ---> install pwntools
```
pip3 install pwntools
```
• Encoding errors / unreadable characters — script opens the wordlist with latin-1 to be compatible with rockyou.txt. If your wordlist uses UTF-8, adapt open(..., encoding='latin-1').

• Permission/Path issues — ensure rockyou.txt is readable and in the same directory or update password_file variable to the correct path.

# Acknowledgements
• pwntools for friendly logging and utilities.

• The rockyou.txt wordlist (commonly used for testing/education).
