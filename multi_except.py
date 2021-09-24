
my_list = [1, 2, 3]

try:
    print("input indexer : ")
    index = int(input())
    print(my_list[index]/0)
except ZeroDivisionError:
    print("can't divide 0")
except IndexError:
    print("wrong indexer")