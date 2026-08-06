# 📧 Email Spam Detection using Machine Learning

## 📌 Project Overview

This project is developed as part of the **OASIS INFOBYTE Data Science Internship**.

The objective of this project is to build a Machine Learning model that classifies SMS messages as **Spam** or **Ham (Legitimate)** using Natural Language Processing (NLP) techniques.

---

## 🎯 Objective

- Detect whether an SMS message is Spam or Ham.
- Apply text preprocessing techniques.
- Convert text into numerical features using TF-IDF.
- Train multiple Machine Learning models.
- Compare model performance using evaluation metrics.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- NLTK
- WordCloud
- Jupyter Notebook

---

## 📂 Dataset

- SMS Spam Collection Dataset
- Total Messages: **5572**
- Ham Messages: **4825**
- Spam Messages: **747**

---

## 🔍 Project Workflow

### 1. Data Loading
- Loaded the SMS Spam Collection dataset.
- Checked dataset shape and column names.

### 2. Data Cleaning
- Removed unnecessary columns.
- Renamed columns.
- Checked missing values.

### 3. Exploratory Data Analysis (EDA)
- Spam vs Ham distribution
- Class distribution visualization

### 4. Text Preprocessing
- Converted text to lowercase
- Removed punctuation
- Removed numbers
- Removed stopwords
- Removed extra spaces

### 5. Feature Extraction
- Applied TF-IDF Vectorization

### 6. Model Building
- Multinomial Naive Bayes
- Logistic Regression

### 7. Model Evaluation
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

### 8. Model Comparison
Compared the performance of both Machine Learning models.

### 9. WordCloud Visualization
- Spam WordCloud
- Ham WordCloud

---

## 📊 Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|--------|----------|-----------|--------|----------|
| Multinomial Naive Bayes | **96.68%** | **99.12%** | **75.84%** | **85.93%** |
| Logistic Regression | 95.96% | 99.06% | 70.47% | 82.35% |

---

## 🏆 Best Model

Based on the evaluation metrics, **Multinomial Naive Bayes** achieved the best overall performance and was selected as the final model for spam detection.

---

## 📈 Project Outputs

- Dataset Overview
- Spam vs Ham Bar Chart
- TF-IDF Feature Extraction
- Naive Bayes Confusion Matrix
- Logistic Regression Confusion Matrix
- Model Comparison Table
- Spam WordCloud
- Ham WordCloud

---

## 📚 Conclusion

This project successfully classifies SMS messages into Spam and Ham categories using Machine Learning.

Text preprocessing and TF-IDF Vectorization significantly improved model performance. Among the two models, **Multinomial Naive Bayes** performed better and achieved the highest accuracy, recall, and F1 Score, making it the most suitable model for this spam detection task.

---

## 👨‍💻 Author

**L Bala Sai**

Data Science Intern

OASIS INFOBYTE