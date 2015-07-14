__author__ = 'danidee'

import sys
from itertools import zip_longest
import graphviz as gv
from paths import *
from level import *
from graph import *


def main():
    app = QtGui.QApplication(sys.argv)

    activity = criticalPath()
    activity.get_num_act()
    activity.show()
    sys.exit(app.exec_())

    '''*********************All the calculations for the resource levelling class*******************'''

    levelit = level()
    levelit.level_est(all_objects)
    all_objects = levelit.level_lst(all_objects)

    #list comprehension to add all the values in the est and lst of the objects
    result = [[sum(j) for j in zip_longest(*i, fillvalue=0)] for i in zip_longest(*[activity.level for activity in all_objects], fillvalue=[0])]

    for i in result:
        print(i)

    total = [[sum(j)] for j in [i for i in result]]

    print(total)

    [print('The efficiency {0:.1f} percent'.format(b/a * 100)) for a, b in zip_longest(*total)]

if __name__ == '__main__': main()
