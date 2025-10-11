import unittest
from CaesarCipher import Decryption

class TestDecryption(unittest.TestCase):

    def test_decrypt_basic(self):
        decryption = Decryption("YludwlDnludQdqgkdqUhggb", shift = 3, isNumbersAltered = False, isSymbolsAltered = False)
        self.assertEqual(decryption.decrypt(), "ViratiAkiraNandhanReddy")

    def test_decrypt_no_shift(self):
        decryption = Decryption("Hello, ViratiAkiraNandhanReddy", shift = 0, isNumbersAltered = False, isSymbolsAltered = False)
        self.assertEqual(decryption.decrypt(), "Hello, ViratiAkiraNandhanReddy")

    def test_decrypt_symbols(self):
        decryption = Decryption("Khb$#Wkhuh#wklv#phvvdjh#lv#iru#whvwlqj#sxusrvh", shift=3, isSymbolsAltered=True, isNumbersAltered=True)
        self.assertEqual(decryption.decrypt(), "Hey! There this message is for testing purpose")

    def test_decrypt_numbers(self):
        decryption = Decryption("Wklv wbsh ri hqfubswlrq zloo qrw hqfubsw vbperov, 4567890123", shift = 3, isNumbersAltered = True, isSymbolsAltered = False)
        self.assertEqual(decryption.decrypt(), "This type of encryption will not encrypt symbols, 1234567890")

    def test_decrypt_all(self):
        decryption = Decryption("Wklv#wbsh#ri#hqfubswlrq#zloo#hqfubsw#hyhubwklqj#olnh#vwulqj#qxpehuv#dqg#vbperov/#Exw#xvlqj#vbpero#vkliwlqj#pdb#surgxfh#kljkob#lqdssursuldwh#phvvdjhv", shift = 3, isNumbersAltered = True, isSymbolsAltered = True)
        self.assertEqual(decryption.decrypt(), "This type of encryption will encrypt everything like string numbers and symbols, But using symbol shifting may produce highly inappropriate messages")

    def test_decrypt_different_shift(self):
        decryption = Decryption("Bpqa(bgxm(wn(mvkzgxbqwv(eqtt(mvkzgxb(mdmzgbpqvo(tqsm(abzqvo(vcujmza(ivl(agujwta4(Jcb(caqvo(agujwt(apqnbqvo(uig(xzwlckm(pqoptg(qvixxzwxzqibm(umaaioma", shift = 8, isNumbersAltered = True, isSymbolsAltered = True)
        self.assertEqual(decryption.decrypt(), "This type of encryption will encrypt everything like string numbers and symbols6 But using symbol shifting may produce highly inappropriate messages")


if __name__ == '__main__':
    unittest.main()