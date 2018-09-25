import matplotlib.pylab as pl
from ExpPDF import ExpPDF

class Experiment(object):

    def __init__(self):
        #upperBound
        self.upper = 10.
        self.tau = 2.2

    #fills an array of random numbers according
    #to pdf using box method
    def runResultsBox(self):
        pdf = ExpPDF(self.tau, self.upper)

        self.results = []
        for i in range(10000):
            self.results.append(pdf.nextBox())

    #fills an array of random numbers according
    #to pdf using Inverse Cumulative method
    def runResultsInvCumul(self):
        pdf = ExpPDF(self.tau, self.upper)

        self.results = []
        for i in range(10000):
            self.results.append(pdf.nextInvCumul())


    #returns mean of self.results
    def resultsMean(self):
        N = float(len(self.results))
        mean = sum(self.results)/N
        return mean


    def plotHist(self, data):
        pl.hist(data, bins = 100)
        pl.show()


    #runs runResults__ many times and gathers mean
    #and other experimental values
    def runMany(Self):
        return None
