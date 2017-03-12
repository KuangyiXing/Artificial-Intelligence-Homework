""" File name:   health_agents.py
    Author:      Kuangyi Xing u5817313
    Date:        2017/03/09
    Description: This file contains agents which fight disease. It is used
                 in Exercise 4 of Assignment 0.
"""

import random

class HealthAgent(object):
    """ A simple disease fighting agent. """
    
    def __init__(self, locations, conn):
        """ This contructor does nothing except save the locations and conn.
            Feel free to overwrite it when you extend this class if you want
            to do some initial computation.
            
            (HealthAgent, [str], { str : set([str]) }) -> None
        """
        self.locations = locations
        self.conn = conn

    def choose_move(self, location, valid_moves, disease, threshold, growth, spread):
        """ Using given information, return a valid move from valid_moves.
            Returning an inalid move will cause the system to stop.
            
            Changing any of the mutable parameters will have no effect on the operation
            of the system.
            
            This agent will locally move to the highest disease, of there is
            is no nearby disease, it will act randomly.
            
            (HealthAgent, str, [str], [str], { str : float }, float, float, float) -> str  
        """
        max_disease = None
        max_move = None
        for move in valid_moves:
           if max_disease is None or disease[move] > max_disease:
               max_disease = disease[move]
               max_move = move
        
        if not max_disease:
            return random.choice(valid_moves)
        
        return max_move
        
#Make a new agent here called SmartHealthAgent, which extends HealthAgent and acts a bit more sensibly
class SmartHealthAgent(HealthAgent) :
    """
    The solution is : assume the agent moves to a location in the list of valid moves and see the effect on the disease
    scenario (add all disease score at each city together). Then choose the move with the lowest disease score (the most     effective
    way to avoid the disease spread).
    """

    def choose_move(self, location, valid_moves, disease, threshold, growth, spread):

        """
        choose a optimal location and return the location on the basis of the effect of the move on the following scenario
        """

        """
        Get the effect of all valid move (i.e. the total disease score after a assumed move)
        stored in a dictionary : predicted_disease_scores {assumed_valid_move: the total disease score after this vald move}
        """
        self.threshold = threshold
        self.growth = growth
        self.spread = spread

        predict_diseases_scores = {}
        for move in valid_moves :
                 predict_diseases_scores[move] = self.simulated_spread_disease(disease,move)



        """
        When there are multiple minimum disease score existing (i.e. whenever the agent moves to any of those locations, the effect on the disease is the same), move the agent to large city (i.e. city with the most connection)




        """
        minimum_value = min(predict_diseases_scores.values())
        minimum_keys = [k for k in predict_diseases_scores if predict_diseases_scores[k] == minimum_value]

        connection_numbers = {}
        for loc in minimum_keys :
            connection_numbers[loc] = len(self.conn[loc])

        optimal_move = max(connection_numbers,key = connection_numbers.get)


        return optimal_move




    def simulated_spread_disease(self,disease,agent_location):

        """
        simulate the scenario , given the agent moves to "agent_location"
        input "agent_location", return the toal disease score when the agent is moved to "agent_location"

        (dictionary,str) -> float
        """
        disease_new_round = disease.copy()
        disease_new_round[agent_location] = 0.0
        total_disease = 0.0



        for location in self.locations:
                d = disease[location]

                if location == agent_location :
                    d = 0.0

                additional_disease = d * self.growth
                disease_new_round[location] += additional_disease

                if d > self.threshold or d == self.threshold:
                    contribution_to_neighbours = d * self.spread

                    for neighbour in self.conn[location]:
                        if agent_location != neighbour:
                            disease_new_round[neighbour] = disease_new_round[neighbour] + contribution_to_neighbours



        for location in disease_new_round :
            total_disease += disease_new_round[location]

        return total_disease










