import sys, math, hmm, algorithms, util

def printHelp():
    print "HMM.py Help message"

def main(args):
    #hardcoding hmm for now, parsing can be done later
    s = [1,2,3,4]
    a = {(1,1):0.999916, (1,2):0.0000760902, (1,3):8.27877e-6, (1,4):1.14809e-7,
        (2,1):0.000128404, (2,2):0.999786, (2,3):0.0000848889, (2,4):1.17723e-6,
        (3,1):0.000128404, (3,2):0.000780214, (3,3):0.999068, (3,4):0.0000235507,
        (4,1):0.000128404, (4,2):0.000780214, (4,3):0.00169821, (4,4):0.997393}
    q = ["D", "I"]
    p = {1:0.603154, 2:0.357419, 3:0.0388879, 4:0.000539295}
    e = {(1, "D"):0.00389708, (1, "I"):0.996103,
        (2, "D"):0.0163858, (2, "I"):0.983614,
        (3, "D"):0.0399756, (3, "I"):0.960024,
        (4, "D"):0.0782973, (4, "I"):0.921703}

    markovModel = hmm.HMM(s, q, a, e, p)
    print "HMM", markovModel
    print "Forward: Emission = D, Prob(D)=", algorithms.forward(markovModel, ["D"])
    #works for sure up to here
    print "Forward: Emission = D,D, Prob(D,D)=", algorithms.forward(markovModel, ["D", "D"])
    
    print "Backward: Emission = D, Prob(D)=", algorithms.backward(markovModel, ["D"])
    print "Backward: Emission = D,D, Prob(D,D)=", algorithms.backward(markovModel, ["D", "D"])
    
    #sequences = util.getSequenceList("./sequences.fasta")
    #print "Baum-Welch Training Sequence Count: ", len(sequences)
    algorithms.baum_welch(markovModel, [list("DIDIDIDIDIDIDDIDIDIDIDIDID")], 10)
            
            
            
if __name__== '__main__':
    main(sys.argv[1:])
