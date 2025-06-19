# Weight-Fat-Tracker

A simple command-line application written in Python to track daily weight, waist, and neck measurements. It calculates body fat percentage using the U.S. Navy method (for men), stores your data in a CSV file, and provides an interactive plot to visualize your progress.

## 📦 Features

- Daily input for weight, waist, and neck circumference.
- Automatically reuses the last entered values if a new input is skipped (enter `0`).
- Body fat percentage calculation using the U.S. Navy formula (for men).
- Stores data in a local CSV file.
- Interactive matplotlib graph to view weight, waist, or body fat % over time.
- Ability to delete an entry by date.

## 🧮 Requirements

- Python 3.7 or newer
- pandas
- matplotlib

Install dependencies with:

```bash```
pip install -r requirements.txt
 
## 🚀 How to Use
```Run the app from the terminal:```
python app.py

Then follow the on-screen menu:

=== Weight Tracker ===
1. Register a new entry
2. View progress graph
3. Delete entry by date
4. Exit

Measurements are entered in metric units (kg, cm). If you enter 0, the app will reuse the last recorded value (if available).

## 📊 Data Format
The application saves data in a CSV file named weight_log.csv with the following columns:

date,weight,waist,neck,fat_pct
2024-06-01,82.3,92,37,18.75
...

## ✏️ Future Improvements
Support for women’s body fat calculation.

Export graphs and reports to PDF.

Web-based version or mobile app.

Cloud sync or secure backup options
