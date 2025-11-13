import unittest
import os
import tempfile
from CaesarCipher import Encryption, Decryption

class TestFileIO(unittest.TestCase):

    def test_encrypt_file_success(self):
        original = "Hello, File IO! 123"
        # create temp file
        with tempfile.TemporaryDirectory() as td:
            fp = os.path.join(td, 'msg.txt')
            with open(fp, 'w', encoding = 'utf-8') as f:
                f.write(original)

            # run encryption in-place
            enc = Encryption(shift = 3, alterNumbers = True, alterSymbols = False)
            ok = enc.encrypt_file(fp)
            self.assertTrue(ok)

            # expected result computed separately
            expected = Encryption(original, shift = 3, alterNumbers = True, alterSymbols = False).encrypt()
            with open(fp, 'r', encoding = 'utf-8') as f:
                content = f.read()
            self.assertEqual(content, expected)

    def test_decrypt_file_success(self):
        original = "Secret file content! 456"
        with tempfile.TemporaryDirectory() as td:
            fp = os.path.join(td, 'data.txt')
            # write encrypted content first
            encrypted = Encryption(original, shift = 4, alterNumbers = True, alterSymbols = False).encrypt()
            with open(fp, 'w', encoding = 'utf-8') as f:
                f.write(encrypted)

            dec = Decryption(shift = 4, isNumbersAltered = True, isSymbolsAltered = False)
            ok = dec.decrypt_file(fp)
            self.assertTrue(ok)

            with open(fp, 'r', encoding = 'utf-8') as f:
                content = f.read()
            self.assertEqual(content, original)

    def test_encrypt_file_nonexistent(self):
        enc = Encryption(shift = 2)
        # use a path that does not exist (temporary dir removed)
        td = tempfile.mkdtemp()
        fp = os.path.join(td, 'no_file.txt')
        # remove directory to ensure file can't be found
        os.rmdir(td)
        self.assertFalse(enc.encrypt_file(fp))

    def test_decrypt_file_nonexistent(self):
        dec = Decryption(shift = 2)
        td = tempfile.mkdtemp()
        fp = os.path.join(td, 'no_file.txt')
        os.rmdir(td)
        self.assertFalse(dec.decrypt_file(fp))


if __name__ == '__main__':
    unittest.main()