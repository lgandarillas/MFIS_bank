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

    #for fset in input_file.values():
    #    print(fset.var)

    for app in applications:

        membership_dict = {}

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

            print(fset.var + ' ' + fset.label + ": "  + str(membership))

            membership_dict[(fset.var, fset.label)] = membership

        print("\n")
        print(membership_dict)

        print("\n")


if __name__ == '__main__':
    main()

