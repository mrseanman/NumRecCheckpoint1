from Experiment import Experiment

def tauFromOneDataSet():
    tau = 2.2
    upperBound = 25.
    numVals = 1000

    #send numExperiments = 0 because irrelevant
    experiment = Experiment(tau, upperBound, numVals, 0)

    experiment.runResultsInvCumul()
    print("Estimation of tau: " + str(experiment.getResultsMean()))
    print("Std. Dev. of results: " + str(experiment.getStdDevResults()))
    experiment.plotHistWithCurve()

def main():
    numExperiments = 5000
    numVals = 100000

    experiment = Experiment()

    '''
    experiment.runMany(numExperiments, numVals)
    print("Mean: " + str(experiment.getResultsSecondMean()))
    print("Std. Deviation of mean lifetime: " + str(experiment.getStdDevResultsMean()))
    print("Mean Std. Deviation in each Experiment: " + str(experiment.getMeanStdDevInResults()))
    experiment.plotHist(experiment.resultsMean)
    '''

    experiment.runResultsInvCumul(numVals)
    print(len(experiment.results))
    experiment.plotHistWithCurve(experiment.results, numVals)



tauFromOneDataSet()
