import sys
from io import StringIO
import unittest

def sum(sen, gosen, man):
    return sen * 1000 + gosen * 5000 + man * 10000

def resolve():
    n, y = map(int, input().split())

    s = -1 #千円の枚数
    g = -1 #五千円の枚数
    finish = False
    i = 0
    while i <= n and finish == False:
        j = 0
        while j <= n and finish == False:
            if i < 0 or j < 0 or n - i - j < 0:
                break;
            if sum(i, j, n - i - j) == y:
                finish = True
                s = i
                g = j
                break;
            j += 1
        i += 1
    
    if finish == True:
        print(n-s-g, g, s)
    else:
        print(-1, -1, -1)

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
        input = """9 45000"""
        output = """4 0 5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 196000"""
        output = """-1 -1 -1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000 1234000"""
        output = """14 27 959"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2000 20000000"""
        output = """2000 0 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
