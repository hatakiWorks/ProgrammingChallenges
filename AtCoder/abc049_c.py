import sys
from io import StringIO
import unittest

import sys
sys.setrecursionlimit(10**6)

words = {'dream', 'dreamer', 'erase', 'eraser'}

def check_daydream(s, t):
    if s == t:
        return True
    if len(t) == 0 or s.find(t) == 0:
        for w in words:
            if len(s) > len(t):
                if check_daydream(s,t + w) == True:
                    return True
    return False

def resolve():
    s = input()
    t = ''

    if check_daydream(s,t) == True:
        print('YES')
    else:
        print('NO')

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
        input = """erasedream"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """dreameraser"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """dreamerer"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
