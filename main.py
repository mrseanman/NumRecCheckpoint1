from Experiment import Experiment

def tauFromOneDataSet():
    tau = 2.2
    upperBound = 30.
    numVals = 1000

    #send numExperiments = 0 because irrelevant
    experiment = Experiment(tau, upperBound, numVals, 0)

    experiment.runResultsInvCumul()
    print("Estimation of tau: " + str(experiment.getResultsMean()))
    print("Std. Dev. of results: " + str(experiment.getStdDevResults()))
    experiment.plotHistWithCurve()

def main():
    tau = 2.2
    upperBound = 30.
    numVals = 1000
    numExperiments = 500


    experiment = Experiment(tau, upperBound, numVals, numExperiments)

    experiment.runMany()
    print("Mean of all data: " + str(experiment.getResultsSecondMean()))
    print("Std. Dev of mean of one experiment: " + str(experiment.getStdDevResultsMean()))
    #print("Mean Std. Deviation in each Experiment: " + str(experiment.getMeanStdDevInResults()))
    experiment.plotHist(experiment.resultsMean)




main()
#tauFromOneDataSet()
