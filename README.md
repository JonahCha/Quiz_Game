# 🧠 True/False Quiz App in Python

Welcome to the **True/False Quiz App**, a simple command-line-based quiz program built using Python's Object-Oriented Programming (OOP) concepts. This application tests the user's knowledge with a series of true/false computer science questions.

## 📌 Project Overview

This project demonstrates:
- Reading and structuring data
- Object-oriented programming (OOP)
- User interaction via console
- Score tracking and validation

## 📂 Project Structure
```txt
├── data.py # Contains quiz questions in dictionary format
├── question_model.py # Defines the Question class
├── quiz_brain.py # Logic for managing quiz progression and scoring
└── main.py # Entry point and game loop
```


## 🧰 Technologies Used

- 🐍 Python 3.x
- 💻 Command Line Interface (CLI)

## 🧩 How It Works

1. Loads a set of True/False questions from `data.py`
2. Converts questions into `Question` objects
3. Uses the `QuizBrain` class to:
   - Display questions one by one
   - Take user input (True/False)
   - Check answers and track scores
4. At the end, displays the user's final score

## ▶️ Getting Started

### Prerequisites
- Python 3.x installed on your machine

### Run the App

```bash
python main.py
```
## 📸 Example Output
```
Q.1: JavaScript derives from a later version of Java (True/False): false
Correct Answer
Current Score is:1/1

Q.2: The Windows ME operating system was released in the year 2000. (True/False): true
Correct Answer
Current Score is:2/2
...
You Have Completed The Quiz
Your Score is: 10/12
```
