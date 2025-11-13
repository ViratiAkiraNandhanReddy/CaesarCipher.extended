'''
# CaesarCipher.Decryption Module

Provides a class for decrypting text that was encrypted using the Caesar cipher algorithm. \
Supports reversing shifts for letters, digits, and optionally symbols.

## Overview

- Reverses the Caesar cipher encryption by shifting characters back by a specified amount.
- Supports lowercase and uppercase letters, digits (if enabled), and symbols (if enabled).
- Includes input validation for all parameters.

## Use Cases
- Basic text de-obfuscation
'''

LOWERCASEASCII: int = 97
UPPERCASEASCII: int = 65
DIGITASCII: int = 48

class Decryption:

    ''' <!-- Detailed Description -->
    # *Decryption Class*

    > The `Decryption` class provides a robust implementation for reversing the Caesar cipher algorithm. \
    It allows users to decrypt text that was previously encrypted by shifting alphabetic characters, digits, \
    and optionally symbols back by a specified amount.

    ## <ins>*Parameters*</ins>

    - **text** (`str`):  
    The encrypted string to be decrypted. Can contain letters, digits, and symbols.

    - **shift** (`int`, default=`3`):  
    The number of positions each character was shifted during encryption.

    - **isSymbolsAltered** (`bool`, default=`False`):  
    If `True`, non-alphanumeric symbols will also be shifted back by the specified amount. If `False`, symbols remain unchanged.

    - **isNumbersAltered** (`bool`, default=`False`):  
    If `True`, digits (`0-9`) will be shifted back by the specified amount, wrapping around after `0`. If `False`, digits remain unchanged.

    ## <ins>*Methods*</ins>

    ### `decrypt() -> str`
    > Decrypts the input text by reversing the Caesar cipher algorithm and the specified options.

    #### <ins>Returns</ins>
    - **`str`**: The decrypted version of the input text.

    #### <ins>*Algorithm Details*</ins>
    
    - **Lowercase letters** (`a-z`): Shifted backward within the lowercase alphabet, wrapping around after `a`.
    - **Uppercase letters** (`A-Z`): Shifted backward within the uppercase alphabet, wrapping around after `A`.
    - **Digits** (`0-9`): If `isNumbersAltered` is `True`, shifted backward within the digit range, wrapping after `0`.
    - **Symbols**: If `isSymbolsAltered` is `True`, shifted backward by the specified amount using ASCII values.
    - **Other characters**: Remain unchanged unless symbol shifting is enabled.

    ## <ins>*Example Usage*</ins>

    ```python
    # Basic decryption of text
    Decryption_cls_obj = Decryption("Khoor", shift = 3, isNumbersAltered = True, isSymbolsAltered = True)
    Decrypted_text = Decryption_cls_obj.decrypt()
    print(Decrypted_text)

    # Decrypt only letters, leave digits and symbols unchanged
    Decryption_cls_obj = Decryption("Ugetgv123!", shift=2)
    print(Decryption_cls_obj.decrypt())
    ```

    ## <ins>*Notes*</ins>
    
    - ***Use the same shift value and options as were used for encryption to ensure correct decryption.***
    - ***emoji were also supported but use with caution.***
    
    ## <ins>*Limitations*</ins>
    
    - it is vulnerable to brute-force and frequency analysis attacks.
    - Only basic ASCII characters are supported for shifting; Unicode and special character support is limited.

    ### Developed by [ViratiAkiraNandhanReddy](https://github.com/ViratiAkiraNandhanReddy)
    '''

    def __init__(self, text: str = '', shift = 3, isSymbolsAltered = False, isNumbersAltered = False):
        
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        if not isinstance(shift, int):
            raise TypeError("shift must be an integer")
        if not isinstance(isSymbolsAltered, bool):
            raise TypeError("isSymbolsAltered must be a boolean")
        if not isinstance(isNumbersAltered, bool):
            raise TypeError("isNumbersAltered must be a boolean")
        
        if shift < 0:
            raise ValueError("shift must be a non-negative integer")

        self.text = text
        self.shift = shift
        self.isSymbolsAltered = isSymbolsAltered
        self.isNumbersAltered = isNumbersAltered

    def decrypt(self)-> str:

        '''***Decrypts the input text using the Caesar cipher algorithm and returns the decrypted text.***'''

        DecryptedText: list[str] = []

        for char in self.text:

            if char.isalpha() and char.islower() :
                # Decrypt lowercase letters
                DecryptedText.append(chr((ord(char) - LOWERCASEASCII - self.shift) % 26 + LOWERCASEASCII))
            
            elif char.isalpha() and char.isupper():
                # Decrypt uppercase letters
                DecryptedText.append(chr((ord(char) - UPPERCASEASCII - self.shift) % 26 + UPPERCASEASCII))
            
            elif char.isdigit() and self.isNumbersAltered:
                # Decrypt digits
                DecryptedText.append(chr((ord(char) - DIGITASCII - self.shift) % 10 + DIGITASCII))
            
            elif not char.isalnum() and self.isSymbolsAltered:
                # Decrypt symbols
                try: DecryptedText.append(chr(ord(char) - self.shift))
                except ValueError as e: raise ValueError('either the shift is too high or the character is unsupported') from e
            
            else:
                # Non-alphabetic characters remain unchanged
                DecryptedText.append(char)

        return ''.join(DecryptedText)
    
    def decrypt_file(self, _filePath: str) -> bool:
        """
        # decrypt_file

        > Decrypt the contents of a file in-place using this instance's
        `decrypt()` method.

        ## <ins>*Purpose*</ins>
        - Read the file at `_filePath`, replace its contents with the
          decrypted text produced by `self.decrypt()`, and return a
          boolean indicating success.

        ## <ins>*Parameters*</ins>
        - `_filePath` (`str`): Path to the file to be decrypted. The file is
          opened in text mode using the environment's default encoding.

        ## <ins>*Returns*</ins>
        - `bool`: `True` when the file was successfully overwritten with the
          decrypted content. Returns `False` when the file cannot be found or
          when permission is denied.

        ## <ins>*Notes*</ins>
        - This performs an in-place overwrite of the file.
        - `FileNotFoundError` and `PermissionError` are caught and result in
          a `False` return value; other exceptions will propagate.

        ## <ins>*Example*<ins>
        ```python
        dec = Decryption('', shift = 4)
        success = dec.decrypt_file('message.txt')
        if success:
            print('File decrypted')
        else:
            print('Failed to decrypt file')
        ```
        """

        try:
            with open(_filePath, 'r', encoding='utf-8') as read:
                self.text = read.read()
            with open(_filePath, 'w', encoding='utf-8') as write:
                write.write(self.decrypt())
            return True
        except (FileNotFoundError, PermissionError):
            return False