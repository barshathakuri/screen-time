# -*- coding: utf-8 -*-
"""screen_time

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eIqPSx6mQMrYqjq4e_Ljb78y1erzr7Sz
"""

pip install ydata_profiling

import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('/content/Survey Response.csv')
profile = ProfileReport(df, title="Profiling Report")

df.head()

Remove null

df.columns

# Define custom encoding mappings
gender_mapping = {
    'Male': 1,
    'Female': 0
}

occupation_mapping = {
    'Self-employed': 2,
    'Student': 1,
    'Employed': 0
}

education_mapping = {
    "Master's degree": 1,
    "Bachelor's degree": 0,
    'Higher secondary education': 3,
    'Primary education': 2
}

work_screen_time_mapping = {
    'Less than 1 hour': 0,
    '1-2 hours approximately': 1,
    '3-4 hours approximately': 2,
    '5-6 hours approximately': 3,
    'More than 6 hours': 4
}

leisure_screen_time_mapping = {
    'Less than 1 hour': 0,
    '1-2 hours': 1,
    '3-4 hours': 2,
    '5-6 hours': 3,
    'More than 6 hours': 4
}

devices_mapping = {
    'Tablet': 1,
    'Television': 2,
    'Laptop/Computer': 3,
    'Smartphone': 4
}

content_mapping = {
    'News': 1,
    'Movies/TV shows': 2,
    'Educational content': 3,
    'Work-related content': 4
}

stress_mapping = {
    'Rarely': 0,
    'Sometimes': 1,
    'Often': 2
}

sleep_quality_mapping = {
    'Strongly Agree': 3,
    'Agree': 2,
    'Neutral': 1,
    'Disagree': 0,
}

sleep_problems_mapping = {
    'Rarely': 0,
    'Sometimes': 1,
    'Always': 2
}

physical_activity_mapping = {
    'Never': 0,
    '1 time': 1,
    '2 times': 2,
    '3-4 times': 3,
    '5 times': 4
}

quality_time_mapping = {
    'Never': 0,
    'Rarely': 1,
    'Sometimes': 2,
    'Often': 3,
    'Always': 4
}

impact_mapping = {
    'Negative': 0,
    'Neutral': 1,
    'Positive': 2
}

change_mapping = {
    'No change': 0,
    'Decrease screen time': 1,
    'Increase screen time': 2
}

no_impact_mapping = {
    'Strongly disagree': -2,
    'Disagree': -1,
    'Neutral': 0,
    'Agree': 1,
    'Strongly agree': 2
}

profile.to_notebook_iframe()

print(df.describe())

import seaborn as sns
import matplotlib.pyplot as plt

# Set the theme for the plot
sns.set_theme(style="whitegrid")

# Create the histogram with KDE (Kernel Density Estimate)
plt.figure(figsize=(10, 6))
sns.histplot(df['Desired Changes to Screen Time'], kde=True, color='teal', bins=30, edgecolor='black')

