import numpy as np
import skfuzzy as skf
import matplotlib.pyplot as plt
from read_utils import *
from Classes import *


def main():
    #read files
    fuzzySetsDict = readFuzzySetsFile('InputVarSets.txt')
    out_fuzzy_sets = readFuzzySetsFile('Risks.txt')
    rules = readRulesFile()
    applications = readApplicationsFile()
    result_file = open('Results.txt', 'w')

    for app in applications:
        fuzzy(app, fuzzySetsDict)

        for fset in fuzzySetsDict.values():
            print(fset.memDegree)

        analyze_rules(rules, fuzzySetsDict, out_fuzzy_sets)
        for fset in out_fuzzy_sets.values():
            fset.printSet()


def analyze_rules(rules, fuzzySetsDict, out_fuzzy_sets):

    for fset in out_fuzzy_sets.values():
            fset.memDegree = 0

    for rule in rules:
        print(rule.consequent, rule.antecedent)
        min = 1

        for i in range(0, len(rule.antecedent)):
            var = fuzzySetsDict[rule.antecedent[i]].memDegree
            print("Var = ", var)
            if var < min:
                min = var
                print("Min = ", min)
        print(out_fuzzy_sets[rule.consequent].memDegree)
        if min >= out_fuzzy_sets[rule.consequent].memDegree:
            out_fuzzy_sets[rule.consequent].memDegree = min
        print('\n')







def fuzzy(app, fuzzySetsDict):

    for fset in fuzzySetsDict.values():
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

