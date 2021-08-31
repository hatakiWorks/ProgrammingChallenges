import sys
from io import StringIO
import unittest

def resolve():
    # -*- coding: utf-8 -*-
    s = str(input())
    s1,s2,s3 = list(s)
    a = int(s1)
    b = int(s2)
    c = int(s3)
    # 出力
    print(a+b+c)

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """101"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
