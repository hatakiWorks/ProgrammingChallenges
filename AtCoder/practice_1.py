import sys
from io import StringIO
import unittest

def resolve():
    # -*- coding: utf-8 -*-
    # 整数の入力
    a = int(input())
    # スペース区切りの整数の入力
    b, c = map(int, input().split())
    # 文字列の入力
    s = input()
    # 出力
    print("{} {}".format(a+b+c, s))

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
        input = """1
2 3
test"""
        output = """6 test"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """72
128 256
myonmyon"""
        output = """456 myonmyon"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
