from dtree import allPruned,buildTree,check
from monkdata import monk1, attributes, monk1test, monk2, monk2test, monk3, monk3test
import random


def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


fractions = [0.3,0.4,0.5,0.6,0.7,0.8]

def classif_error(dataset):
    for fraction in fractions:
        dataset_train, datast_val = partition(dataset, fraction)
        tr1=buildTree(dataset_train, attributes)
        pruned_trees = allPruned(tr1)
        for pruned in pruned_trees:
            if pruned == pruned_trees[0]:
                continue
            elif pruned == pruned_trees[1]:
                i = 1
                i_best = i
                error = check(pruned, datast_val)
                error_best = error
                index_best = pruned
            else:
                i += 1
                error = check(pruned, datast_val)
                if error <= error_best: #means that this tree is better
                    error_best = error
                    index_best = pruned
                    i_best = i
                    print("now the best desicion tree for monk1 is NO.", i, "which is:", index_best, "with error:", error_best)
        print("finally the best desicion tree for monk1 is NO.", i_best, "which is:", index_best, "with error:", error_best)


classif_error(monk1)

