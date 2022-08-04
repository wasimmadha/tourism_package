from flask import Flask, request
import sys
from packagePrediction.entity import package_predictor

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        Age = float(request.json['Age'])
        TypeofContact = float(request.json['TypeofContact'])
        CityTier = float(request.json['CityTier'])
        DurationOfPitch = float(request.json['DurationOfPitch'])
        Occupation = float(request.json['Occupation'])
        Gender = float(request.json['Gender'])
        NumberOfPersonVisiting = float(request.json['NumberOfPersonVisiting'])
        NumberOfFollowups = request.json['NumberOfFollowups']
        ProductPitched = float(request.json['ProductPitched'])
        PreferredPropertyStar = float(request.json['PreferredPropertyStar'])
        MaritalStatus = float(request.json['MaritalStatus'])
        NumberOfTrips = float(request.json['NumberOfTrips'])
        Passport = float(request.json['Passport'])
        PitchSatisfactionScore = request.json['PitchSatisfactionScore']
        OwnCar = float(request.json['OwnCar'])
        NumberOfChildrenVisiting = float(request.json['NumberOfChildrenVisiting'])
        Designation = float(request.json['Designation'])
        MonthlyIncome = float(request.json['MonthlyIncome'])
        
        person_data = package_predictor.GetData(
            Age = Age,
            TypeofContact = TypeofContact,
            CityTier = CityTier,
            DurationOfPitch = DurationOfPitch,
            Occupation = Occupation,
            Gender = Gender,
            NumberOfPersonVisiting = NumberOfPersonVisiting,
            NumberOfFollowups = NumberOfFollowups,
            ProductPitched = ProductPitched,
            PreferredPropertyStar = PreferredPropertyStar,
            MaritalStatus = MaritalStatus, 
            NumberOfTrips = NumberOfTrips,
            Passport = Passport,
            PitchSatisfactionScore = PitchSatisfactionScore,
            OwnCar = OwnCar,
            NumberOfChildrenVisiting = NumberOfChildrenVisiting,
            Designation = Designation,
            MonthlyIncome = MonthlyIncome
        )


        X = person_data.get_dataframe()

        result = package_predictor.PackagePredictor.predict(X)
        
        if(result == 1):
            return "You will buy our package"
        else:
            return "You won't buy our package"

    return 'Done'
if __name__ == "__main__":
    app.run()