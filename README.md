# 🎫 Support Ticket Classifier

A Machine Learning and Natural Language Processing (NLP) based web application that automatically classifies customer support tickets into relevant categories.

The application provides a simple and interactive Streamlit interface where users can enter a customer support issue and receive an automatically predicted support category.

---

## 📌 Project Overview

Customer support teams receive a large number of tickets every day. Manually reading and categorizing each ticket can be time-consuming.

This project automates the support ticket classification process using Machine Learning and Natural Language Processing.

The user enters a customer support issue into the application. The text is processed using TF-IDF feature extraction and passed to a trained Linear Support Vector Machine model to predict the most relevant support category.

---

## ✨ Features

- 🎫 Automatic support ticket classification
- 🧠 Natural Language Processing (NLP)
- 🤖 Machine Learning based prediction
- 📝 Simple support ticket text input
- 💡 Ready-to-use example tickets
- 📊 Word-level TF-IDF
- 🔤 Character-level TF-IDF
- ⚡ Fast predictions
- 🖥️ Interactive Streamlit web interface
- 📂 Multiple support ticket categories

---

## 🧠 Machine Learning Model

The application uses a **Linear Support Vector Machine (Linear SVM)** for text classification.

### Feature Extraction

The model uses two types of TF-IDF features:

### 1. Word-level TF-IDF

Word-level TF-IDF captures important individual words and combinations of words from customer support tickets.

### 2. Character-level TF-IDF

Character-level TF-IDF captures character patterns within the text and helps the model handle variations in words and spelling.

Both feature types are combined and provided to the Linear SVM classifier.

### Machine Learning Pipeline

```text
Customer Support Ticket
          ↓
     Text Cleaning
          ↓
   Word-level TF-IDF
          +
 Character-level TF-IDF
          ↓
      Linear SVM
          ↓
   Predicted Category
```

---

## 📂 Ticket Categories

The application supports the following ticket categories:

- 💳 Billing
- 🔧 Technical Issue
- 🔐 Account Access
- ✨ Feature Request
- 📦 Delivery / Shipping
- 💰 Refund / Return
- ❓ General Inquiry

---

## 🖥️ Application Interface

The application is built using Streamlit and provides an easy-to-use interface.

### 📌 About

The sidebar provides an overview of the Support Ticket Classifier and explains that Natural Language Processing is used to automatically classify customer support tickets.

### 🤖 Model

The application displays the machine learning approach used for classification:

- Linear SVM
- Word-level TF-IDF
- Character-level TF-IDF

### 📝 Ticket Input

Users can enter their customer support issue into the main text input area.

### 💡 Example Tickets

The application provides example buttons that allow users to quickly test the classifier.

Available examples include:

- 💳 Billing
- 🔧 Technical
- 🔐 Account
- 📦 Delivery

### 🔍 Classify Ticket

After entering a ticket, the user can click the **Classify Ticket** button.

The application processes the text and displays the predicted support category.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application and Machine Learning development |
| Pandas | Dataset processing |
| Scikit-learn | Machine Learning |
| TF-IDF | Text feature extraction |
| Linear SVM | Ticket classification |
| Joblib | Saving and loading trained models |
| Streamlit | Web application interface |

---

## 📁 Project Structure

```text
support-ticket-classifier/
│
├── app.py
├── ticket_classifier.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── support_tickets_kaggle.csv
│
├── models/
│   └── ticket_classifier.pkl
│
├── src/
│
└── venv/
```

### File Description

**`app.py`**

Main Streamlit application that provides the user interface and performs ticket classification.

**`ticket_classifier.py`**

Python file containing the ticket classification functionality.

**`requirements.txt`**

Contains the Python packages required to run the project.

**`ticket_classifier.pkl`**

Serialized trained Machine Learning model.

**`support_tickets_kaggle.csv`**

Dataset used for training the classifier.

**`README.md`**

Project documentation.

**`.gitignore`**

Specifies files and folders that should not be uploaded to GitHub.

**`venv/`**

Local Python virtual environment used during development. It should not be uploaded to GitHub.

---

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd support-ticket-classifier
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will start locally and can be opened in a web browser.

---

## 💡 How to Use

### Step 1 — Enter a Ticket

Enter the customer's support issue in the text box.

Example:

```text
I was charged twice for my subscription and would like help with my payment.
```

### Step 2 — Classify the Ticket

Click:

```text
🔍 Classify Ticket
```

### Step 3 — View the Prediction

The application analyzes the entered text and displays the predicted support category.

---

## 📊 Model Training

The Machine Learning model was trained using Google Colab.

The training process consists of:

1. Loading the customer support ticket dataset
2. Combining relevant ticket text
3. Cleaning and preprocessing the text
4. Splitting the dataset into training and testing data
5. Creating Word-level TF-IDF features
6. Creating Character-level TF-IDF features
7. Combining the TF-IDF features
8. Training a Linear SVM classifier
9. Evaluating the trained model
10. Saving the trained model using Joblib

---

## 📈 Model Performance

The trained classifier achieved:

```text
Accuracy: 99.94%
```

The model was evaluated using a separate test dataset.

The evaluation included:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

The classification report showed approximately **1.00 F1-score across the supported categories** on the test set.

---

## 🔄 Application Workflow

```text
             User
               │
               ▼
     Enter Support Ticket
               │
               ▼
        Text Processing
               │
               ▼
     Word + Character TF-IDF
               │
               ▼
          Linear SVM
               │
               ▼
      Predicted Category
               │
               ▼
       Display Result
```

---

## 🎯 Project Objective

The main objective of this project is to demonstrate how Machine Learning and Natural Language Processing can be used to automate customer support ticket categorization.

Automating ticket classification can help support teams:

- Reduce manual ticket sorting
- Organize incoming support requests
- Improve ticket routing
- Save time
- Handle large numbers of tickets more efficiently
- Provide a foundation for automated support systems

---

## 🌟 Advantages

- Fast ticket classification
- Simple user interface
- Easy to use
- Lightweight Machine Learning model
- Combines word and character-level text features
- Can be run locally
- Can be extended for real-world customer support systems

---

## 🔮 Future Enhancements

The project can be further improved by adding:

- ⚡ Automatic urgency detection
- 📊 Prediction confidence visualization
- 📁 Batch CSV ticket classification
- 📈 Support ticket analytics dashboard
- 🗂️ Prediction history
- 🗄️ Database integration
- 🔔 Automatic ticket routing
- 🌐 Cloud deployment
- 🔐 User authentication
- 📧 Email-based ticket classification

---

## 📦 Dependencies

The main Python dependencies are:

```text
streamlit
scikit-learn
joblib
pandas
```

They can be installed using:

```bash
pip install -r requirements.txt
```

---

## 🧪 Example Categories

### Billing

Example:

```text
I was charged twice for my subscription.
```

### Technical Issue

Example:

```text
The application is not working properly.
```

### Account Access

Example:

```text
I cannot access my account.
```

### Feature Request

Example:

```text
I would like to have a new feature added to the application.
```

### Delivery / Shipping

Example:

```text
My order has not been delivered yet.
```

### Refund / Return

Example:

```text
I would like to request a refund for my purchase.
```

### General Inquiry

Example:

```text
I would like some information about your product.
```

---

## 👩‍💻 Author

**Nagasri**

---

## 📜 License

This project is created for educational and portfolio purposes.
