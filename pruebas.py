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

    lables = ["Age", "IncomeLevel", "Assets", "Amount", "Job", "History"]

    for app in applications:

        for fset in input_file.values():
            if fset.var == lables[0]:
                age = app.data[0][1]
                age_mf = skf.interp_membership(fset.x, fset.y, age)
                print("Membresia: " + str(age_mf))

            if fset.var == lables[1]:
                income = app.data[1][1]
                income_mf = skf.interp_membership(fset.x, fset.y, income)
                print("Membresia: " + str(income_mf))

            if fset.var == lables[2]:
                assets = app.data[2][1]
                assets_mf = skf.interp_membership(fset.x, fset.y, assets)
                print("Membresia: " + str(assets_mf))

            if fset.var == lables[3]:
                amount = app.data[3][1]
                amount_mf = skf.interp_membership(fset.x, fset.y, amount)
                print("Membresia: " + str(amount_mf))

            if fset.var == lables[4]:
                job = app.data[4][1]
                job_mf = skf.interp_membership(fset.x, fset.y, job)
                print("Membresia: " + str(job_mf))

            if fset.var == lables[5]:
                history = app.data[5][1]
                history_mf = skf.interp_membership(fset.x, fset.y, history)
                print("Membresia: " + str(history_mf))



        print("\n")


if __name__ == '__main__':
    main()

