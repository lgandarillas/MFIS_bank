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

    for fset in input_file.values():
        print(fset.x)
        print(fset.y)
        print("Membresia: " + str(skf.interp_membership(fset.x, fset.y, 35)))

if __name__ == '__main__':
    main()

