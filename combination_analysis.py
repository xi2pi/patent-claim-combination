# -*- coding: utf-8 -*-
"""
@author: Christian Winkler
"""


def num_combinations(claim_):
    num_com_list = [0] * len(claim_)
    num_com_list[0] = 1
    
    num_com_list_idx = 0
    for i in claim_:
        if num_com_list_idx > 0:
            for j in i:
                num_com_list[num_com_list_idx] += num_com_list[j-1]
        num_com_list_idx += 1
            
    return num_com_list



### NUMBER OF COMBINATION
claim = [[1], [1], [1,2], [1], [2], [1,2,3,4,5], [2,5], [3,4]]
result = num_combinations(claim)
#print(result)
print("Total combinations: " + str(sum(result)))


