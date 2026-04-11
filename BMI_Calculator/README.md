# BMI Calculator 🏋️

A Python-based BMI (Body Mass Index) Calculator built as part of the Oasis Infobyte Python Development Internship (AICTE OIB-SIP).

## 📌 Project Description
This project calculates the Body Mass Index (BMI) of a user based on their weight and height, and classifies it into health categories. It includes both a CLI and GUI version.

## 🚀 Features
- Takes weight (kg) and height (metres) as input
- Calculates BMI using the standard formula
- Classifies BMI into 4 categories
- Handles invalid inputs and negative values gracefully
- Color coded result display (GUI version)

## 🧮 BMI Formula
BMI = weight / (height × height)

## 📊 BMI Categories
| Category | BMI Range |
|---|---|
| Underweight | Less than 18.5 |
| Normal | 18.5 to 24.9 |
| Overweight | 25 to 29.9 |
| Obese | 30 and above |

## 🛠️ Tech Stack
- Python 3
- Tkinter (GUI)

## ▶️ How to Run

### CLI Version
1. Clone this repository
   git clone https://github.com/amanverma123-prog/OIBSIP.git
2. Navigate to the project folder
   cd OIBSIP/BMI_Calculator
3. Run the script
   python bmi.py

### GUI Version
1. Navigate to the project folder
   cd OIBSIP/BMI_Calculator
2. Run the GUI script
   python bmi_gui.py

## 📁 Project Structure
OIBSIP/
└── BMI_Calculator/
    ├── bmi.py        ← CLI version
    └── bmi_gui.py    ← GUI version (Tkinter)

## 🖥️ GUI Version
Built using Tkinter with:
- Input fields for weight and height
- Color coded result display
  - 🔵 Blue → Underweight
  - 🟢 Green → Normal
  - 🟠 Orange → Overweight
  - 🔴 Red → Obese

## 👨‍💻 Author
Aman Verma
Python Development Intern @ Oasis Infobyte
