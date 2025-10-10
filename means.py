

def mean_arthmetic(lista_ocen):
    sum = 0
    for ocena in lista_ocen:
        print("Suma: ", sum, " ocena ", ocena)
        sum += ocena
    print("Suma: ", sum)
    len(lista_ocen)
    mean = sum / len(lista_ocen)
    print("srednia artmetyczna", mean)
    return mean

def mean_geometric(lista_ocen):
    product = 1
    for ocena in lista_ocen:
        product *= ocena
    mean_geometric = product ** (1 / len(lista_ocen))
    print("mean_geometric", mean_geometric)
    return mean_geometric


def mean_arthmetic2(lista_ocen):
    mean = sum (lista_ocen) / len(lista_ocen)
    print("srednia artmetyczna", mean)
    return mean

if __name__ == "__main__":
    sum4 = mean_arthmetic2([1, 2, 3, ])
    sum5 = mean_arthmetic2([4, 5, 6, ])
    sum6 = mean_arthmetic2([9, 10, 11, ])
    print("sum4, sum5, sum6 ", sum4, sum5, sum6)
    sum1 = mean_arthmetic([1, 2, 3, ])
    sum2 = mean_arthmetic([4, 5, 6, ])
    sum3 = mean_arthmetic([9, 10, 11, ])
    print("sum1, sum2m sum3 ", sum1, sum2, sum3)

    my_tuple = (1, 2, 3)
    print(my_tuple[1])  # -> 2

    my_dict = {"name": "Alice", "age": 25}
    print(my_dict["name"])  # -> Alice

    my_set = {1, 2, 3, 3, 2}
    print(my_set)  # -> {1, 2, 3}

    a = 10  # int
    b = 5.5  # float
    c = True  # bool
    d = "Python"  # str

    print(type(a), type(b), type(c), type(d))

    my_list = [1, 2, 3, "Python"]
    my_list.append(4)
    print(my_list[0])  # -> 1

    lista_ocen = [5, 4.5, 3.5, 6, 2.5, 4, 6, 5.5, 2, 3]
    # sum = 0
    # # sum += lista_ocen [0]
    # # sum += lista_ocen [1]
    # for ocena in lista_ocen:
    #     print ("Suma: ", sum, " ocena ", ocena)
    #     sum += ocena
    # print ("Suma: ", sum )
    # len(lista_ocen)
    # mean = sum/len(lista_ocen)
    # print ("srednia artmetyczna", mean )

    product = 1
    for ocena in lista_ocen:
        product *= ocena
    mean_geometric = product ** (1 / len(lista_ocen))
    print ("mean_geometric", mean_geometric )
