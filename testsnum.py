import unittest;
from num import dec2bin, bin2dec, dec2oct, oct2dec, dec2hex, hex2dec, bin2hex, oct2bin

class test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(dec2bin(11), 1011)
    def test_2(self):
        self.assertEqual(bin2dec("1011"), 11)
    def test_3(self):
        self.assertEqual(dec2oct(11), "0o13")
    def test_4(self):
        self.assertEqual(oct2dec("0o13"), 11)
    def test_5(self):
        self.assertEqual(dec2hex(11), "0xb")
    def test_6(self):
        self.assertEqual(hex2dec("0xb"), 11)
    def test_7(self):
        self.assertEqual(bin2hex("11"), "0x3")
    def test_8(self):
        self.assertEqual(oct2bin("11"), 1001)
if __name__ == '__main__':
    unittest.main();
