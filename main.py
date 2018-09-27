from Experiment import Experiment

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



main()
