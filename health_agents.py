""" File name:   health_agents.py
    Author:      <your name goes here>
    Date:        <the date goes here>
    Description: This file contains agents which fight disease. It is used
                 in Exercise 4 of Assignment 0.
"""

import random
import operator

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
    scenario (add all disease score at each city together). Then choose the move with the lowest disease score (the most effective
    way to avoid the disease spread).


    """

    def choose_move(self, location, valid_moves, disease, threshold, growth, spread):

        """
        choose a optimal location and return the location on the basis of the effect of the move on the following scenario
        """
        # optimal_move = None
        # predicted_disease_scenarios = {}
        # for move in valid_moves :
        #     predicted_diseases = self.simulated_spread_disease(disease,move,growth,threshold,spread)
        #     total_disease = 0.0
        #     for predicted_disease in predicted_diseases :
        #         total_disease += predicted_diseases[predicted_disease]
        #     predicted_disease_scenarios[move] = total_disease
        #
        # print("predicted_disease_scenarios",predicted_disease_scenarios)
        #
        # optimal_move = min(predicted_disease_scenarios,key = predicted_disease_scenarios.get)

        self.threshold = threshold
        self.growth = growth
        self.spread = spread

        optimal_move = None
        predict_diseases_scores = {}
        for move in valid_moves :
            predict_diseases_scores[move] = self.simulated_spread_disease(disease,move)



        optimal_move = min(predict_diseases_scores,key = predict_diseases_scores.get)






      #  disease = predict_diseases_scores[optimal_move]

        #print("move to :",optimal_move,predict_diseases_scores[optimal_move])


        return optimal_move




    def simulated_spread_disease(self,disease,agent_location):

        """
        simulate the scenario , given the agent moves to "agent_location"
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

        print("assumed move:", agent_location, disease_new_round,"disease_score",total_disease)



        return total_disease










