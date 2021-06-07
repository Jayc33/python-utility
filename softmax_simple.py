import numpy as np
from typing import List
from prettytable import PrettyTable

def softmax_all(q_arr: List[float], t: float) -> List[float]:
    '''Calcuates the Softmax probability for all values in a list of q values for a temperature t'''
    sum = 0.0
    for q in q_arr:
        sum += np.exp(q / t)
        
    ret = []
    for q in q_arr:
        ret.append(np.exp(q/t) / sum)
        
    return ret

def softmax_single(q: float, q_arr: List[float], t: float) -> List[float]:
    '''Calcuates the Softmax probability for a single q value using a list of q values and a temperature t. 
    The method does not check if the list contains the single value.'''
    sum = 0.0
    for q in q_arr:
        sum += np.exp(q / t)
        
    return np.exp(q / t) / sum

if __name__ == '__main__':
    
    q_arr = [0.0, 0.2, 0.8, 1.2, 1.4]
    t_arr = [0.04, 0.2, 1.0, 5.0, 25.0]
    
    for t in t_arr:
        header = [f"t"]
        header.extend([f"q{i}: {q}" for i, q in enumerate(q_arr)])
        table = PrettyTable(header)
        probs = softmax_all(q_arr, t)
        row = [t]
        row.extend([round(p, 6) for p in probs])
        table.add_row(row)
        print(table)
        weighted = np.array(q_arr) * np.array(probs)
        print(sum(weighted))
        print("\n")