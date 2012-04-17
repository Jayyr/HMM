import sys, math, hmm, algorithms, util, parser, seqCompare

def main(args):
    if(len(args) != 2):
        print "Error. main.py needs two arguments"
        print "Example: python main.py sequences.fasta initial_parameters.txt"
        exit()
    #hardcoding hmm for now, parsing can be done later
    s = [1,2,3,4]
    pParser = parser.pparser()
    parameters = pParser.parse_Parameters(args[1])
    p = parameters[0]
    a = parameters[1]
    e = parameters[2]
    q = ['D', 'I']
    x = seqCompare.compareSequences(args[0])

    markovModel = hmm.HMM(False,s, q, a, e, p)
    #print "HMM", markovModel
    """
    print "Forward: Emission = D, Prob(D)=", algorithms.forward(markovModel, x)
    print "Forward: Emission = D, Prob(D)=", algorithms.forward(markovModel, ['D'])
    #works for sure up to here
    print "Forward: Emission = D,D, Prob(D,D)=", algorithms.forward(markovModel, ['D', 'D'])
    
    print "Backward: Emission = D, Prob(D)=", algorithms.backward(markovModel, ['D'])
    print "Backward: Emission = D,D, Prob(D,D)=", algorithms.backward(markovModel, ['D', 'D'])
    """
    newModel = algorithms.baum_welch_log(markovModel, [x], 10)
    algorithms.decodings(markovModel, x, "decodings_initial.txt") 
    algorithms.decodings(newModel, x, "decodings_estimated.txt") 
            
if __name__== '__main__':
    main(sys.argv[1:])
