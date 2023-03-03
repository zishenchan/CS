# credit main about recurion and array
'''
Definition for functions: foo(), fighters()
'''

x = "foo"
y = "fighters"

def fighters(a, b):
    x = 1
    y = 2
    result = (a+x) * (b-y)
    return result

def foo(a, b):
    a = a * 2
    b = a * 2
    print(f"{x}{y}")
    return fighters(a, b)

def main():
    x = 10
    y = 20
    result = foo(x, y)
    print(result, fighters(x, y))

if __name__ == "__main__":
    main()