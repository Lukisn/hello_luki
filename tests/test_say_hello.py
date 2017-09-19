#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from hello_luki.say_hello import say_hello
# TODO: mock sys.stdout.write to test output


class TestSayHello(unittest.TestCase):

    def test_default(self):
        self.assertIsNone(say_hello())

    def test_other_name(self):
        self.assertIsNone(say_hello(name="Zacharias"))


if __name__ == "__main__":
    unittest.main()
