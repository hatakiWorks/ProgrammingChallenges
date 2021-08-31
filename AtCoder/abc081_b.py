import sys
from io import StringIO
import unittest

def resolve():
    # -*- coding: utf-8 -*-
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    even = True
    while True:
        for i, t in enumerate(a):
            if t % 2 == 1:
                even = False
                break
            else:
                a[i] = t / 2

        if even == False:
            break
        count += 1
    
    print(count)


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
        input = """3
8 12 40"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
5 6 8 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
382253568 723152896 37802240 379425024 404894720 471526144"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
