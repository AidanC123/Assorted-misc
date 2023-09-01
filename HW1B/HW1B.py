import urllib
from itertools import combinations
import time
from collections import defaultdict

def main(file_location, support, itemset_size):
    candidate_dct = defaultdict(lambda:0)
    for i in range(itemset_size):
        now = time.time()
        candidate_dct = data_pass(file_location, support, pass_nbr=i+1,candidate_dct=candidate_dct)
    return candidate_dct

def update_candidates(item_lst, candidate_dct, pass_nbr):
    if pass_nbr == 1:
        for item in item_lst:
            candidate_dct[(item,)] += 1
    else:
        frequent_item_set = set()
        for item_tuple in combinations(sorted(item_lst), pass_nbr - 1):
            if item_tuple in candidate_dct:
                frequent_item_set.update(item_tuple)
        for item_set in combinations(sorted(frequent_item_set), pass_nbr):
            candidate_dct[item_set] += 1
    return candidate_dct

def clear_items(candidate_dct, support, pass_nbr):
    for item_tuple, cnt in candidate_dct.items():
        if cnt < support or len(item_tuple) < pass_nbr:
            del candidate_dct[item_tuple]
    return candidate_dct

def data_pass(file_location, support, pass_nbr, candidate_dct):
    for line in file_location:
        item_lst = line.split(" ")
        candidate_dct = update_candidates(item_lst, candidate_dct, pass_nbr)
    #candidate_dct = clear_items(candidate_dct, support, pass_nbr)
    return candidate_dct

if __name__ == "__main__":
    f = open("browsing.txt", "r")
    file_location = f.read()
    file_location = file_location.split(' ')
    print(file_location)
    support = 200
    itemset_size = 3
    itemsets_dct = main(file_location, support, itemset_size)
    
    i = 0
    for itemset, frequency in itemsets_dct.items():
        print(itemset, frequency)
        i += 1
        if i == 10:
            break
