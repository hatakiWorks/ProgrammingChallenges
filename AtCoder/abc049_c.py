import sys
from io import StringIO
import unittest

import sys
sys.setrecursionlimit(10**6)

words = {'dream', 'dreamer', 'erase', 'eraser'}

def check_daydream(s, t_pos):
    if len(s) == t_pos:
        return True
    if len(s) > t_pos:
        for w in words:
            if w == s[t_pos : t_pos + len(w)]:
                if check_daydream(s,t_pos + len(w)) == True:
                    return True
    return False

def resolve():
    s = input()

    if check_daydream(s,0) == True:
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
