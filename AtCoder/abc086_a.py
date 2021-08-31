import sys
from io import StringIO
import unittest

def resolve():
    # -*- coding: utf-8 -*-
    # スペース区切りの整数の入力
    a, b = map(int, input().split())
    if a*b % 2 == 1:
        s = "Odd"
    else:
        s = "Even"
    # 出力
    print(s)

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
        input = """3 4"""
        output = """Even"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 21"""
        output = """Odd"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
