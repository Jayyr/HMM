import sys, math

def outputEstimatedParameters(model, fileName):
    try:
        outputFile = open(fileName, 'w')
    except:
        print "File could not be opened"
    for i in model.getStates():
        outputFile.write('%d %.2e\n' % (i, model.p(i)))
    for i in model.getStates():
        for j in model.getStates():
            outputFile.write('%.2e' % model.a(i,j))
            if j != model.getStates()[len(model.getStates())-1]:
                outputFile.write(' ')
            else:
                outputFile.write('\n')
    for i in model.getStates():
        outputFile.write('%d %.2e %.2e\n' % (i, model.e(i,model.getEmissions()[0]), model.e(i,model.getEmissions()[1])))
    outputFile.close()

def outputLikelihoods(likelihoods, fileName):
    try:
        outputFile = open(fileName, 'w')
    except:
        print "File could not be opened"
    for i in likelihoods:
        outputFile.write('%.2e\n' % i)
    outputFile.close()
    
def outputDecodings(decodings, fileName):
    f = open(fileName, 'w')
    for v in decodings:
        f.write("%d %d %.2e\n" % v)
    f.close()
    
