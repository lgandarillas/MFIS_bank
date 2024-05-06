#!/usr/bin/env python3

"""
Reads the input files, processes the data and writes the results to an output file.
"""

import numpy as np
import skfuzzy as skf
from classes import FuzzySetsDict, FuzzySet, RuleList, Rule, Application

def read_fuzzy_sets_file(file_name):
    """
    This function reads a file containing fuzzy set descriptions
    and returns a dictionary with all of them.
    """
    fuzzy_sets_dict = FuzzySetsDict()
    infile = open(file_name, 'r', encoding='utf-8')
    line = infile.readline()
    while line != '':
        fuzzy_set = FuzzySet()
        element_list = line.split(', ')
        setid = element_list[0]
        var_label=setid.split('=')
        fuzzy_set.var=var_label[0]
        fuzzy_set.label=var_label[1]

        xmin = int(element_list[1])
        xmax = int(element_list[2])
        a = int(element_list[3])
        b = int(element_list[4])
        c = int(element_list[5])
        d = int(element_list[6])
        x = np.arange(xmin,xmax,1)
        y = skf.trapmf(x, [a, b, c, d])
        fuzzy_set.x = x
        fuzzy_set.y = y
        fuzzy_sets_dict.update( { setid : fuzzy_set } )

        line = infile.readline()
    infile.close()
    return fuzzy_sets_dict

def read_rules_file():
    """This function reads a file containing rules"""
    infile = open('Files/Rules.txt', 'r', encoding='utf-8')
    rules = RuleList()
    line = infile.readline()
    while line != '':
        rule = Rule()
        line = line.rstrip()
        element_list = line.split(', ')
        rule.ruleName = element_list[0]
        rule.consequent = element_list[1]
        lhs = []
        for i in range(2, len(element_list), 1):
            lhs.append(element_list[i])
        rule.antecedent = lhs
        rules.append(rule)
        line = infile.readline()
    infile.close()
    return rules

def read_applications_file():
    """This function reads a file containing applications"""
    infile = open('Files/Applications.txt', 'r', encoding='utf-8')
    application_list = []
    line = infile.readline()
    while line != '':
        element_list = line.split(', ')
        app = Application()
        app.appId = element_list[0]
        app.data = []
        for i in range(1, len(element_list), 2):
            app.data.append([element_list[i], int(element_list[i+1])])
        application_list.append(app)
        line = infile.readline()
    infile.close()
    return application_list
