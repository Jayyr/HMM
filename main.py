import sys, math, hmm, algorithms, util, parser, seqCompare, fileHandler

def main(args):
    if(len(args) != 2):
        print "Error. main.py needs two arguments"
        print "Example: python main.py sequences.fasta initial_parameters.txt"
        exit()
    if(args[0] != 'sequence.fasta' || args[1] != 'initial_parameters.txt'):
        print "Please input: sequence.fasta, initial_parameters.txt as arguments"
        exit()
    s = [1,2,3,4]
    pParser = parser.pparser()
    parameters = pParser.parse_Parameters(args[1])
    p = parameters[0]
    a = parameters[1]
    e = parameters[2]
    q = ['I', 'D']
    x = seqCompare.compareSequences(args[0])
    markovModel = hmm.HMM(False,s, q, a, e, p)

    #print "HMM", markovModel
    newModel = algorithms.baum_welch_log(markovModel, [x], 10)
    fileHandler.outputEstimatedParameters(newModel, 'estimated_parameters.txt')
    fileHandler.outputLikelihoods([algorithms.forward_log(markovModel, x),algorithms.forward_log(newModel, x)], 'likelihoods.txt')
    decodings_initial = algorithms.decodings(markovModel, x)
    fileHandler.outputDecodings(decodings_initial, 'decodings_initial.txt')
    decodings_estimated = algorithms.decodings(newModel, x)
    fileHandler.outputDecodings(decodings_estimated, 'decodings_estimated.txt')
            
if __name__== '__main__':
    main(sys.argv[1:])
