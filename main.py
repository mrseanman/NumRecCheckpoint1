from Experiment import Experiment

def main():
    numExperiments = 500
    numVals = 1000

    experiment = Experiment()
    experiment.runMany(numExperiments, numVals)
    experiment.plotHist(experiment.resultsMean)

main()
