import unittest
from CaesarCipher import Encryption

class TestEncryption(unittest.TestCase):

    def test_encrypt_basic(self):
        encryption = Encryption("ViratiAkiraNandhanReddy", shift = 3, alterNumbers = False, alterSymbols = False)
        self.assertEqual(encryption.encrypt(), "YludwlDnludQdqgkdqUhggb")
    
    def test_encrypt_no_shift(self):
        encryption = Encryption("Hello, ViratiAkiraNandhanReddy", shift = 0, alterNumbers = False, alterSymbols = False)
        self.assertEqual(encryption.encrypt(), "Hello, ViratiAkiraNandhanReddy")
    
    def test_encrypt_symbols(self):
        encryption = Encryption("Hey! There this message is for testing purpose", shift = 3, alterNumbers = False, alterSymbols = True)
        self.assertEqual(encryption.encrypt(), "Khb$#Wkhuh#wklv#phvvdjh#lv#iru#whvwlqj#sxusrvh")
    
    def test_encrypt_numbers(self):
        encryption = Encryption("This type of encryption will not encrypt symbols, 1234567890", shift = 3, alterNumbers = True, alterSymbols = False)
        self.assertEqual(encryption.encrypt(), "Wklv wbsh ri hqfubswlrq zloo qrw hqfubsw vbperov, 4567890123")

    def test_encrypt_all(self):
        encryption = Encryption("This type of encryption will encrypt everything like string numbers and symbols, But using symbol shifting may produce highly inappropriate messages", shift = 3, alterNumbers = True, alterSymbols = True)
        self.assertEqual(encryption.encrypt(), "Wklv#wbsh#ri#hqfubswlrq#zloo#hqfubsw#hyhubwklqj#olnh#vwulqj#qxpehuv#dqg#vbperov/#Exw#xvlqj#vbpero#vkliwlqj#pdb#surgxfh#kljkob#lqdssursuldwh#phvvdjhv")

    def test_encrypt_different_shift(self):
        encryption = Encryption("This type of encryption will encrypt everything like string numbers and symbols, But using symbol shifting may produce highly inappropriate messages", shift = 8, alterNumbers = True, alterSymbols = True)
        self.assertEqual(encryption.encrypt(), "Bpqa(bgxm(wn(mvkzgxbqwv(eqtt(mvkzgxb(mdmzgbpqvo(tqsm(abzqvo(vcujmza(ivl(agujwta4(Jcb(caqvo(agujwt(apqnbqvo(uig(xzwlckm(pqoptg(qvixxzwxzqibm(umaaioma")
    
if __name__ == '__main__':
    unittest.main()