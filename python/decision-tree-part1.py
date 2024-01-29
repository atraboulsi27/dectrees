from monkdata import monk1, attributes, monk1test, monk2, monk2test, monk3, monk3test
import dtree as d
from drawtree_qt5 import drawTree

tr1=d.buildTree(monk1, attributes,2)

drawTree(tr1)