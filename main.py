from Experiment import Experiment

def main():
    experiment = Experiment()
    experiment.runResultsInvCumul()
    print(experiment.resultsMean())
    experiment.plotHist(experiment.results)

main()
