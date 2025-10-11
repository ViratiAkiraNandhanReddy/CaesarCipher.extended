'''
# *CaesarCipher Encryption Package*

---
A simple, flexible, and educational Python package for encrypting and decrypting text using the classic Caesar cipher algorithm. \
This package is ideal for small to mid-scale projects where basic encryption is preferred over storing plain text, such as for usernames, \
passwords, or other sensitive information.

## <ins>*Overview*</ins>

The CaesarCipher package provides two main classes, `Encryption` and `Decryption`, for performing Caesar cipher-based encryption and decryption. \
The algorithm is extended to support not only alphabetic characters but also digits and symbols, making it versatile for various text processing needs.

This package is best suited for scenarios where some level of obfuscation is required, and storing plain text is not acceptable. \
While it is not intended for high-security applications, it offers a significant improvement over storing sensitive data in plain text.

## <ins>*Algorithm*</ins>

The **Caesar cipher** is a substitution cipher where each character in the input text is shifted by a fixed number of positions. \
Traditionally, it operates on alphabetic characters, wrapping around the alphabet if necessary. This package extends the algorithm to optionally shift digits and symbols as well.

- **Alphabetic characters**: Shifted within their respective case (lowercase or uppercase), wrapping around after 'z' or 'Z'.
- **Digits**: If enabled, shifted within the range 0-9, wrapping after '9'.
- **Symbols**: If enabled, shifted using ASCII values, wrapping at 256.

This approach provides basic obfuscation and is suitable for educational, demonstration, and simple data protection purposes.

## <ins>*Features*</ins>

- Encrypt and decrypt text using the Caesar cipher.
- Support for shifting letters, digits, and symbols.
- Input validation for all parameters.
- Easy-to-use API.
- Suitable for small to mid-scale projects.
- Much better than storing plain text for sensitive data.

## <ins>*Installation*</ins>

Install from PyPI:

```bash
pip install CaesarCipher
```

Or clone from GitHub:

```bash
git clone https://github.com/ViratiAkiraNandhanReddy/CaesarCipher.extended.git
cd CaesarCipher.extended
```

## <ins>*Usage*</ins>

### <ins>***Encryption Class***</ins>

```python
from CaesarCipher import Encryption

# Encrypt text with default settings
enc = Encryption("Hello, World! 123")
encrypted = enc.encrypt()
print(encrypted)

# Encrypt with custom shift and options
enc2 = Encryption("Secret123!", shift = 5, alterNumbers = True, alterSymbols = True)
print(enc2.encrypt())
```

### <ins>***Decryption Class***</ins>

```python
from CaesarCipher import Decryption

# Decrypt text with default settings
dec = Decryption("Khoor, Zruog! 456")
decrypted = dec.decrypt()
print(decrypted)

# Decrypt with custom shift and options
dec2 = Decryption("Xjhwjy678!", shift = 5, isNumbersAltered = True, isSymbolsAltered = True)
print(dec2.decrypt())
```

## <ins>*API Reference*</ins>

### <ins>***Encryption Class Details***</ins>

#### `Encryption(text: str, shift: int = 3, alterSymbols: bool = False, alterNumbers: bool = False)`

- **text**: The input string to encrypt.
- **shift**: Number of positions to shift each character (default: 3).
- **alterSymbols**: If `True`, non-alphanumeric symbols are shifted (default: `False`).
- **alterNumbers**: If `True`, digits are shifted (default: `False`).

#### `encrypt() -> str`

Encrypts the input text using the specified options and returns the encrypted string.

**Use Cases:**
- Obfuscating usernames, passwords, or other sensitive data.
- Educational demonstrations of classical cryptography.
- Simple data protection in small to mid-scale projects.

### <ins>***Decryption Class Details***</ins>

#### `Decryption(text: str, shift: int = 3, isSymbolsAltered: bool = False, isNumbersAltered: bool = False)`

- **text**: The encrypted string to decrypt.
- **shift**: Number of positions to shift each character back (default: 3).
- **isSymbolsAltered**: If `True`, non-alphanumeric symbols are shifted back (default: `False`).
- **isNumbersAltered**: If `True`, digits are shifted back (default: `False`).

#### `decrypt() -> str`

Decrypts the input text using the specified options and returns the original string.

**Use Cases:**
- Retrieving obfuscated data for authentication or display.
- Educational exercises in cryptography.

## <ins>*Limitations*</ins>

- **Security**: The Caesar cipher is not suitable for strong security needs. It is vulnerable to brute-force and frequency analysis attacks.
- **Symbol Shifting**: May produce non-printable or unexpected characters.
- **Character Support**: Only basic ASCII characters are supported for shifting; Unicode and special character support is limited.
- **Password Storage**: Not recommended for storing passwords in production—use proper cryptographic hashing instead.

## <ins>*Security Note*</ins>

While this package provides better protection than storing plain text, it is not a substitute for modern cryptographic algorithms. \
For production systems, especially those handling passwords or highly sensitive data, use strong hashing algorithms like bcrypt or Argon2.

## <ins>*Author & Social Links*</ins>
#### GitHub: [ViratiAkiraNandhanReddy](https://github.com/ViratiAkiraNandhanReddy)
#### Website: [viratiakiranandhanreddy.github.io](https://viratiakiranandhanreddy.github.io)
#### Repository: [CaesarCipher.extended](https://github.com/ViratiAkiraNandhanReddy/CaesarCipher.extended)
#### PyPI Package: [CaesarCipher](https://pypi.org/project/CaesarCipher/)
#### Project Website: https://viratiakiranandhanreddy.github.io/CaesarCipher.extended/
#### LinkedIn: [viratiakiranandhanreddy](https://linkedin.com/in/viratiakiranandhanreddy/)
#### X (Twitter): [Viratiaki53](https://x.com/Viratiaki53)
#### Instagram: [viratiaki53](https://instagram.com/viratiaki53/)
#### Gmail: viratiaki@gmail.com

> ***If you have any questions, suggestions, or want to contribute, feel free to reach out via GitHub!***

## <ins>*License*</ins>

***Copyright (C) 2025 ViratiAkiraNandhanReddy*** <br>
***This project is licensed under the `GNU GENERAL PUBLIC LICENSE`.***

### Developed and maintained by [**ViratiAkiraNandhanReddy**](https://github.com/ViratiAkiraNandhanReddy).

'''
from .Encryption import Encryption
from .Decryption import Decryption

__all__ = ['Encryption', 'Decryption']
__version__ = '2.9'
__author__ = 'ViratiAkiraNandhanReddy'
__license__ = 'GNU GENERAL PUBLIC LICENSE'
