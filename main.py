from Experiment import Experiment
import numpy as np


#for finding tau from one experiment
#plots a pretty graph with that
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


#calls many experiments and finds distribution data
#associated with averages
def manyExperiments():
    tau = 2.2
    upperBound = 30.
    numVals = 1000
    numExperiments = 500


    experiment = Experiment(tau, upperBound, numVals, numExperiments)

    experiment.runMany()
    print("Mean of all data: " + str(experiment.getResultsSecondMean()))
    print("Std. Dev. of mean of one experiment: " + str(experiment.getStdDevResultsMean()))
    print("Std. Error. on mean of all data: " + str(experiment.getStdDevResultsMean()/np.sqrt(experiment.numExperiments)))
    experiment.plotHist(experiment.resultsMean)




manyExperiments()
#tauFromOneDataSet()
