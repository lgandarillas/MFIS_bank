import numpy as np
import skfuzzy as skf
import matplotlib.pyplot as plt
from MFIS_Read_Functions import *
from MFIS_Classes import *


def main():
    #read files
    input_file = readFuzzySetsFile('InputVarSets.txt')
    output_file = readFuzzySetsFile('Risks.txt')
    rules = readRulesFile()
    applications = readApplicationsFile()
    result_file = open('Results.txt', 'w')

    for app in applications:
        fuzzy(app, input_file)

def fuzzy(app, input_file):
    age = app.data[0]
    income = app.data[1]
    assets = app.data[2]
    amount = app.data[3]
    job = app.data[4]
    history = app.data[5]

    for fuzz_set in input_file.values():
        if fuzz_set.var == 'Age':
            if fuzz_set.label == 'Young':
                fuzz_set.memDegree = skf.interp_membership(fuzz_set.x, fuzz_set.y, float(age))
                print(fuzz_set.memDegree)
            elif fuzz_set.label == 'Adult':
                fuzz_set.memDegree = skf.interp_membership(fuzz_set.x, fuzz_set.y, age)
                print(fuzz_set.memDegree)
            else:
                fuzz_set.memDegree = skf.interp_membership(fuzz_set.x, fuzz_set.y, age)
                print(fuzz_set.memDegree)


if __name__ == "__main__":
    main()



"""
    for app in applications:
        x = processApplication(app, imput_file, output_file, rules)
        output_file.write(app.appId + ' ' + str(x) + '\n')

"""