# Add a title and labels
plt.title('Distribution of Desired Changes to Screen Time', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Desired Changes', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Customize ticks
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Remove the top and right spines
sns.despine()

# Show the plot
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the style and palette
sns.set(style="whitegrid")
sns.set_palette("pastel")

plt.figure(figsize=(10, 6))
sns.barplot(x='Education Level', y='Screen Time Impact on Quality of Life', data=df, ci=None)
plt.title('Screen Time Impact on Quality of Life by Education Level', fontsize=16)
plt.xlabel('Education Level', fontsize=14)
plt.ylabel('Impact on Quality of Life', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Avg. Daily Screen Time', y='Screen Time Impact on Quality of Life', data=df, palette="coolwarm")
plt.title('Screen Time Impact on Quality of Life by Average Daily Screen Time', fontsize=16)
plt.xlabel('Average Daily Screen Time (hours)', fontsize=14)
plt.ylabel('Impact on Quality of Life', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

plt.figure(figsize=(10, 6))
sns.violinplot(x='Weekly Physical Activity', y='Screen Time Impact on Quality of Life', data=df, palette="muted", inner="quartile")
plt.title('Screen Time Impact on Quality of Life by Weekly Physical Activity', fontsize=16)
plt.xlabel('Weekly Physical Activity', fontsize=14)
plt.ylabel('Impact on Quality of Life', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

plt.figure(figsize=(10, 6))
sns.pointplot(x='Age', y='Screen Time Impact on Quality of Life', data=df, markers='o', linestyles='-', palette="viridis")
plt.title('Screen Time Impact on Quality of Life by Age Group', fontsize=16)
plt.xlabel('Age Group', fontsize=14)
plt.ylabel('Impact on Quality of Life', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(y='Screen Time Impact on Quality of Life', hue=' Gender', data=df, palette="Set2")
plt.title('Screen Time Impact on Quality of Life by Gender', fontsize=16)
plt.xlabel('Count', fontsize=14)
plt.ylabel('Impact on Quality of Life', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='Gender', fontsize=12, title_fontsize=14)
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Sleep Issues from Screen Time', y='Screen Time Impact on Quality of Life', data=df, hue='Age', style=' Gender', palette="deep", s=100, alpha=0.7)
plt.title('Screen Time Impact on Quality of Life vs. Sleep Issues from Screen Time', fontsize=16)
plt.xlabel('Sleep Issues from Screen Time', fontsize=14)
plt.ylabel('Impact on Quality of Life', fontsize=14)
plt.legend(title='Age', fontsize=12, title_fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

g = sns.FacetGrid(df, col='Occupation', row=' Gender', margin_titles=True, height=4, aspect=1.5, palette="coolwarm")
g.map(sns.barplot, 'Screen Time Impact on Quality of Life', 'Occupation', ci=None)
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Screen Time Impact on Quality of Life by Occupation and Gender', fontsize=16)
g.set_axis_labels("Impact on Quality of Life", "")
g.add_legend(title='Occupation', fontsize=12, title_fontsize=14)
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Set a style for the plot
sns.set(style='whitegrid')

# Increase the figure size for better readability
plt.figure(figsize=(14, 10))

# Calculate the correlation matrix
corr = df.corr()

# Create a heatmap with enhanced aesthetics
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",  # Format the annotations to 2 decimal places
    cmap='coolwarm',
    vmin=-1, vmax=1,
    linewidths=0.75,
    linecolor='white',
    cbar_kws={"shrink": .75},  # Shrink the colorbar slightly
    square=True,  # Make the cells square-shaped
    annot_kws={"size": 10, "weight": "bold", "color": "black"}  # Style annotations
)

# Add title and adjust font sizes
plt.title('Correlation Heatmap', fontsize=18, weight='bold')
plt.xticks(fontsize=12, rotation=45, ha='right', weight='bold')
plt.yticks(fontsize=12, weight='bold')

# Adjust the layout to make sure labels and title fit well
plt.tight_layout()

# Display the heatmap
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Define target and features
X = df.drop(columns=["Screen Time Impact on Quality of Life"])
y = df["Screen Time Impact on Quality of Life"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize models
models = {
    "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
    "decision_tree": DecisionTreeClassifier(random_state=42),
    "random_forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(random_state=42),
    "gradient_boosting": GradientBoostingClassifier(random_state=42)
}

# Train and evaluate each model
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = accuracy

# Find the best model
best_model = max(results, key=results.get)
best_accuracy = results[best_model]

print(f"Best Model: {best_model} with Accuracy: {best_accuracy:.2f}")

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Assuming you have a DataFrame `data`

# Select features based on their correlation with the target
features = ["Screen Time & Sleep Quality", "Education Level", "Avg. Daily Screen Time"]
X = df[features]
y = df["Screen Time Impact on Quality of Life"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.2f}")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Select features based on their correlation with the target
features = ["Screen Time & Sleep Quality", "Education Level", "Avg. Daily Screen Time"]
X = df[features]
y = df["Screen Time Impact on Quality of Life"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize models
models = {
    "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
    "decision_tree": DecisionTreeClassifier(random_state=42),
    "random_forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(random_state=42),
    "gradient_boosting": GradientBoostingClassifier(random_state=42)
}

# Train, predict, and evaluate each model
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = accuracy

# Find the best model
best_model = max(results, key=results.get)
best_accuracy = results[best_model]

# Output the results
print("Model Performance:")
for name, accuracy in results.items():
    print(f"{name}: {accuracy:.2f}")

print(f"\nBest Model: {best_model} with Accuracy: {best_accuracy:.2f}")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Sample dataset creation based on correlation values
# Assuming a sample DataFrame `data` with selected columns
# data = pd.DataFrame(...) # This should represent your actual data

# Selecting features based on correlation with the target variable
features = ["Screen Time & Sleep Quality", "Education Level", "Avg. Daily Screen Time", "Sleep Issues from Screen Time"]
X = df[features]
y = df["Screen Time Impact on Quality of Life"]

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initializing models
models = {
    "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
    "decision_tree": DecisionTreeClassifier(random_state=42),
    "random_forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(random_state=42),
    "gradient_boosting": GradientBoostingClassifier(random_state=42)
}

# Training, predicting, and evaluating each model
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = accuracy

# Identifying the best model
best_model = max(results, key=results.get)
best_accuracy = results[best_model]

results, best_model, best_accuracy

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Generating synthetic data for demonstration
data = pd.DataFrame({
    "Screen Time & Sleep Quality": [2, 3, 1, 2, 3, 1, 4, 2, 5, 3, 2, 3, 1, 4, 2],
    "Education Level": [3, 2, 4, 3, 2, 5, 1, 3, 4, 2, 3, 2, 4, 1, 3],
    "Avg. Daily Screen Time": [7, 5, 6, 8, 5, 7, 4, 6, 5, 8, 7, 5, 6, 4, 7],
    "Sleep Issues from Screen Time": [3, 2, 4, 1, 5, 3, 2, 4, 5, 2, 3, 2, 4, 1, 3],
    "Screen Time Impact on Quality of Life": [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
})

# Selecting features based on correlation with the target variable
features = ["Screen Time & Sleep Quality", "Education Level", "Avg. Daily Screen Time", "Sleep Issues from Screen Time"]
X = data[features]
y = data["Screen Time Impact on Quality of Life"]

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Setting up the parameter grids for each model
param_grids = {
    "logistic_regression": {
        'C': [0.01, 0.1, 1, 10, 100],
        'solver': ['liblinear', 'lbfgs']
    },
    "decision_tree": {
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 10, 20],
        'min_samples_leaf': [1, 5, 10]
    },
    "random_forest": {
        'n_estimators': [10, 50, 100],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 10, 20]
    },
    "SVM": {
        'C': [0.01, 0.1, 1, 10],
        'kernel': ['linear', 'rbf', 'poly']
    },
    "gradient_boosting": {
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.01, 0.1, 0.2],
        'max_depth': [3, 5, 7]
    }
}

# Models to evaluate
models = {
    "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
    "decision_tree": DecisionTreeClassifier(random_state=42),
    "random_forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(random_state=42),
    "gradient_boosting": GradientBoostingClassifier(random_state=42)
}

# Performing Grid Search with Cross-Validation
best_estimators = {}
for name, model in models.items():
    grid_search = GridSearchCV(estimator=model, param_grid=param_grids[name], cv=5, scoring='accuracy', n_jobs=-1)
    grid_search.fit(X_train, y_train)
    best_estimators[name] = grid_search.best_estimator_
    print(f"Best parameters for {name}: {grid_search.best_params_}")
    print(f"Best cross-validation accuracy for {name}: {grid_search.best_score_}")

# Evaluating the best models on the test set
test_scores = {}
for name, model in best_estimators.items():
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    test_scores[name] = accuracy

best_model = max(test_scores, key=test_scores.get)
best_accuracy = test_scores[best_model]

print("\nTest Set Accuracy Scores:")
print(test_scores)
print(f"\nBest Model: {best_model} with accuracy: {best_accuracy}")

from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

import numpy as np

# Generating synthetic data for demonstration
data = pd.DataFrame({
    "Screen Time & Sleep Quality": [2, 3, 1, 2, 3, 1, 4, 2, 5, 3, 2, 3, 1, 4, 2],
    "Education Level": [3, 2, 4, 3, 2, 5, 1, 3, 4, 2, 3, 2, 4, 1, 3],
    "Avg. Daily Screen Time": [7, 5, 6, 8, 5, 7, 4, 6, 5, 8, 7, 5, 6, 4, 7],
    "Sleep Issues from Screen Time": [3, 2, 4, 1, 5, 3, 2, 4, 5, 2, 3, 2, 4, 1, 3],
    "Screen Time Impact on Quality of Life": [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
})

# Selecting features based on correlation with the target variable
features = ["Screen Time & Sleep Quality", "Education Level", "Avg. Daily Screen Time", "Sleep Issues from Screen Time"]
X = data[features]
y = data["Screen Time Impact on Quality of Life"]

# Scaling the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Defining models
models = {
    "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
    "decision_tree": DecisionTreeClassifier(random_state=42),
    "random_forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(random_state=42),
    "gradient_boosting": GradientBoostingClassifier(random_state=42)
}

models["logistic_regression"].fit(X_scaled, y)
pred_val = models["logistic_regression"].predict(np.array([1,2,2,1]).reshape(1, -1))
print("tt")
print(pred_val)
# Performing cross-validation
cv_results = {}
for name, model in models.items():
    scores = cross_val_score(model, X_scaled, y, cv=5, scoring='accuracy')
    cv_results[name] = scores.mean()

# Identifying the best model based on cross-validation score
best_model = max(cv_results, key=cv_results.get)
best_score = cv_results[best_model]

print("Cross-Validation Scores:")
print(cv_results)
print(f"\nBest Model: {best_model} with cross-validation accuracy: {best_score}")

from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Generating synthetic data for demonstration
data = pd.DataFrame({
    "Screen Time & Sleep Quality": [2, 3, 1, 2, 3, 1, 4, 2, 5, 3, 2, 3, 1, 4, 2],
    "Education Level": [3, 2, 4, 3, 2, 5, 1, 3, 4, 2, 3, 2, 4, 1, 3],
    "Avg. Daily Screen Time": [7, 5, 6, 8, 5, 7, 4, 6, 5, 8, 7, 5, 6, 4, 7],
    "Sleep Issues from Screen Time": [3, 2, 4, 1, 5, 3, 2, 4, 5, 2, 3, 2, 4, 1, 3],
    "Screen Time Impact on Quality of Life": [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
})

# Selecting features based on correlation with the target variable
features = ["Screen Time & Sleep Quality", "Education Level", "Avg. Daily Screen Time", "Sleep Issues from Screen Time"]
X = data[features]
y = data["Screen Time Impact on Quality of Life"]

# Scaling the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Defining models
models = {
    "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
    "decision_tree": DecisionTreeClassifier(random_state=42),
    "random_forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(random_state=42),
    "gradient_boosting": GradientBoostingClassifier(random_state=42)
}

# Performing cross-validation and storing results
cv_results = {}
for name, model in models.items():
    scores = cross_val_score(model, X_scaled, y, cv=5, scoring='accuracy')
    cv_results[name] = scores.mean()

# Identifying the best model based on cross-validation score
best_model = max(cv_results, key=cv_results.get)
best_score = cv_results[best_model]

print("Cross-Validation Scores:")
print(cv_results)
print(f"\nBest Model: {best_model} with cross-validation accuracy: {best_score}")

# Plotting the results with scores on top of the bars
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")
bars = plt.bar(cv_results.keys(), cv_results.values(), color=sns.color_palette("pastel"), edgecolor='black')

# Adding the accuracy scores on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.02, round(yval, 3), ha='center', va='bottom', fontsize=12)

plt.xlabel('Model', fontsize=14)
plt.ylabel('Cross-Validation Accuracy', fontsize=14)
plt.title('Model Performance Comparison', fontsize=16, weight='bold')
plt.ylim(0, 1)  # Set y-axis limits to be between 0 and 1
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
sns.despine()  # Remove top and right spines
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score, auc

# Create the DataFrame
data = pd.DataFrame({
    "Screen Time & Sleep Quality": [2, 3, 1, 2, 3, 1, 4, 2, 5, 3, 2, 3, 1, 4, 2],
    "Education Level": [3, 2, 4, 3, 2, 5, 1, 3, 4, 2, 3, 2, 4, 1, 3],
    "Avg. Daily Screen Time": [7, 5, 6, 8, 5, 7, 4, 6, 5, 8, 7, 5, 6, 4, 7],
    "Sleep Issues from Screen Time": [3, 2, 4, 1, 5, 3, 2, 4, 5, 2, 3, 2, 4, 1, 3],
    "Screen Time Impact on Quality of Life": [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
})

# Define features and target variable
X = data.drop("Screen Time Impact on Quality of Life", axis=1)
y = data["Screen Time Impact on Quality of Life"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict probabilities on the test set
y_prob = model.predict_proba(X_test)[:, 1]

# Compute ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

# Plot ROC curve
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, auc, ConfusionMatrixDisplay

# Create the DataFrame
data = pd.DataFrame({
    "Screen Time & Sleep Quality": [2, 3, 1, 2, 3, 1, 4, 2, 5, 3, 2, 3, 1, 4, 2],
    "Education Level": [3, 2, 4, 3, 2, 5, 1, 3, 4, 2, 3, 2, 4, 1, 3],
    "Avg. Daily Screen Time": [7, 5, 6, 8, 5, 7, 4, 6, 5, 8, 7, 5, 6, 4, 7],
    "Sleep Issues from Screen Time": [3, 2, 4, 1, 5, 3, 2, 4, 5, 2, 3, 2, 4, 1, 3],
    "Screen Time Impact on Quality of Life": [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
})

# Define features and target variable
X = data.drop("Screen Time Impact on Quality of Life", axis=1)
y = data["Screen Time Impact on Quality of Life"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Display the confusion matrix
ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
plt.title('Confusion Matrix for Logistic Regression')
plt.show()

import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Generating synthetic data for binary classification
data = pd.DataFrame({
    "Feature 1": np.random.rand(100),
    "Feature 2": np.random.rand(100),
    "Feature 3": np.random.rand(100),
    "Feature 4": np.random.rand(100),
    "Target": np.random.randint(0, 2, 100)  # Binary target variable
})

# Selecting features and target
X = data.drop(columns="Target")
y = data["Target"]

# Scaling the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Defining models
models = {
    "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
    "decision_tree": DecisionTreeClassifier(random_state=42),
    "random_forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(random_state=42),
    "gradient_boosting": GradientBoostingClassifier(random_state=42)
}

# Performing cross-validation and storing results
cv_results = {}
for name, model in models.items():
    scores = cross_val_score(model, X_scaled, y, cv=5, scoring='accuracy')
    cv_results[name] = scores.mean()

# Identifying the best model based on cross-validation score
best_model = max(cv_results, key=cv_results.get)
best_score = cv_results[best_model]

print("Cross-Validation Scores:")
print(cv_results)
print(f"\nBest Model: {best_model} with cross-validation accuracy: {best_score}")

# Plotting the results with scores on top of the bars
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")
bars = plt.bar(cv_results.keys(), cv_results.values(), color=sns.color_palette("pastel"), edgecolor='black')

# Adding the accuracy scores on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, round(yval, 3), ha='center', va='bottom', fontsize=12)

plt.xlabel('Model', fontsize=14)
plt.ylabel('Cross-Validation Accuracy', fontsize=14)
plt.title('Binary Classification Model Performance', fontsize=16, weight='bold')
plt.ylim(0, 1)  # Set y-axis limits to be between 0 and 1
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
sns.despine()  # Remove top and right spines
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

# Generating synthetic data for binary classification
data = pd.DataFrame({
    "Feature 1": np.random.rand(100),
    "Feature 2": np.random.rand(100),
    "Feature 3": np.random.rand(100),
    "Feature 4": np.random.rand(100),
    "Target": np.random.randint(0, 2, 100)  # Binary target variable
})

# Selecting features and target
X = data.drop(columns="Target")
y = data["Target"]

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scaling the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Defining models
models = {
    "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
    "decision_tree": DecisionTreeClassifier(random_state=42),
    "random_forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(random_state=42),
    "gradient_boosting": GradientBoostingClassifier(random_state=42)
}

# Training models and plotting confusion matrices
plt.figure(figsize=(15, 10))
for i, (name, model) in enumerate(models.items(), 1):
    # Train the model
    model.fit(X_train_scaled, y_train)

    # Predict on the test set
    y_pred = model.predict(X_test_scaled)

    # Compute confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    # Plot confusion matrix
    plt.subplot(2, 3, i)  # Create subplots
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    disp.plot(cmap=plt.cm.Blues, ax=plt.gca(), colorbar=False)
    plt.title(name)
    plt.grid(False)  # Remove grid for cleaner look

plt.tight_layout()
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns

# Generating synthetic data for binary classification
data = pd.DataFrame({
    "Feature 1": np.random.rand(100),
    "Feature 2": np.random.rand(100),
    "Feature 3": np.random.rand(100),
    "Feature 4": np.random.rand(100),
    "Target": np.random.randint(0, 2, 100)  # Binary target variable
})

# Selecting features and target
X = data.drop(columns="Target")
y = data["Target"]

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scaling the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Defining models
models = {
    "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
    "decision_tree": DecisionTreeClassifier(random_state=42),
    "random_forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(probability=True, random_state=42),  # probability=True is needed for ROC curve
    "gradient_boosting": GradientBoostingClassifier(random_state=42)
}

# Plotting the ROC curves
plt.figure(figsize=(10, 8))
sns.set(style="whitegrid")

for name, model in models.items():
    # Train the model
    model.fit(X_train_scaled, y_train)

    # Predict probabilities
    y_prob = model.predict_proba(X_test_scaled)[:, 1]

    # Compute ROC curve and AUC
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    # Plot the ROC curve
    plt.plot(fpr, tpr, label=f'{name} (AUC = {roc_auc:.2f})')

# Plotting diagonal line for no-skill classifier
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')

# Aesthetics and labels
plt.xlabel('False Positive Rate', fontsize=14)
plt.ylabel('True Positive Rate', fontsize=14)
plt.title('ROC Curves for Binary Classification Models', fontsize=16, weight='bold')
plt.legend(loc='lower right', fontsize=12)
plt.grid(alpha=0.3)
sns.despine()
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_recall_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns

# Generating synthetic data for binary classification
data = pd.DataFrame({
    "Feature 1": np.random.rand(100),
    "Feature 2": np.random.rand(100),
    "Feature 3": np.random.rand(100),
    "Feature 4": np.random.rand(100),
    "Target": np.random.randint(0, 2, 100)  # Binary target variable
})

# Selecting features and target
X = data.drop(columns="Target")
y = data["Target"]

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scaling the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Defining models
models = {
    "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
    "decision_tree": DecisionTreeClassifier(random_state=42),
    "random_forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(probability=True, random_state=42),  # probability=True is needed for probability estimates
    "gradient_boosting": GradientBoostingClassifier(random_state=42)
}

# Plotting the Precision-Recall curves
plt.figure(figsize=(10, 8))
sns.set(style="whitegrid")

for name, model in models.items():
    # Train the model
    model.fit(X_train_scaled, y_train)

    # Predict probabilities
    y_prob = model.predict_proba(X_test_scaled)[:, 1]

    # Compute Precision-Recall curve and AUC
    precision, recall, _ = precision_recall_curve(y_test, y_prob)
    pr_auc = auc(recall, precision)

    # Plot the Precision-Recall curve
    plt.plot(recall, precision, label=f'{name} (AUC = {pr_auc:.2f})')

# Aesthetics and labels
plt.xlabel('Recall', fontsize=14)
plt.ylabel('Precision', fontsize=14)
plt.title('Precision-Recall Curves for Binary Classification Models', fontsize=16, weight='bold')
plt.legend(loc='lower left', fontsize=12)
plt.grid(alpha=0.3)
sns.despine()
plt.show()

from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Generating synthetic data for binary classification
data = pd.DataFrame({
    "Feature 1": np.random.rand(100),
    "Feature 2": np.random.rand(100),
    "Feature 3": np.random.rand(100),
    "Feature 4": np.random.rand(100),
    "Target": np.random.randint(0, 2, 100)  # Binary target variable
})

# Selecting features and target
X = data.drop(columns="Target")
y = data["Target"]

# Scaling the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Defining models
models = {
    "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
    "decision_tree": DecisionTreeClassifier(random_state=42),
    "random_forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(random_state=42),
    "gradient_boosting": GradientBoostingClassifier(random_state=42)
}

models["logistic_regression"].fit(X_scaled, y)
pred_val = models["logistic_regression"].predict(np.array([1,2,2,1]).reshape(1, -1))
print("tt")
print(pred_val)

# Performing cross-validation and storing results
cv_results = {}
for name, model in models.items():
    scores = cross_val_score(model, X_scaled, y, cv=5, scoring='accuracy')
    cv_results[name] = scores.mean()

# Identifying the best model based on cross-validation score
best_model = max(cv_results, key=cv_results.get)
best_score = cv_results[best_model]

print("Cross-Validation Scores:")
print(cv_results)
print(f"\nBest Model: {best_model} with cross-validation accuracy: {best_score}")

# Plotting the results with scores on top of the bars
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")
bars = plt.bar(cv_results.keys(), cv_results.values(), color=sns.color_palette("pastel"), edgecolor='black')

# Adding the accuracy scores on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, round(yval, 3), ha='center', va='bottom', fontsize=12)

plt.xlabel('Model', fontsize=14)
plt.ylabel('Cross-Validation Accuracy', fontsize=14)
plt.title('Binary Classification Model Performance', fontsize=16, weight='bold')
plt.ylim(0, 1)  # Set y-axis limits to be between 0 and 1
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
sns.despine()  # Remove top and right spines
plt.show()

import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

import numpy as np

# Generating synthetic data for demonstration
data = pd.DataFrame({
    "Screen Time & Sleep Quality": [2, 3, 1, 2, 3, 1, 4, 2, 5, 3, 2, 3, 1, 4, 2],
    "Education Level": [3, 2, 4, 3, 2, 5, 1, 3, 4, 2, 3, 2, 4, 1, 3],
    "Avg. Daily Screen Time": [7, 5, 6, 8, 5, 7, 4, 6, 5, 8, 7, 5, 6, 4, 7],
    "Sleep Issues from Screen Time": [3, 2, 4, 1, 5, 3, 2, 4, 5, 2, 3, 2, 4, 1, 3],
    "Screen Time Impact on Quality of Life": [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
})

# Selecting features based on correlation with the target variable
features = ["Screen Time & Sleep Quality", "Education Level", "Avg. Daily Screen Time", "Sleep Issues from Screen Time"]
X = data[features]
y = data["Screen Time Impact on Quality of Life"]

# Scaling the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Defining models
models = {
    "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "SVM": SVC(random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42)
}

models["logistic_regression"].fit(X_scaled, y)
pred_val = models["logistic_regression"].predict(np.array([1,2,2,1]).reshape(1, -1))
print("tt")
print(pred_val)
# Performing cross-validation
cv_results = {}
for name, model in models.items():
    scores = cross_val_score(model, X_scaled, y, cv=5, scoring='accuracy')
    cv_results[name] = scores.mean()

# Identifying the best model based on cross-validation score
best_model = max(cv_results, key=cv_results.get)
best_score = cv_results[best_model]

# Plotting the results with scores on top of the bars
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")
bars = plt.bar(cv_results.keys(), cv_results.values(), color=sns.color_palette("pastel"), edgecolor='black')

# Adding the accuracy scores on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, round(yval, 3), ha='center', va='bottom', fontsize=12)

plt.xlabel('Model', fontsize=14)
plt.ylabel('Cross-Validation Accuracy', fontsize=14)
plt.title('Binary Classification Model Performance', fontsize=16, weight='bold')
plt.ylim(0, 1)  # Set y-axis limits to be between 0 and 1
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
sns.despine()  # Remove top and right spines
plt.show()

print("Cross-Validation Scores:")
print(cv_results)
print(f"\nBest Model: {best_model} with cross-validation accuracy: {best_score}")

import pickle

with open('model.pkl','wb') as f:
    pickle.dump(models["logistic_regression"],f)

