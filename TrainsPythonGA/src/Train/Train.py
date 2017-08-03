

# Class that contains all the logic and methods related to the train
# stations and distances between them needed for the application
class Train:
    train_graph = {}

    def __init__(self):
        pass

    # Method to initialize the graph of stations and distances between them
    def assign_graph(self, train_graph):
        self.train_graph = train_graph

    # Method to calculate the distance of a given secuence of stations
    def calculate_distance(self, route):
        total = 0
        for i in range(0, len(route)-1):
            origin = route[i]
            destiny = route[i+1]
            modified = False
            for path, val in self.train_graph.iteritems():
                if origin+destiny == path:
                    total += int(val)
                    modified = True
            if not modified:
                return 'NO SUCH ROUTE'
        return total

    # Method to calculate the number of different paths to go from a station to another one
    def calculate_strips(self, strip, maximum_stops=0, exact_stops=0):
        total = 0
        results = []
        curr_stops = 2
        resulting_paths = []
        curr_paths = self.train_graph.keys()
        destinies = self.train_graph.keys()
        while curr_stops <= maximum_stops:
            for destiny1 in curr_paths:
                if (curr_stops > 1) or (curr_stops == 1 and destiny1[0][0] == strip[0]):
                    for destiny2 in destinies:
                        if destiny1[-1] == destiny2[0]:
                            if destiny1[0] == strip[0] and \
                               destiny2[-1] == strip[1] and \
                               (exact_stops == 'N' or curr_stops == maximum_stops):
                                total += 1
                                resulting_paths.append(destiny1 + destiny2[-1])
                            else:
                                results.append(destiny1 + destiny2[-1])
            curr_paths = results
            results = []
            curr_stops += 1
        return total

    # Method to calculate the minimum number of stops needed to go from a station to another one
    def calculate_shortest_route(self, strip):
        results = []
        curr_stops = 1
        resulting_paths = []
        curr_paths = self.train_graph.keys()
        destinies = self.train_graph.keys()
        iteration = 0
        while curr_stops < 9:
            for ind1, destiny1 in enumerate(curr_paths):
                if (iteration > 0) or (iteration == 0 and destiny1[0][0] == strip[0]):
                    for ind2, destiny2 in enumerate(destinies):
                        if not ind1 == ind2:
                            if destiny1[-1] == destiny2[0]:
                                if destiny1[0] == strip[0] and destiny2[-1] == strip[1]:
                                    resulting_paths.append(destiny1 + destiny2[-1])
                                else:
                                    results.append(destiny1 + destiny2[-1])
            curr_paths = results
            results = []
            curr_stops += 1
            iteration += 1
        min_dist = 999999
        for path in resulting_paths:
            path_dist = self.calculate_distance(path)
            if path_dist < min_dist:
                min_dist = path_dist
        return min_dist

    # Method to calculate the number of different routes that can be travelled from a station to another one
    # in less than a maximum distance
    def routes_in_distance(self, strip, distance):
        results = {}
        resulting_paths = {}
        curr_paths = self.train_graph
        destinies = self.train_graph
        iteration = 0
        prev_paths = ''
        while True:
            for ind1, destiny1 in enumerate(curr_paths.iteritems()):
                if (iteration > 0) or (iteration == 0 and destiny1[0][0] == strip[0]):
                    for ind2, destiny2 in enumerate(destinies.iteritems()):
                        if not ind1 == ind2:
                            if destiny1[0][-1] == destiny2[0][0]:
                                curr_distance = resulting_paths.get(destiny1[0], self.calculate_distance(destiny1[0]))
                                added_distance = destiny2[1]
                                total_distance = curr_distance + added_distance
                                if total_distance < distance:
                                    if destiny1[0][0] == strip[0] and destiny2[0][-1] == strip[1]:
                                        resulting_paths[destiny1[0] + destiny2[0][-1]] = total_distance
                                    results[destiny1[0] + destiny2[0][-1]] = total_distance
            curr_paths = results
            results = {}
            iteration += 1
            if prev_paths == results:
                break
            prev_paths = results
        return len(resulting_paths)
