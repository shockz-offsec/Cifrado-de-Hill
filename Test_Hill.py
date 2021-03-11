#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from Hill import *


class Test_1_1_KeyGen(unittest.TestCase):

    def test_1(self):
        key = uoc_hill_genkey(2)
        self.assertEqual(len(key), 2)
        self.assertEqual(len(key[0]), 2)
        self.assertLessEqual(np.max(key), 40)
        self.assertGreaterEqual(np.min(key), 0)

    def test_2(self):
        key = uoc_hill_genkey(3)
        self.assertEqual(len(key), 3)
        self.assertEqual(len(key[0]), 3)
        self.assertLessEqual(np.max(key), 40)
        self.assertGreaterEqual(np.min(key), 0)

    def test_3(self):
        key = uoc_hill_genkey(4)
        self.assertEqual(len(key), 4)
        self.assertEqual(len(key[0]), 4)
        self.assertLessEqual(np.max(key), 40)
        self.assertGreaterEqual(np.min(key), 0)

    def test_4(self):
        key = uoc_hill_genkey(5)
        self.assertEqual(len(key), 5)
        self.assertEqual(len(key[0]), 5)
        self.assertLessEqual(np.max(key), 40)
        self.assertGreaterEqual(np.min(key), 0)



class Test_1_2_Cipher(unittest.TestCase):

    def test_1(self):
        key = [[33, 1, 7], [40, 32, 24], [12, 22, 19]]
        plaintext = "SECRET TEXT"
        ciphertext = ":9OB8:OI5,4Y"
        ciphertext_new = uoc_hill_cipher(plaintext, key)
        self.assertEqual(ciphertext_new, ciphertext)

    def test_2(self):
        key = [[13, 17], [10, 16]]
        plaintext = "AB"
        ciphertext = "RQ"
        ciphertext_new = uoc_hill_cipher(plaintext, key)
        self.assertEqual(ciphertext_new, ciphertext)

    def test_3(self):
        key = [[7, 3, 37], [14, 32, 36], [29, 37, 18]]
        plaintext = "AB"
        ciphertext = "8 A"
        ciphertext_new = uoc_hill_cipher(plaintext, key)
        self.assertEqual(ciphertext_new, ciphertext)

    def test_4(self):
        key = [[7, 3, 37], [14, 32, 36], [29, 37, 18]]
        plaintext = "HELLO WORLD"
        ciphertext = "RHQA7 FP19MY"
        ciphertext_new = uoc_hill_cipher(plaintext, key)
        self.assertEqual(ciphertext_new, ciphertext)

    def test_5(self):
        key = [[5, 15, 18, 15, 10], [22, 10, 35, 10, 37], [28, 33, 31, 7, 30], [14, 35, 33, 38, 28], [30, 0, 37, 26, 6]]
        plaintext = "ONE, TWO OR THREE?"
        ciphertext = "VJ03HX,OH?5G7OVE6IID"
        ciphertext_new = uoc_hill_cipher(plaintext, key)
        self.assertEqual(ciphertext_new, ciphertext)

    def test_6(self):
        key = [[13, 17], [10, 16]]
        plaintext = "THIS IS MY SECRET"
        ciphertext = ":PA A.MA5MG6E5C3XZ"
        ciphertext_new = uoc_hill_cipher(plaintext, key)
        self.assertEqual(ciphertext_new, ciphertext)


class Test_1_3_Decipher(unittest.TestCase):

    def test_1(self):
        key = [[33, 1, 7], [40, 32, 24], [12, 22, 19]]
        plaintext = "SECRET TEXT"
        ciphertext = ":9OB8:OI5,4Y"
        plaintext_new = uoc_hill_decipher(ciphertext, key)
        self.assertEqual(plaintext_new, plaintext)

    def test_2(self):
        key = [[13, 17], [10, 16]]
        plaintext = "AB"
        ciphertext = "RQ"
        plaintext_new = uoc_hill_decipher(ciphertext, key)
        self.assertEqual(plaintext_new, plaintext)

    def test_3(self):
        key = [[7, 3, 37], [14, 32, 36], [29, 37, 18]]
        plaintext = "AB"
        ciphertext = "8 A"
        plaintext_new = uoc_hill_decipher(ciphertext, key)
        self.assertEqual(plaintext_new, plaintext)

    def test_4(self):
        key = [[7, 3, 37], [14, 32, 36], [29, 37, 18]]
        plaintext = "HELLO WORLD"
        ciphertext = "RHQA7 FP19MY"
        plaintext_new = uoc_hill_decipher(ciphertext, key)
        self.assertEqual(plaintext_new, plaintext)

    def test_5(self):
        key = [[5, 15, 18, 15, 10], [22, 10, 35, 10, 37], [28, 33, 31, 7, 30], [14, 35, 33, 38, 28], [30, 0, 37, 26, 6]]
        plaintext = "ONE, TWO OR THREE?"
        ciphertext = "VJ03HX,OH?5G7OVE6IID"
        plaintext_new = uoc_hill_decipher(ciphertext, key)
        self.assertEqual(plaintext_new, plaintext)

    def test_6(self):
        key = [[13, 17], [10, 16]]
        plaintext = "THIS IS MY SECRET"
        ciphertext = ":PA A.MA5MG6E5C3XZ"
        plaintext_new = uoc_hill_decipher(ciphertext, key)
        self.assertEqual(plaintext_new, plaintext)




if __name__ == '__main__':

    # create a suite with all tests
    test_classes_to_run = [Test_1_1_KeyGen, Test_1_2_Cipher, Test_1_3_Decipher]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    all_tests_suite = unittest.TestSuite(suites_list)

    # run the test suite with high verbosity
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(all_tests_suite)



