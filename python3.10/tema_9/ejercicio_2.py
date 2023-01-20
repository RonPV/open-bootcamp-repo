
from functools import reduce

def main():
    numeros = [1,2,3,4,5,6,7,8,9,10]
    lista = list(filter(lambda n: (n%2 !=0), numeros))
    print(reduce(lambda a,b:(a+b),lista))

if __name__ == "__main__":
    main()