#!/usr/bin/env python3

"""
This module is the main module of the project. It reads the input files,
processes the data andwrites the results to an output file.
"""

import numpy as np
import skfuzzy as skf
from read import read_fuzzy_sets_file, read_rules_file, read_applications_file

def main():
    """Reads the input files, processes the data and writes the results to an output file."""
    fuzzy_sets_dict = read_fuzzy_sets_file('Files/InputVarSets.txt')
    out_fuzzy_sets = read_fuzzy_sets_file('Files/Risks.txt')
    rules = read_rules_file()
    applications = read_applications_file()
    result_file = open('Files/Results.txt', 'w', encoding='utf-8')

    for app in applications:
        fuzzy(app, fuzzy_sets_dict)
        analyze_rules(rules, fuzzy_sets_dict, out_fuzzy_sets)
        result = defuzzify(out_fuzzy_sets)
        result_file.write(str(app.appId)+ " " + str(result) + "\n")


def defuzzify(out_fuzzy_sets):
    """Defuzzifies the output fuzzy sets and returns the result."""
    set_list = []
    nums = np.arange(100)
    for fset in out_fuzzy_sets.values():
        dset = []
        for i in fset.y:
            if i > fset.memDegree:
                dset.append(fset.memDegree)
            else:
                dset.append(i)
        set_list.append(dset)
    lmaximum = np.maximum(set_list[0], np.maximum(set_list[1], set_list[2]))
    #print(lmaximum)
    result = skf.defuzzify.centroid(nums, lmaximum)
    print("Result = ", result)
    return result

def analyze_rules(rules, fuzzy_sets_dict, out_fuzzy_sets):
    """Analyzes the rules and updates the output fuzzy sets."""
    for fset in out_fuzzy_sets.values():
        fset.memDegree = 0

    for rule in rules:
        min_num = 1
        for antecedent_i in rule.antecedent:
            var = fuzzy_sets_dict[antecedent_i].memDegree
            if var < min_num:
                min_num = var

        if min_num >= out_fuzzy_sets[rule.consequent].memDegree:
            out_fuzzy_sets[rule.consequent].memDegree = min_num


def fuzzy(app, fuzzy_sets_dict):
    """Calculates the membership degrees for the input fuzzy sets."""
    for fset in fuzzy_sets_dict.values():
        if fset.var == "Age":
            age = app.data[0][1]
            membership = skf.interp_membership(fset.x, fset.y, age)

        elif fset.var == "IncomeLevel":
            income = app.data[1][1]
            membership = skf.interp_membership(fset.x, fset.y, income)

        elif fset.var == "Assets":
            assets = app.data[2][1]
            membership = skf.interp_membership(fset.x, fset.y, assets)

        elif fset.var == "Amount":
            amount = app.data[3][1]
            membership = skf.interp_membership(fset.x, fset.y, amount)

        elif fset.var == "Job":
            job = app.data[4][1]
            membership = skf.interp_membership(fset.x, fset.y, job)

        elif fset.var == "History":
            history = app.data[5][1]
            membership = skf.interp_membership(fset.x, fset.y, history)
        else:
            print("Error\n")

        fset.memDegree = membership

if __name__ == "__main__":
    main()
