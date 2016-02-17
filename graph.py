import graphviz as gv

__author__ = 'danidee'


class DrawGraph:


    """
    This class handles the generation of datatypes(lists) to enable graphviz
    draw the graphs of the activities using activities on nodes
    """

    def __init__(self):
        pass

    @staticmethod
    def generate_paths(unordered):
        """
        This method gets all the paths in the project appends Start and Finish to them and then splits them into
        sublists of graph edges e.g [[A, B, C]] becomes [[[Start, A]], [[A, B]], [[B, C]], [[C, Finish]]]
        they're nested this way because label_graph will append a dictionary containing properties that style the
        directed graph when passed to graphviz, in this method we're still working with pure Activity objects, they've
        not been substitued with their id's
        :param unordered: List of all possible paths in the project
        :return: Nested Sublist of graph edges e.g [[A, B, C]] becomes [[[Start, A]], [[A, B]], [[B, C]], [[C, Finish]]]
        """
        paths = [[activity for activity in path] for path in unordered]

        graph_path = list()
        for b in paths:
            b.insert(0, 'Start')
            b.append('Finish')
            for c in zip(b, b[1:]):
                ind_lists = [list(c)]
                graph_path.append(ind_lists)

        print(graph_path)
        return graph_path

    @staticmethod
    def label_graph(graph_path):
        """
        This method styles the graph by adding a dictionary to each edge in graph_path, this attributes of the
        dictionary tell graphviz how to style our graph
        :param graph_path: nested sublists of edges in the graph
        :return: nested sublists where each activity has been substituted with it's id (so graphviz can draw)
        """
        for a in graph_path:
            a.append({})

            #  if the first element  == Start it will fail to get a duration and throw an AttributeError, if so set the
            #  duration as 0
            try:
                duration = a[0][0].duration
            except AttributeError:
                a[1].update({'label': str(0)})

                #  if the first activity after Start is a critical activity update the graph line to red
                if a[0][1].is_critical:
                    a[1].update({'color': 'red'})
                continue

            duration = int(duration) if duration % 1 == 0.0 else duration
            a[1].update({'label': str(duration)})

            # if the first activity is a critical and the second activity is critical also update the graph line to red
            if a[0][0].is_critical and getattr(a[0][1], 'is_critical', False):
                a[1].update({'color': 'red'})

            #  if the first activity is critical we're at the end of the graph( =='Finish') update the graph line to red
            elif a[0][0].is_critical and a[0][1] == 'Finish':
                a[1].update({'color': 'red'})

        graph_path = [[[b.id if hasattr(b, 'id') else b for b in a[0]], a[1]] for a in graph_path]

        return graph_path

    @staticmethod
    def add_edges(graph, edges):
        """
        Method that loops through the list of edges and adds the edges and their properties to the graph
        :param graph: graphviz graph
        :param edges: Nested sublists of graph edges (represented by their id's not pure Activity objects)
        :return:
        """
        for e in edges:
            if isinstance(e[0], list):
                graph.edge(*e[0], **e[1])
            else:
                graph.edge(*e)
        return graph

    def draw(self, all_paths):
        """
        :param all_paths: all the possible paths in the project
        :return: None
        """

        graph = gv.Digraph(format='png')
        graph._head = 'strict digraph %s{'  # i should not be doing this
        graph.node_attr['shape'] = 'circle'
        graph.graph_attr['rankdir'] = 'LR'
        unlabelled_edges = self.generate_paths(all_paths)
        labelled_edges = self.label_graph(unlabelled_edges)
        print(labelled_edges)
        graphviz_path = self.add_edges(graph, labelled_edges)
        graphviz_path.render('graphs/network_diagram')

if __name__ == '__main__':
    main()
