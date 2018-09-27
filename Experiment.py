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
        return np.mean(self.results)

    #returns the mean of the standard deviation of all the results in
    #resultsSecond
    def getMeanStdDevInResults(self):
        runningSum = 0.
        for result in self.resultsSecond:
            runningSum += np.std(result)
        return runningSum/len(self.resultsSecond)

    #returns std deviation of resultsMean
    def getStdDevResultsMean(self):
        return np.std(self.resultsMean, axis = 0)

    #returns mean of resultsMean
    #this is the mean of all data
    def getResultsSecondMean(self):
        return np.mean(self.resultsMean)




    #runs runResults__ many times and gathers mean
    #and other experimental values
    '''
        numiterVals: the number of data points taken in a set
        numIterExperiments: the number of sets of data taken
        resultsSecond: list of numIterExperiments many runResults
        resultsMean: list of all the means of the corresponding results
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

    def plotHistWithCurve(self, data, numVals):
        bins = 100

        pdf = ExpPDF(self.tau, self.upper)
        x = np.linspace(0, self.upper, 200)
        y = []
        for val in x:
            #some scaling done
            y.append((numVals * self.upper/bins) * pdf.evaluate(val))

        pl.hist(data, bins = bins)
        pl.plot(x,y)
        pl.show()

    def plotHist(self, data):
        pl.hist(data, bins = 100)
        pl.show()
