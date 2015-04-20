'''
Created on Apr 2, 2015

@author: danidee
'''

from copy import deepcopy

class criticalPath:
    
    def __init__(self):
        '''
        Initialize all the variables we're going to use to calculate the critical path
        '''
        self.id = None
        self.pred = tuple()
        self.dur = None
        self.est = None
        self.lst = None
        #list to store all the objects
        self.all_objects = list()
        
    def create_objects(self):
        
        return criticalPath()
    
    def get_properties(self):
        ''' 
        This functions gets all the input from the user and stores the
        activity name a string, the predecessor in a tuple and the duration
        in a string
        '''
        r = criticalPath()
        Object_list = list()
        num_act = int(input('How many activities are in the project:\n'))
        for i in range(num_act):
            name = input('what is the name of the activity {}:\n'.format(i+1))
            activity_object = r.create_objects()
            pred = input('what is the predecessor(s) of the activity:\n')
            pred = tuple(pred.replace(',', ''))
            dur = input('what is the duration of the activity:\n')
            
            #sets the properties of the objects from what was gotten from the user
            activity_object.set_properties(name, pred, dur)
            #****
            Object_list.append(activity_object)
            
            self.all_objects.append(activity_object)
            
            
        
        return Object_list
    
    def set_properties(self, name, predecessor, duration):
        self.id = name
        self.pred = predecessor
        self.dur = duration
        
        
    def get_nodes(self):
        '''
        Iterate through the objects, get the activities without predecessors and returns
        a list of them
        '''
        list_node = list()
        ls = self.get_properties()
        for i in ls:
            for a in i.pred:
                if '0' in a:
                    myls = list()
                    myls.append(i)
                    list_node.append(myls)
        
        return list_node
    
    #returns a list of all activity objects
    def get_obj(self):
        
        return self.all_objects


def main():
    activity = criticalPath()
    all_objects = activity.get_obj()
    starting_nodes = activity.get_nodes()
    
    
    for ind, st_nodes in enumerate(starting_nodes):
        for node in all_objects:
            #pdb.set_trace()
            if st_nodes[-1].id in node.pred:
                starting_nodes[ind].append(deepcopy(node))
    
    for i in starting_nodes:
        for a in i:
            print(a.id, end=',')
        print()
    
        
    
if __name__ == '__main__': main()
