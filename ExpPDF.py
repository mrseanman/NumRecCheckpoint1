import numpy as np

class ExpPDF(object):

    def __init__(self, tau, upperBound):
        self.tau = tau
        self.upper = upperBound
        self.fMax = 1./self.tau

    #returns value of exp pdf at x
    def evaluate(self, x):
        return 1./self.tau * np.exp(-x/self.tau)

    #returns random value in range according to PDF
    #uses box method
    def nextBox(self):
        #boolean for wether we have found a value to return
        foundVal = False
        while not(foundVal):
            x = np.random.uniform(0, self.upper)
            y = np.random.uniform(0., self.fMax)
            if y <= self.evaluate(x):
                foundVal = True
        return x

    #returns random value in range according to PDF
    #uses inverse cumulative method
    def nextInvCumul(self):
        maxCumul = 1-np.exp(-self.upper/self.tau)
        y = np.random.uniform(0, maxCumul)
        return self.evalInvCumul(y)

    #evaluates the inverse cumulative function associated with
    #pdf distribution
    def evalInvCumul(self, x):
        return -self.tau*np.log(1-x)
