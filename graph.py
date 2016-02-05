__author__ = 'danidee'

import graphviz as gv


class draw_graph():
    '''
    This class handles the generation of datatypes(lists) to enable graphviz
    draw the graphs of the activities using activities on nodes
    '''
    def __init__(self):
        pass

    def generate_paths(self, unordered):

        paths = list()
        for i in unordered:
            tmp_list = list()
            for a in i:
                tmp_list.append(a.id)
            paths.append(tmp_list)

        graph_path = list()
        for b in paths:
            b.insert(0, 'Start')
            b.append('Finish')
            for c in zip(b, b[1:]):
                ind_lists = [list(c)]
                graph_path.append(ind_lists)

        print(graph_path)
        return graph_path

    def label_graph(self, graph_path, critical_path, all_activities):
        for a in graph_path:
            a.append({})
            for b in a:
                for act in all_activities:
                    if b[0] == act.id:
                        duration = act.duration
                        duration = int(duration) if duration % 1 == 0.0 else duration
                        a[1].update({'label': str(duration)})
                        break
                    else:
                        if not a[1]:
                            a[1].update({'label': str(0)})
                for c in critical_path:
                    if 'Start' in b:
                        if b[1] == c.id:
                            a[1].update({'color': 'red'})

                    if b[1] == c.id:
                        for d in critical_path:
                            if b[0] == d.id:
                                a[1].update({'color': 'red'})
                                break

                    if 'Finish' in b:
                        if b[0] == c.id:
                            a[1].update({'color': 'red'})
                break

        return graph_path

    def add_edges(self, graph, edges):
        for e in edges:
            if isinstance(e[0], list):
                graph.edge(*e[0], **e[1])
            else:
                graph.edge(*e)
        return graph

    def draw(self, all_activities, all_paths, critical_path):
        '''*******************Drawing the graph of the activities with graphviz**************************'''
        graph = gv.Digraph(format='png')
        graph._head = 'strict digraph %s{'
        graph.node_attr['shape'] = 'circle'
        graph.graph_attr['rankdir'] = 'LR'
        unlabelled_edges = self.generate_paths(all_paths)
        labelled_edges = self.label_graph(unlabelled_edges, critical_path, all_activities)
        print(labelled_edges)
        graphviz_path = self.add_edges(graph, labelled_edges)
        graphviz_path.render('graphs/network_diagram')

if __name__ == '__main__': main()
