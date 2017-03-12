""" File name:   disease_scenario.py
    Author:      Kuangyi Xing u5817313
    Date:        2017/03/08
    Description: This file represents a scenario simulating the spread of an
                 infectious disease around Australia. It should be 
                 implemented for Part 1 of Exercise 4 of Assignment 0.
                 
                 See the lab notes for a description of its contents.
"""

class DiseaseScenario :
    def read_scenario_file(self, scenario_file_name):
        """
        read a scenario from the given file and store the relevant information
        (DiseaseScenario, str) -> bool
        """
        try :
            scenario_file = open(scenario_file_name,"r")
        except IOError :
            return False



        self.locations = []
        self.disease = {}
        self.conn = {}

        for line in scenario_file:
            if "threshold" in line:
                words = line.split()
                self.threshold = float(words[1])
            elif "growth" in line:
                words = line.split()
                self.growth = float(words[1])
            elif "spread" in line:
                words = line.split()
                self.spread = float(words[1])
            elif "location" in line:
                words = line.split()
                self.locations.append(words[1])
            elif "start" in line:
                words = line.split()
                self.location = words[1]
            elif "disease" in line:
                words = line.split()
                self.disease[words[1]] = float(words[2])

        for location in self.locations:
            if location not in self.disease:
                self.disease[location] = 0.0

        for location in self.locations:
            self.conn[location] = set([])



        scenario_file = open(scenario_file_name, "r")


        for line in scenario_file:
            words = line.split()
            if "conn" in line:
                self.conn[words[1]].add(words[2])
                self.conn[words[2]].add(words[1])


        scenario_file.close()

        return True


    def valid_moves(self):
        """
        This method should return a list of valid moves.
        Each valid move is either a neighbouring location or the current location of the agent (which indicates that the agent stays put).
        (DiseaseScenario) -> [str]

        """
        valid_moves_locations = self.conn[self.location].copy()

        valid_moves_locations.add(self.location)

        return list(valid_moves_locations)

    def move(self, loc):
        """
        move the agent to the specified location and clear the disease there
        (DiseaseScenario, str) -> None
        """


        if loc not in self.valid_moves():
            raise ValueError("{} is not a valid location".format(loc))
        else:
            self.disease[loc] = 0.0
            self.location = loc

    def spread_disease(self):
        """
         This method should spread the disease according the threshold, growth, spread, and connections between locations.
         Disease only spreads to adjacent locations if the spreading location has greater than or equal to the threshold level of disease.
         Disease will not spread to a location where the agent is.
         (DiseaseScenario) -> None
        """
        disease_new_round = self.disease.copy()

        for loc in self.locations:
            d = self.disease[loc]
            additional_disease = d * self.growth
            disease_new_round[loc] += additional_disease

            if d > self.threshold or d == self.threshold :
                contribution_to_neighbours = d * self.spread


                for neighbour in self.conn[loc]:

                    if self.location != neighbour:
                        disease_new_round[neighbour] = disease_new_round[neighbour] + contribution_to_neighbours




        self.disease = disease_new_round

