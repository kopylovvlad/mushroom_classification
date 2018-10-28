from typing import List, Any, Dict, Tuple, Union


class BiCluster:
    def __init__(self, vec, left=None, right=None, distance=0.0, id=None) -> None:
        self.left = left
        self.right = right
        self.vec = vec
        self.id = id
        self.distance = distance


def prepare_vector(
    vector_data: Tuple[List[str], Dict[str, List[int]]]
) -> Tuple[List[str], List[str], List[List[float]]]:
    vector_head: List[str]
    vector_body: Dict[str, List[int]]
    vector_head, vector_body = vector_data
    rownames: List[str] = list(vector_body.keys())
    data: List[List[float]] = []
    for i_list in vector_body.values():
        arr: List[float] = []
        for i in i_list:
            arr.append(float(i))
        data.append(arr)

    return (rownames, vector_head, data)


def tanimoto_coeff(
        data1: List[int],
        data2: List[int]
) -> float:
    '''
    returns 0 if lists are equal
    returns >0 and <1 if lists are not equal
    '''
    if len(data1) != len(data2):
        raise BaseException('Data length are not equal')

    A: float = 0
    B: float = 0
    C: float = 0

    for i in range(len(data1)):
        A += (data1[i] * data2[i])
        B += pow(data1[i], 2)
        C += pow(data2[i], 2)

    if (B + C - A) != 0:
        result: float = (A / (B + C - A))
        return 1 - result
    else:
        return 1.0


def hcluster(rows, distance=tanimoto_coeff):
    # https://en.wikipedia.org/wiki/Hierarchical_clustering
    distances = {}
    currentclustid = -1
    clust = [BiCluster(rows[i], id=i) for i in range(len(rows))]

    while len(clust) > 1:
        lowestpair = (0, 1)
        closest: float = distance(clust[0].vec, clust[1].vec)
        for i in range(len(clust)):
            for j in range(i+1, len(clust)):
                if (clust[i].id, clust[j].id) not in distances:
                    distances[(clust[i].id, clust[j].id)] = distance(
                        clust[i].vec, clust[j].vec)

                d: float = distances[(clust[i].id, clust[j].id)]
            if d < closest:
                closest = d
                lowestpair = (i, j)

        # calculate average for two items
        mergevec = [
            (clust[lowestpair[0]].vec[i]+clust[lowestpair[1]].vec[i])/2.0
            for i in range(len(clust[0].vec))]

        # create new cluster
        newcluster = BiCluster(mergevec, left=clust[lowestpair[0]],
                               right=clust[lowestpair[1]],
                               distance=closest, id=currentclustid)
        currentclustid -= 1
        del clust[lowestpair[1]]
        del clust[lowestpair[0]]
        clust.append(newcluster)

    return clust[0]


def get_three_closest_names(
    test_row: List[int],
    know_item_names: List[str],
    know_data: List[List[int]],
    distance=tanimoto_coeff
) -> List[str]:
    three_closest_names: List[str] = []
    distance_dict: Dict[int, float] = {}

    # calculate distance for each
    for i in range(len(know_data)):
        know_d: List[int] = know_data[i]
        distance_dict[i] = distance(test_row, know_d)

    # min value in top
    distance_arr: List[List[Union[float, int]]] = []
    for i in distance_dict:
        distance_arr.append([
            distance_dict[i],
            i
        ])
    del distance_dict
    for i in sorted(distance_arr)[:3]:
        three_closest_names.append(know_item_names[i[1]])
    return three_closest_names


def clust_to_string(clust, labels=None, n: int=0) -> str:
    '''print to console'''

    s: str = ''
    for _i in range(n):
        s = s + ' '

    if clust.id < 0:
        s = s + "-\n"
    else:
        if labels == None:
            s = s + str(clust.id) + "\n"
        else:
            s = s + str(labels[clust.id]) + "\n"

    if clust.left != None:
        s = s + clust_to_string(clust.left, labels=labels, n=n+1)
    if clust.right != None:
        s = s + clust_to_string(clust.right, labels=labels, n=n+1)
    return s
