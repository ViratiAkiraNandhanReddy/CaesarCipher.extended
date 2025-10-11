'''
# CaesarCipher.Encryption Module

The Caesar cipher is a classic encryption technique that shifts each character in the input text by a fixed number of positions. \
Traditionally, it operates on alphabetic characters, wrapping around the alphabet if necessary.

## Key Features
- **Simple substitution**: Each character is replaced by another character a fixed distance away.
- **Configurable shift**: The number of positions to shift can be set by the user.
- **Alphabet wrapping**: Shifting beyond 'z' or 'Z' wraps around to the start of the alphabet.
- **Optional digit and symbol shifting**: Digits and non-alphanumeric symbols can also be shifted if desired.

## Use Cases
- Basic text obfuscation
'''

LOWERCASEASCII: int = 97
UPPERCASEASCII: int = 65
DIGITASCII: int = 48

class Encryption:

    ''' <!-- Detailed Description --> 
    # *Encryption Class*

    > The `Encryption` class provides a flexible implementation of the Caesar cipher algorithm, allowing users to encrypt text by shifting \
    alphabetic characters, digits, and optionally symbols. It is designed for educational, demonstration, and basic obfuscation purposes.

    ## <ins>*Parameters*</ins>

    - **text** (`str`):  
    The input string to be encrypted. Can contain letters, digits, and symbols.

    - **shift** (`int`, default=`3`):  
    The number of positions each character will be shifted.

    - **alterSymbols** (`bool`, default=`False`):  
    If `True`, non-alphanumeric symbols will also be shifted by the specified amount. If `False`, symbols remain unchanged.

    - **alterNumbers** (`bool`, default=`False`):  
    If `True`, digits (`0-9`) will be shifted by the specified amount, wrapping around after `9`. If `False`, digits remain unchanged.

    ## <ins>*Methods*</ins>

    ### `encrypt() -> str`
    > Encrypts the input text using the Caesar cipher algorithm and the specified options.

    #### <ins>*Returns*</ins>
    - **`str`**: The encrypted version of the input text.

    #### <ins>*Algorithm Details*</ins>
    
    - **Lowercase letters** (`a-z`): Shifted within the lowercase alphabet, wrapping around after `z`.
    - **Uppercase letters** (`A-Z`): Shifted within the uppercase alphabet, wrapping around after `Z`.
    - **Digits** (`0-9`): If `alterNumbers` is `True`, shifted within the digit range, wrapping after `9`.
    - **Symbols**: If `alterSymbols` is `True`, shifted by the specified amount using ASCII values.
    - **Other characters**: Remain unchanged unless symbol shifting is enabled.

    ## <ins>*Example Usage*</ins>

    ```python
    # Basic encryption of text
    Encryption_cls_obj = Encryption("Hello, World! 123", shift = 5, alterNumbers = True, alterSymbols = True)
    Encrypted_text = Encryption_cls_obj.encrypt()
    print(Encrypted_text)

    # Encrypt only letters, leave digits and symbols unchanged
    Encryption_cls_obj = Encryption("Secret123!", shift = 2)
    print(Encryption_cls_obj.encrypt())
    ```

    ## <ins>*Notes*</ins>

    - The algorithm supports shifting lowercase and uppercase letters, digits (if enabled), and symbols (if enabled).
    - Symbol shifting uses ASCII values and may result in non-printable or unexpected characters.
    - Only basic ASCII characters are supported for shifting; Unicode support is limited.
    - This algorithm is useful for small to mid-scale projects where basic encryption is preferred over storing plain text.
    - While not suitable for high-security needs, it can be used to obscure sensitive information such as passwords, making it harder to read at a glance or in logs.
    - For decryption, this library provides a separate `Decryption` class that reverses the encryption process using the same shift value.
    - ***Always use the same shift value for both encryption and decryption to ensure correct results.***
    - ***emoji were also supported but use with caution.***
    
    ## <ins>*Limitations*</ins>

    - It is vulnerable to brute-force and frequency analysis attacks.
    - Symbol shifting may produce non-printable or unexpected characters.
        
    ### Developed by [ViratiAkiraNandhanReddy](https://github.com/ViratiAkiraNandhanReddy)
    '''

    def __init__(self, text: str, shift: int = 3, alterSymbols: bool = False, alterNumbers: bool = False):

        if not isinstance(text, str):
            raise TypeError("text must be a string")
        if not isinstance(shift, int):
            raise TypeError("shift must be an integer")
        if not isinstance(alterSymbols, bool):
            raise TypeError("alterSymbols must be a boolean")
        if not isinstance(alterNumbers, bool):
            raise TypeError("alterNumbers must be a boolean")
        
        if shift < 0:
            raise ValueError("shift must be a non-negative integer")

        self.text: str = text
        self.shift: int = shift
        self.alterSymbols: bool = alterSymbols
        self.alterNumbers: bool = alterNumbers

    def encrypt(self) -> str:
        
        '''***Encrypts the input text using the Caesar cipher algorithm and returns the encrypted text.***'''
    
        EncryptedText: list[str] = []

        for char in self.text:

            if char.isalpha() and char.islower() :
                # Encrypt lowercase letters
                EncryptedText.append(chr((ord(char) - LOWERCASEASCII + self.shift) % 26 + LOWERCASEASCII))
            
            elif char.isalpha() and char.isupper():
                # Encrypt uppercase letters
                EncryptedText.append(chr((ord(char) - UPPERCASEASCII + self.shift) % 26 + UPPERCASEASCII))
            
            elif char.isdigit() and self.alterNumbers:
                # Encrypt digits
                EncryptedText.append(chr((ord(char) - DIGITASCII + self.shift) % 10 + DIGITASCII))
            
            elif not char.isalnum() and self.alterSymbols:
                # Encrypt symbols
                try: EncryptedText.append(chr(ord(char) + self.shift))
                except ValueError as e: raise ValueError('either the shift is too high or the character is unsupported') from e
                
            else:
                # Non-alphabetic characters remain unchanged
                EncryptedText.append(char)

        return ''.join(EncryptedText)