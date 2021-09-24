
my_list = [1, 2, 3]

try:
    print("input indexer: ")
    index = int(input())
    print(my_list[index]/0)

except ZeroDivisionError as err:
    print("can't divide 0. ({})".format(err))
except IndexError as err:
    print("wrong indexer. ({})".format(err))