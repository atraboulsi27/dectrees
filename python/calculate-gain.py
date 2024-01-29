from dtree import averageGain
from monkdata import monk1,monk2,monk3,attributes

for dataset in [{"n": "monk1", "d":monk1},
    {"n": "monk2", "d":monk2},
    {"n": "monk3", "d":monk3}]:
    for attrib in attributes:
        print(f"The information gain in {dataset['n']} by {attrib.name} is: {averageGain(dataset['d'],attrib)}")