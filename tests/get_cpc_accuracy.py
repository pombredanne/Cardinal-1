#-----------------------------------------------------------------------------
# Three-Pronged Approach to Exploring the Limits of Static Malware Analyses:  
# Callsite Parameter Cardinality (CPC) Counting: get_cpc_accuracy.py                 
#                                                                               
# Compares the dictionary computed by cpc-tool to the ones generated by
# cpc_extract and tells their accuracy
#                                                                               
# Luke Jones (luke.t.jones.814@gmail.com)                                       
#                                                                               
#-----------------------------------------------------------------------------
from __future__ import print_function
import sys


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Need at least 2 file arguments. Ground truth first.")
        sys.exit()

    truth = dict()
    test = dict()
    with open(sys.argv[1], 'r') as g:
        for line in g:
            tokens = line.split(" ")
            truth[tokens[0]] = tokens[1]
    g.close()

    right_count = 0
    wrong_count = 0
    with open(sys.argv[2], 'r') as f:
        for line in f:
            tokens = line.split(" ")
            try:
                if int(truth[tokens[0]]) == int(tokens[1]):
                    right_count += 1
                else:
                    wrong_count += 1
            except KeyError:
                pass

    percent = float(right_count)/float(right_count+wrong_count)

    print("%f accuracy for %d functions" % (percent,right_count+wrong_count))
    #for entry in truth:
        #print("%s, %s" % (entry, truth[entry]))