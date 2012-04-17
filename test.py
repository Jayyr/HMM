import sys, math, util, hmm, parser, seqCompare, algorithms, fileHandler

def main(args):
    s = [1,2,3,4]
    pParser = parser.pparser()
    parameters = pParser.parse_Parameters('initial_parameters.txt')
    p = parameters[0]
    a = parameters[1]
    e = parameters[2]
    q = ['I', 'D']
    x = seqCompare.compareSequences('sequences.fasta')
    #x = ['D','I','D','I','D','D','D','I','I','I','I','I','I','I','I','I']
    markovModel = hmm.HMM(False,s, q, a, e, p)

    #backwardLog = algorithms.getBackwardList_log(markovModel, ['D', 'D','I'])
    #for i in backwardLog:
    #    for k,v in i.iteritems():
    #        i[k] = math.exp(v)
    #print "Forward: Emission = D, Prob(D)=", algorithms.getForwardList(markovModel, ['D'])
    #print "Backward: Emission = D, Prob(D)=", algorithms.getBackwardList(markovModel, ['D'])
    #print "Forward: Emission = D, Prob(D)=", algorithms.getForwardList_log(markovModel, ['D'])
    #print "Backward: Emission = D, Prob(D)=", algorithms.getBackwardList_log(markovModel, ['D'])
    #print "Forward: Emission = D, Prob(D)=", algorithms.getForwardList(markovModel, ['D', 'D','I'])
    #print "Backward: Emission = D, Prob(D)=", algorithms.getBackwardList(markovModel, ['D', 'D','I'])
    #print "Forward: Emission = D, Prob(D)=", algorithms.getForwardList_log(markovModel, ['D', 'D','I'])
    #print "Backward: Emission = D, Prob(D)=", backwardLog

    posterior = algorithms.posterior_decoding(markovModel, x)
    outputFile1 = open('posterior_initial.txt', 'w')
    for i in posterior:
        outputFile1.write('%d\n' % i)
    outputFile1.close()

    posterior2 = algorithms.posterior_decoding(markovModel, x)
    outputFile2 = open('posterior_new.txt', 'w')
    for a in posterior2:
        outputFile2.write('%d\n' % a)
    outputFile2.close()

    posterior3 = algorithms.posterior_decoding(markovModel, x)
    outputFile3 = open('posterior_new2.txt', 'w')
    for b in posterior3:
        outputFile3.write('%d\n' % b)
    outputFile3.close()
    
    
    #newModel = algorithms.baum_welch_log(markovModel, [x], 10, 10)
    #
    #print newModel.getTransitionProbabilities()
    #print newModel.getEmissionProbabilities()
    #fileHandler.outputEstimatedParameters(newModel, 'estimated_parameters.txt')
    #fileHandler.outputLikelihoods([algorithms.forward_log(markovModel, x), algorithms.forward_log(newModel, x)], 'likelihoods.txt')


if __name__== '__main__':
    main(sys.argv[1:])
