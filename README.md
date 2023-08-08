# Kaggle-Competition---Predict-House-Sale-Prices-with-Machine-Learning
My first **Kaggle Data Science Competition** entry: a **Predictive Machine Learning Model** on the sale **price of houses**. The aim of this competition is to predict the Sale Price of a dataset of houses based on a number of features (79 to be exact). The model I decided to use was a **Random Forest Regressor**, since the multidimensionality was too complex to apply a pure statistical model (although it may be possible). 

This document will present a brief summary of the case, the findings, process and results so far.

It's important to clarify that this is a Work In Progress (WIP) and I'll continue to work on improving these models. Trial and error are only part of the improvement process, that's true for both Machine Learning and Human Learning.


## Contents

  1) data_description.txt: a text file that contains **information on all the features** of this dataset (name, description and possible values for discrete variables).
  2) train.csv: dataset destined to **train the model**, straight from the Kaggle Competition.
  3) test.csv: dataset destined to **test the model** and get the final predictions, also straight from the Kaggle Competition.
  4) functions.py: custom made python script with a function to **clean and prepare this particular dataset** (this function will be used in the jupyter notebook that creates the model).
  5) **Exploratory Data Analysis**.ipynb: jupyter notebook that shows the distribution of prices, it's relation with many variables and provides context and Feature Engineering opportunities.
  6) Random Forest Model - V2.ipynb: **jupyter notebook** that creates the **Random Forest Regressor Model**, trains it, tests it and outputs the data.
  7) Kaggle Competition - House Prices - Advanced Regression Techniquesrandom_forest_v2.rar: compressed file with the **final Random Forest Regressor model**.
  8) submissions_v2.csv: **final output** of the process, file to submit to the Kaggle Competition.

## Context for the Kaggle Competition
This Kaggle Competition (https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) is being held for learning purposes only. It's an Ongoing competition with thousands of teams and individuals that attempt to *predict the test dataset* the best they can. 
There's **no limit to the amount of entries** that can be made, so it leaves *room for improvement* and *learning through iterations*.

The **evaluation metric** is the *Root-Mean-Squared_error* between the *logarithm of the predicted value* and the *logarithm of the observed sales price*. This means, the closer the value is to 0, the better prediction the model made.

## 1st Iteration: Building a Good Random Forest Regressor Model.
For my first attempt I focused on *cleaning the data**, **preparing it for the model** and **training it**. 

The initial dataset has many missing values, it mixes ordinal and categorical values with measures, and is overall somewhat inconsistent. Most of the time went into cleaning that dataset, creating the functions.py file (which not only cleans and prepares but also transforms features to fit the model's needs) and just getting an initial model that worked. 

## 2nd Iteration: Hyper Tuning Random Forest Regressor Model parameters.
On the first attempt, I chose the parameters for the Random Forest Regressor Model arbitrarily. To improve on the previous score, I figured I might as well use a **cross-validation technique** to find the **best parameters** to fit this case.

After some training, the model came out different and got a slightly better result.

## 3rd Iteration (WIP): Advanced **Feature Engineering**.
After seeing the results of my first two attempts, even though the score is promising enough, it still seems that there's room for improvement. 
I decided to perform a much **deeper Exploratory Data Analysis** and focus on the variables: which ones are useful, which ones aren't, are there still variables to be transformed, how are these related to the Sale Price, how are they correlated and much more.

Even though the Exploratory Data Analysis is still not 100% complete (because there are 81 columns to take into account), there's already many insights to apply to this model:
  - Turn MSSubClass from ordinal to categorical
  - Combine Condition1 and Condition2 for one-hot encoding
  - Combine Exterior1st and Exterior2nd for one-hot encoding
  - Combine BsmtType1 and BsmtType2 for one-hot encoding (if they refer to the same basement)
  - Create feature product of quality * area for Pool and Garage
  - Add Ordinal Scale on Fence

To better understand this process, I recommend going through the *Exploratory Data Analysis jupyter notebook*.

## Results

### 1st Iteration
The result I got for this first attempt was **0.14792**. Again, the lower this value is, the better the model did at predicting. Having an initial value of less than 0.15 is a great start.
This put me around position **#2112** out of **4184 teams**.

Here's a graph that shows a preliminary test on the performance of the model.

**Green: Actual**           --             **Red: Predicted**

![image](https://github.com/DataGuti/Kaggle-Competition---Predict-House-Sale-Prices-with-Machine-Learning/assets/57073572/ee07b624-5d4d-4a5c-9adc-b9ff6f84e27c)

## Results

### 2nd Iteration
The result I got for this first attempt was **0.14694**. That's basically a 0.001 decrease on the value (meaning the model improved). Again, the lower the value is, the better the model did, and since the evaluation metric uses logarithms, results are bound to be low.
This put me around position **#1978** out of **4184 teams**.

Here's a graph that shows a preliminary test on the performance of the model.

**Green: Actual**           --             **Red: Predicted**

![image](https://github.com/DataGuti/Kaggle-Competition---Predict-House-Sale-Prices-with-Machine-Learning/assets/57073572/0f83e918-5e44-4f24-87b2-6f902d82d6b1)

### 3rd Iteration
Work In Progress

## Conclusions

This project resulted in a Predictive Machine Learning Model that gets values that are significantly close to the observed ones. Although there's still room for improvement, a model that gets close results has already been acomplished. Still, iterations and trying are key to improving existing models in any field.

## Future Lines of Work

  - Finish the 3rd iteration by applying good practices of **Feature Engineering** (such as the ones mentioned beforehand in the 3rd iteration section).
  - Creating a new model with this dataset and hyper-tuning its parameters for optimal results.
  - Evaluate the possibility of using a Gradient Boosting model and compare its results with the Random Forest model.
  - Try to improve model's predictions for the houses with the highest prices.

