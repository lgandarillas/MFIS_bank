import numpy as np
import skfuzzy as skf
import matplotlib.pyplot as plt
from read_utils import *
from Classes import *


def main():
    #read files
    input_file = readFuzzySetsFile('InputVarSets.txt')
    output_file = readFuzzySetsFile('Risks.txt')
    rules = readRulesFile()
    applications = readApplicationsFile()
    result_file = open('Results.txt', 'w')

    for app in applications:
        fuzzy(app, input_file)
        for fset in input_file.values():
            print(fset.memDegree)
        print("\n")
        #analyze_rules(rules, f_dict)


def analyze_rules(rules, f_dict):
    pass 
   # for rule in rules:
   #     print(rule.antecedent)
   #     print('\n')



def fuzzy(app, input_file):

    for fset in input_file.values():
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

