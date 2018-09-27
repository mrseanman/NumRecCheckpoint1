from Experiment import Experiment

def main():
    numExperiments = 5000
    numVals = 1000

    experiment = Experiment()
    experiment.runMany(numExperiments, numVals)
    print("Mean: " + str(experiment.getResultsSecondMean()))
    print("Std Deviationstr: " + str(experiment.getStdDevResultsMean()))
    experiment.plotHist(experiment.resultsMean)


main()
