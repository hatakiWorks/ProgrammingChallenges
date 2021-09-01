import sys
from io import StringIO
import unittest

def resolve():
    # -*- coding: utf-8 -*-
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    alice = 0
    bob = 0
    for i, t in enumerate(a):
        if i % 2 == 0:
            alice += a[i]
        else:
            bob += a[i]
    print(alice - bob)

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
        input = """2
3 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
2 7 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
20 18 2 18"""
        output = """18"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
