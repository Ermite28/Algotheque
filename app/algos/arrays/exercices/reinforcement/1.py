import sys
import matplotlib.pyplot as plt


def relationship_list_size(k):
    """A list to explore the relationship between a list's
    length and it's underlying size in python."""
    data = []
    lenData = []
    sizeData = []
    for i in range(k):
        lenData.append(len(data))
        sizeData.append(sys.getsizeof(data))
        data.append(i)

    plt.plot(lenData, sizeData)
    plt.title("Evolution of list size")
    plt.xlabel("Length ")
    plt.ylabel("Size in bytes")
    plt.show()


relationship_list_size(30)
