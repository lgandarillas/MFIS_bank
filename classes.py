#!/usr/bin/env python3
"""
This module contains the classes used in the fuzzy system.
"""

class FuzzySetsDict(dict):
    """
    Represents a dictionary of fuzzy sets.
    The key is the setid and the value is a FuzzySet object.
    """

    def print_fuzzy_sets_dict(self):
        """Prints the fuzzy sets in the dictionary."""
        for elem in self:
            print("sentido", elem)
            self[elem].print_set()

class FuzzySet:
    """Represents a fuzzy set."""
    var = ""            # Variable of the fuzzy set (ex.: Age)
    label = ""          # Label of the specific fuzzy set (ex.: Young)
    x = []              # List of abscissas, from xmin to xmax, 1 by 1
    y = []              # List of ordinates (float)
    mem_degree = 0      # Membership degree for the current application

    def print_set(self):
        """Prints the fuzzy set."""
        print("var:       ", self.var)
        print("label:     ", self.label)
        print("mem_degree:", self.mem_degree)
        print()

class RuleList(list):
    """Represents a list of rules."""

    def print_rule_list(self):
        """Prints the rules in the list."""
        for elem in self:
            elem.print_rule()

class Rule:
    """Represents a rule."""
    rule_name = ""      # Name of the rule (str)
    antecedent = []     # List of setids
    consequent = ""     # Just one setid
    strength = 0        # Float
    consequent_x = []   # Output fuzzySet, abscissas
    consequent_y = []   # Output fuzzySet, ordinates

    def print_rule(self):
        """Prints the rule."""
        print("rule_name:", self.rule_name)
        print("IF       ", self.antecedent)
        print("THEN     ", self.consequent)
        print("strength:", self.strength)
        print()

class Application:
    """Represents an application."""
    app_id = ""         # Application identifier (str)
    data = []           # List of ValVarPair

    def print_application(self):
        """Prints the application."""
        print("App ID:", self.app_id)
        for elem in self.data:
            print(elem[0], "is", elem[1])
        print()
