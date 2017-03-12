""" File name:   dfa.py
Author:      Kuangyi Xing  u5817313
Date:        2017/03/06
Description: This file defines a function which reads in
a DFA described in a file and builds an appropriate datastructure.

There is also another function which takes this DFA and a word
and returns if the word is accepted by the DFA.

It should be implemented for Exercise 3 of Assignment 0.

See the assignment notes for a description of its contents.
"""


def load_dfa(dfa_file_name):
    """ This function reads the DFA in the specified file and returns a
    data structure representing it. It is up to you to choose an appropriate
    data structure. The returned DFA will be used by your accepts_word
    function. Consider using a tuple to hold the parts of your DFA, one of which
    might be a dictionary containing the edges.

    We suggest that you return a tuple containing the names of the start
    and accepting states, and a dictionary which represents the edges in
    the DFA.

    (str) -> Object
    """

    dfa_file = open(dfa_file_name, "r")
    dfa_tup = ()
    edge_dictionary = {}

    for line in dfa_file:
        if "initial" in line:
            words = line.split()
            initial_state = words[1]
            dfa_tup += (initial_state,)

        elif "accepting" in line:
            words = line.split()
            accepting_state = words[1:]
            dfa_tup += (accepting_state,)

        elif "transition" in line:
            words = line.split()
            resource_state = words[1]
            destination_state = words[2]
            edge = words[3]
            edge_dictionary[(resource_state, edge)] = destination_state

    dfa_tup += (edge_dictionary,)
    return dfa_tup



def accepts_word(dfa, word):
    """ This function takes in a DFA (that is produced by your load_dfa function)
                and then returns True if the DFA accepts the given word, and False
                otherwise.

                (Object, str) -> bool
    """
    state = dfa[0]
    edge_dictionary = dfa[2]
    for index in range(len(word)) :
        if edge_dictionary.has_key((state,word[index])) :
            state = edge_dictionary[(state, word[index])]
            if index == len(word) - 1 :
                if state in dfa[1] :
                    return True
                else :
                    return False
        else :
            return False


