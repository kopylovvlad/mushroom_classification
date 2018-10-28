from typing import List, Dict, Tuple


def csv_to_vector(filereader) -> Tuple[List[str], List[str], List[List[int]]]:
    '''
    convert csv-file to typle without first column: (item_names, props, data)
    '''
    item_names: List[str] = []
    props: List[str] = []
    pre_data: List[List[str]] = []
    data: List[List[int]] = []
    i: int = 0
    j: int = 0
    for row in filereader:
        i += 1
        if i == 1:
            props = row
            continue
        title: str = str(i) + '_' + row[0]
        item_names.append(title)
        tmp_data: List[str] = []
        j = 0
        for symbol in row:
            j += 1
            if j == 1:
                # without first col
                continue
            else:
                tmp_data.append(symbol)
        pre_data.append(tmp_data)

    #
    # pre_data to data
    #
    data_dict: List[Dict[str, int]] = []
    i = 0
    for i in range(len(pre_data[0])):
        data_dict.append({})

    i = 0
    for i in range(len(pre_data[0])):
        for j in range(len(pre_data)):
            row = pre_data[j]
            row_symbol: str = row[i]
            h = data_dict[i]
            if not row_symbol in list(h.keys()):
                data_dict[i][row_symbol] = len(list(h.keys())) + 1
    i = 0
    for row in pre_data:
        tmp_data = []
        for i in range(len(row)):
            symbol = row[i]
            tmp_data.append(data_dict[i][symbol])
        data.append(tmp_data)

    return (item_names, props, data)
