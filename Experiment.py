import matplotlib.pylab as pl
import sys
import numpy as np

from ExpPDF import ExpPDF

class Experiment(object):

    def __init__(self):
        #upperBound
        #the choice of upper bound has a large effect on final results!
        self.upper = 25.
        self.tau = 2.2

    #fills an array of random numbers according
    #to pdf using box method
    def runResultsBox(self, numIter):
        pdf = ExpPDF(self.tau, self.upper)

        self.results = []
        for i in range(numIter):
            self.results.append(pdf.nextBox())

    #fills an array of random numbers according
    #to pdf using Inverse Cumulative method
    def runResultsInvCumul(self, numIter):
        pdf = ExpPDF(self.tau, self.upper)

        self.results = []
        for i in range(numIter):
            self.results.append(pdf.nextInvCumul())


    #returns mean of self.results
    def getResultsMean(self):
        N = float(len(self.results))
        mean = sum(self.results)/N
        return mean

    def getStdDevResultsMean(self):
        return np.std(self.resultsMean, axis = 0)

    def getResultsSecondMean(self):
        return np.mean(self.resultsMean)

    def plotHist(self, data):
        pl.hist(data, bins = 100)
        pl.show()


    #runs runResults__ many times and gathers mean
    #and other experimental values
    '''
        numiterVals: the number of data points taken in a set
        numIterExperiments: the number of sets of data taken
        runResultsSecond: array of numIterExperiments many runResults
        resultsMean: array of all the means of the corresponding results
    '''
    def runMany(self, numIterExperiments, numIterVals):
        self.resultsSecond = []
        self.resultsMean = []
        for i in range(numIterExperiments):
            sys.stdout.write("\r" + str(100*i/numIterExperiments)[0:3] + "%")

            self.runResultsInvCumul(numIterVals)
            self.resultsMean.append(self.getResultsMean())
            self.resultsSecond.append(self.results)

            sys.stdout.flush()
        print("")
