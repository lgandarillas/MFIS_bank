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

        for fset in input_file.values():
            if fset.var == "Age":
                age = app.data[0][1]
                age_mf = skf.interp_membership(fset.x, fset.y, age)
                print(fset.var + ' ' + fset.label + ": "  + str(age_mf))

            if fset.var == "IncomeLevel":
                income = app.data[1][1]
                income_mf = skf.interp_membership(fset.x, fset.y, income)
                print(fset.var + ' ' + fset.label + str(income_mf))

            if fset.var == "Assets":
                assets = app.data[2][1]
                assets_mf = skf.interp_membership(fset.x, fset.y, assets)
                print(fset.var + ' ' + fset.label  + str(assets_mf))

            if fset.var == "Amount":
                amount = app.data[3][1]
                amount_mf = skf.interp_membership(fset.x, fset.y, amount)
                print(fset.var + ' ' + fset.label + str(amount_mf))

            if fset.var == "Job":
                job = app.data[4][1]
                job_mf = skf.interp_membership(fset.x, fset.y, job)
                print(fset.var + ' ' + fset.label + str(job_mf))

            if fset.var == "History":
                history = app.data[5][1]
                history_mf = skf.interp_membership(fset.x, fset.y, history)
                print(fset.var + ' ' + fset.label + str(history_mf))



        print("\n")


if __name__ == '__main__':
    main()

