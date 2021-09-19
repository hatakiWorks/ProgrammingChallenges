import sys
from io import StringIO
import unittest

def distance(prelist, postlist):
    return int(postlist[1]) - int(prelist[1]) + int(postlist[2]) - int(prelist[2])

def check_root(prelist, postlist):
    time = int(postlist[0]) - int(prelist[0])
    if distance(prelist, postlist) > time:
        return False
    if (distance(prelist, postlist) - time) % 2 == 0:
        return True
    else:
        return False

def resolve():
    n = int(input())  # nは入力回数
    pos_list = [['0','0','0']]
    for i in range(n):
        pos_list.append(list(input().split()))
    
    result = False
    for i in range(n-1):
        result = check_root(pos_list[i],pos_list[i+1])
        if result == False:
            break
    
    if result:
        print('Yes')
    else:
        print('No')

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
3 1 2
6 1 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
2 100 100"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
5 1 1
100 1 1"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
