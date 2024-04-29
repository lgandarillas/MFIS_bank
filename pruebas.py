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

        print("\n")


if __name__ == '__main__':
    main()

