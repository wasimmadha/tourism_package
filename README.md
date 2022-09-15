# Tourism Package Prediction

This project aims to solve the problem of predicting the customer with buy the package or not , using Sklearn's supervised machine learning techniques. It is a classification problem and predictions are carried out on dataset, Several regression techniques have been studied, including XGboost and Random forests of decision trees.

💿 Installing
1. Environment setup.
```
conda create --prefix venv python=3.9 -y
```
```
conda activate venv/
````
2. Install Requirements and setup
```
pip install -r requirements.txt
```
5. Run Application
```
Flask
```


🔧 Built with
- Flask
- Python 3.9
- Machine learning
- 🏦 Industrial Use Cases

## Models Used
* Logistice Regression
* KNN
* Decision Tree
* Random Forest 
* XGBoost
* CatBoost
* AdaBoost

* GridSearchCV is used for Hyperparameter Optimization in the pipeline.

* Any modification has to be done in  Inside Config.yaml which can be done in route **/update_model_config**

## `packagePrediction` is the main package folder which contains 

**Artifact** : Stores all artifacts created from running the application

**Components** : Contains all components of Machine Learning Project
- DataIngestion
- DataValidation
- DataTransformations
- ModelTrainer
- ModelEvaluation
- ModelPusher

**Routes for An API**:
```
/train
```
  * Retrained the model

```
/predict
```
*Parameters*: 
  * Age
  * TypeofContact 
  * CityTier 
  * DurationOfPitch 
  * Occupation 
  * Gender 
  * NumberOfPersonVisiting 
  * NumberOfFollowups ProductPitched 
  * PreferredPropertyStar
  * MaritalStatus 
  * NumberOfTrips 
  * Passport 
  * PitchSatisfactionScore OwnCar 
  * NumberOfChildrenVisiting 
  * Designation 
  * MonthlyIncome 




**Custom Logger and Exceptions** are used in the Project for better debugging purposes.

## Conclusion
- This Project can be used in real-life by Travel agency to predict that the customer will buy package or not
