def estimator(data):
    import json



    data = json.loads(data)

    def Impact(data):
        currentlyInfected = data.get("reportedCases") * 10
        infectionsByRequestedTime = currentlyInfected * 1024
        severeCasesByRequestedTime = 0.15 * infectionsByRequestedTime
        totalhosbed4severe = 0.35 * data['totalHospitalBeds']
        hospitalBedsByRequestedTime = totalhosbed4severe - severeCasesByRequestedTime
        return {'currentlyInfected': currentlyInfected, 'infectionsByRequestedTime': infectionsByRequestedTime}

    def severeImpact(data):
        currentlyInfected = data['reportedCases'] * 50
        infectionsByRequestedTime = currentlyInfected * 1024
        severeCasesByRequestedTime = 0.15 * infectionsByRequestedTime
        totalhosbed4severe = 0.35 * data['totalHospitalBeds']
        hospitalBedsByRequestedTime = totalhosbed4severe - severeCasesByRequestedTime

        return {'currentlyInfected': currentlyInfected, 'infectionsByRequestedTime': infectionsByRequestedTime}

    return data, Impact(data), severeImpact(data)
data = input()

estimator(data)