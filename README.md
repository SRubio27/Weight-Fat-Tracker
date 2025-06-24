# Weight & Body Fat Tracker 🏋️‍♂️📊

A simple Python-based console application for tracking daily weight, waist, and neck measurements, with automatic calculation of body fat percentage (for men only, using the U.S. Navy method). Data is stored in a local CSV file and visualized using interactive matplotlib charts.

---

## 🚀 Features

- Register daily entries of:
  - Weight (kg)
  - Waist (cm)
  - Neck (cm)
- Calculates body fat percentage (US Navy method)
- Automatically reuses the last value if 0 is entered
- Deletes specific entries by date
- Interactive plot with options to view:
  - Weight
  - Waist
  - Body Fat Percentage
- Data saved in `weight_log.csv` (not pushed to GitHub for privacy)

---

## 📦 Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```

`requirements.txt`:
```
pandas
matplotlib
```

---

## 📂 File Structure

```
Weight-Fat-Tracker/
├── app.py               # Main application
├── weight_log.csv       # Your private log file (excluded from GitHub)
├── README.md            # This file
├── requirements.txt     # Dependencies
└── .gitignore           # Prevents logging personal data
```

---

## ▶️ How to Use

Run the app from your terminal:

```bash
python app.py
```

You'll see a menu:

```
=== Weight Tracker ===
1. Register a new entry
2. View progress graph
3. Delete entry by date
4. Exit
```

Choose an option by typing the number.

---

## 🛡️ Privacy

This app saves your physical data (weight, waist, neck) in a file named `weight_log.csv`. This file is **excluded from the repository using `.gitignore`** to protect your privacy.

---

## 📈 Example Plot

An interactive matplotlib window will allow you to choose between weight, waist, and fat % to view your progress.

---

## 📝 License

This project is open source and free to use.
