# add.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    import sys
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(f"The sum of {a} and {b} is {add(a, b)}")
