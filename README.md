
# Sonoma County Animal Shelter: Dog Adoption Outcome Prediction

## 📘 Project Overview

This project analyzes data from the **Sonoma County Animal Shelter** to understand and predict dog adoption outcomes. The shelter's mission is to enhance animal welfare through better resource allocation and efficient adoption matching. By identifying factors that influence whether a dog gets adopted, returned to owner, transferred, or experiences another outcome, we aim to support data-driven decisions in shelter operations.

---

## 🎯 Objectives

- Analyze key factors that influence dog adoption and other outcomes.
- Develop predictive models to estimate outcome types.
- Provide actionable insights to improve adoption rates.

---

## 📊 Hypotheses

1. **Breed & Age**: Younger dogs and popular breeds are more likely to be adopted.
2. **Health Condition**: Dogs in treatable or healthy conditions have a higher chance of adoption.
3. **Size & Color**: Smaller and visually appealing dogs are adopted more quickly.

---

## 📁 Dataset Information

- **Source**: Sonoma County government portal
- **Records**: 13,640 dog entries
- **Columns**: 23 features, including:
  - Name, Type, Breed, Color
  - Sex, Size, Date of Birth
  - Intake & Outcome details
  - Shelter stay duration
  - Health conditions
  - Location (latitude, longitude, zip)

---

## 🧹 Data Processing

- **Cleaning**: Removed rows with missing values and irrelevant unique IDs.
- **Feature Engineering**:
  - Calculated `Age` from birth and outcome date.
  - Applied log and square-root transformations to `Age` and `Days in Shelter`.
  - Encoded categorical features using One-Hot and Frequency Encoding.
  - Grouped dog colors into 4 categories for simplification.
  - Consolidated rare outcome types under `Other`.
- **Final Dataset**: 13,505 rows × 20 features (all numeric)

---

## ⚙️ Model Implementation

### 🧪 Feature Selection Methods:
- **All Features (Passthrough)**
- **SelectKBest** (f_classif based)
- **VarianceThreshold** (removes low variance features < 0.2)

### 🤖 Models Used:
1. **Logistic Regression**
2. **K-Nearest Neighbors (KNN)**
3. **Support Vector Machine (SVM)** – Linear and RBF kernel
4. **Decision Tree**
5. **Naive Bayes**
6. **Random Forest**
7. **XGBoost**

### 🔄 Model Workflow:
1. Train-Test Split (80:20)
2. Feature Scaling
3. Model Training with Pipelines
4. Hyperparameter Tuning via **GridSearchCV**
5. Evaluation Metrics: **Accuracy**, **Precision**, **Recall**, **F1 Score**

---

## 🏆 Best Model Results

- **Best Model**: XGBoost with passthrough features and RobustScaler
- **Accuracy**: **83%**
- **F1 Score**: 
  - Class 2 (e.g., Adoption): Precision **92%**, Recall **93%**
  - Class 3: Recall was low (41%) → improvement needed
- **Confusion Matrix Insight**: 
  - Strong performance in `Adoption` and `Return to Owner`
  - Challenges in accurately predicting `Transfer` outcomes

---

## 🔍 Key Insights

| Feature                         | Importance     |
|---------------------------------|----------------|
| `Intake_Condition_UNTREATABLE` | 0.360          |
| `HEALTHY`                       | 0.057          |
| `Age_log`                       | 0.023          |
| `Breed_Frequency`               | 0.017          |

- Health condition at intake is the **most critical** predictor.
- Age and breed have **modest** influence.
- Transfer outcomes need **further attention** due to misclassification.

---

## 📌 Conclusion & Future Work

- The model achieved **good performance**, validating most hypotheses.
- **Health status** and **age** significantly influence adoption.
- Misclassifications in minority classes highlight a need for:
  - **More balanced data**
  - **Alternative sampling strategies**
  - **Advanced ensemble methods**

---

## 🛠 Technologies Used

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **XGBoost**
- **Matplotlib / Seaborn**
- **Jupyter Notebook**

---

## 📬 Contact

- This project is for academic and non-commercial research purposes.
- Please refer to the Sonoma County Open Data Portal [https://data.sonomacounty.ca.gov/] for data usage terms.
