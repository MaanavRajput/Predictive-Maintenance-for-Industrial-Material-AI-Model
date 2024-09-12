# Predictive-Maintenance-for-Industrial-Material-AI-Model
TEAM: PUROHIT JOEL JOY          73042 92201
      RAJPUT MAANAV NITIN       97693 86001
      KABIR SAHANI              91365 42980
      AYUSH TIWARI              72768 42423       

Introduction
This project involves training an AI model to predict material failures. By analyzing the historical performance of materials, the model can identify patterns that lead to potential failures, improving predictive maintenance and reducing downtime.

Dataset Description
The dataset used for training the model contains data on various material properties, stress factors, environmental conditions, and failure states. Each row represents a material sample, with features such as:
- Material type
- Stress level(Torque, rotational speed)
- Environmental conditions (air temperature, Process temperature)
- Failure status (binary: 1 for failure, 0 for no failure)

Dataset Split Info
The dataset was divided into the following sets:
- Training set: 80% of the data, used to train the model.
- Validation set: 10% of the data, used for hyperparameter tuning and to avoid overfitting.
- Test set:10% of the data, used to evaluate the model's performance after training.

Approach
The approach used for this project included:
1. Preprocessing:Data cleaning and normalization.
2. Feature selection: Identifying the most relevant features using statistical analysis.
3. Model selection: Logistic Regression which is perfect for binary outputs
4. Training and Optimization: Hyperparameter tuning using grid search and cross-validation to optimize model performance.

Results
The model was able to accurately predict material failures with net precision of 97.30%. 

Dependencies
- Python 3.x
- NumPy
- Pandas
- Scikit-learn
- TensorFlow/PyTorch (depending on the model used)
- Matplotlib/Seaborn for visualizations

Performance and Accuracy
Accuracy: The model achieved an accuracy of 97.30% on the test set.
Precision: 97%
Recall: 97%
Confusion Matrix: The confusion matrix shows the breakdown of true positives, false positives, true negatives, and false negatives.

The F1 score for the model was:

Class 0 (No failure): F1 score = 0.99
Class 1 (Failure): F1 score = 0.37


