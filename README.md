# Genpass

Genpass is a strong, simple, and straightforward password generator created in **Python 3.13**. It allows you to create secure and custom passwords directly from your command line.

## Installation

To use Genpass, you need to have Python 3.13 or a newer version installed, The project doesn't require any external libraries, so you can run it directly.

1. Clone the repository:
```bash
git clone https://github.com/devtools-py/genpass.git
cd genpass
```

2. Run the program:
```bash
python3 genpass.py
```

## How to Use

Genpass offers some command-line option to customize the generated password.

### Options

- `-l <length>`: Sets the **password length**. The value must be an integer. The **minimum is 12**, and the **default is 16** if not specified.

- `-d <characters>`: Allows you to **remove unwanted characters** from the character set. The program ensures that the password will always contain uppercase letters, lowercase letters, numbers and symbols. It will generate an error if you try to remove all characters from one of the aforementioned sets.

### Examples
1. **Generate a password with the default length (16):**
```bash
python3 genpass.py
```

2. **Generate a password with 24 characters:**
```bash
python genpass.py -l 24
```

3. **Generate a password, removing the characters "i" and "o":**
```bash
python3 genpass.py -d io
```

4. **Generate a password with 18 characters, removing the "@" character:**
```bash
python3 genpass.py -l 18 -d @
```
