import sys
from io import StringIO
import unittest

def sumdigit(i):
    sum = 0;
    while i != 0:
        sum += i % 10
        i = int(i / 10)
    return sum

def resolve():
    n, a, b = map(int, input().split())
    sum = 0
    for i in range(n+1):
        if a <= sumdigit(i) and sumdigit(i) <= b:
            sum += i
    
    print(sum)


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
        input = """20 2 5"""
        output = """84"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 1 2"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 4 16"""
        output = """4554"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
