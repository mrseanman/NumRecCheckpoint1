import matplotlib.pylab as pl
import sys
import numpy as np

from ExpPDF import ExpPDF

class Experiment(object):

    def __init__(self, tau, upperBound, numVals, numExperiments):
        #upperBound
        #the choice of upper bound has a large effect on final results!
        self.upper = upperBound
        self.tau = tau
        self.numVals = numVals
        self.numExperiments = numExperiments



    #fills an array of random numbers according
    #to pdf using box method
    def runResultsBox(self):
        pdf = ExpPDF(self.tau, self.upper)

        self.results = []
        for i in range(self.numVals):
            self.results.append(pdf.nextBox())

    #fills an array of random numbers according
    #to pdf using Inverse Cumulative method
    def runResultsInvCumul(self):
        pdf = ExpPDF(self.tau, self.upper)

        self.results = []
        for i in range(self.numVals):
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

    #returns standard deviation of reults
    def getStdDevResults(self):
        return np.std(self.results)

    #returns std deviation of resultsMean
    def getStdDevResultsMean(self):
        return np.std(self.resultsMean)

    #returns mean of resultsMean
    #this is the mean of all data
    def getResultsSecondMean(self):
        return np.mean(self.resultsMean)


    #runs runResults__ many times and gathers mean
    #and other experimental values
    '''
        numVals: the number of data points taken in a set
        numIterExperiments: the number of sets of data taken
        resultsSecond: list of numIterExperiments many runResults
        resultsMean: list of all the means of the corresponding results
    '''
    def runMany(self):
        self.resultsSecond = []
        self.resultsMean = []
        for i in range(self.numExperiments):
            sys.stdout.write("\r" + str(100*i/self.numExperiments)[0:3] + "%")

            self.runResultsInvCumul()
            self.resultsMean.append(self.getResultsMean())
            self.resultsSecond.append(self.results)

            sys.stdout.flush()
        print("")

    def plotHistWithCurve(self):
        bins = 50

        pdf = ExpPDF(self.tau, self.upper)
        x = np.linspace(0, self.upper, 200)
        y = []
        for val in x:
            #some scaling done
            y.append((self.numVals * self.upper/bins) * pdf.evaluate(val))

        pl.hist(self.results, bins = bins)
        pl.plot(x,y)
        pl.show()

    def plotHist(self, data):
        pl.hist(data, bins = 100)
        pl.show()
