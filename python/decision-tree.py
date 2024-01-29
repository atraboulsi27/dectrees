from monkdata import monk1, attributes, monk1test, monk2, monk2test, monk3, monk3test
import dtree as d
from drawtree_qt5 import drawTree

tr1=d.buildTree(monk1, attributes)
tr2=d.buildTree(monk2, attributes)
tr3=d.buildTree(monk3, attributes)
print(drawTree(tr1))

print(f"The correctness of monk1 training {d.check(tr1, monk1)}")
print(f"The correctness of monk1 test {d.check(tr1, monk1test)}")

print(f"The correctness of monk2 training {d.check(tr2, monk2)}")
print(f"The correctness of monk2 test {d.check(tr2, monk2test)}")

print(f"The correctness of monk3 training {d.check(tr3, monk3)}")
print(f"The correctness of monk3 test {d.check(tr3, monk3test)}")