from itertools import product

def carticianProducts (A, B):
    return list (product (A, B))

if __name__ == '__main__':
    A = set (map (int, input ().split ()))
    B = set (map (int, input ().split ()))
    # print (carticianProducts (A, B))
    for i in carticianProducts (A, B):
        print (i, end=" ")