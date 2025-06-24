import csv
import math
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.widgets import RadioButtons

# Constants
HEIGHT_CM = 178  # Fixed user height in this version
CSV_FILE = "weight_log.csv"

# --- Body fat percentage using U.S. Navy method (for men) ---
def calculate_body_fat(neck_cm, waist_cm):
    if waist_cm <= neck_cm:
        raise ValueError("Waist must be larger than neck for valid calculation.")

    height_in = HEIGHT_CM * 0.3937
    neck_in = neck_cm * 0.3937
    waist_in = waist_cm * 0.3937

    fat_pct = 86.010 * math.log10(waist_in - neck_in) - 70.041 * math.log10(height_in) + 36.76
    return round(fat_pct, 2)

# --- Register a new daily measurement ---
def register_entry():
    try:
        df = pd.read_csv(CSV_FILE)
        last_entry = df.iloc[-1]
        last_weight = last_entry['weight']
        last_waist = last_entry['waist']
        last_neck = last_entry['neck']
        last_date = datetime.strptime(last_entry['date'], "%Y-%m-%d")
        next_date = (last_date + timedelta(days=1)).strftime("%Y-%m-%d")
    except (FileNotFoundError, pd.errors.EmptyDataError, IndexError):
        last_weight = last_waist = last_neck = None
        next_date = datetime.now().strftime("%Y-%m-%d")

    print("Enter your daily measurements. Enter 0 to reuse the last recorded value (if available).")

    weight = float(input(f"Weight (kg) [{last_weight if last_weight is not None else ''}]: ") or last_weight or 0)
    waist = float(input(f"Waist (cm) [{last_waist if last_waist is not None else ''}]: ") or last_waist or 0)
    neck = float(input(f"Neck (cm) [{last_neck if last_neck is not None else ''}]: ") or last_neck or 0)
    weight = weight if weight > 0 else last_weight
    waist = waist if waist > 0 else last_waist
    neck = neck if neck > 0 else last_neck

    try:
        fat_pct = calculate_body_fat(neck, waist)
    except ValueError as e:
        print("Error:", e)
        return

    try:
        with open(CSV_FILE, mode="a+", newline="") as file:
            file.seek(0)
            content = file.read()
            writer = csv.writer(file)
            if content.strip() == "":
                writer.writerow(["date", "weight", "waist", "neck", "fat_pct"])
            writer.writerow([next_date, weight, waist, neck, fat_pct])
        print(f"Entry saved for {next_date}. Body fat: {fat_pct}%\n")
    except Exception as e:
        print("Error saving entry:", e)

# --- Delete a record by date ---
def delete_entry_by_date(date_to_delete):
    try:
        with open(CSV_FILE, "r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)

        header = rows[0]
        filtered_rows = [row for row in rows if row[0] != date_to_delete or row == header]

        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(filtered_rows)

        print(f"Entry with date {date_to_delete} has been deleted.")
    except Exception as e:
        print("Error deleting entry:", e)

# --- Interactive graph with selectable metric ---
def show_interactive_plot():
    try:
        df = pd.read_csv(CSV_FILE, parse_dates=["date"])
    except (FileNotFoundError, pd.errors.EmptyDataError):
        print("No data to display.")
        return

    df = df.sort_values("date")

    metrics = {
        "Weight": ("weight", "Weight (kg)"),
        "Waist": ("waist", "Waist (cm)"),
        "Body Fat %": ("fat_pct", "Body Fat (%)")
    }

    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.3)

    x = df["date"]
    key, ylabel = metrics["Weight"]
    line, = ax.plot(x, df[key], marker='o', linestyle='-', color='teal')
    ax.set_title(f"Progress of {ylabel}")
    ax.set_ylabel(ylabel)
    ax.set_xlabel("Date")
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True)

    ax_radio = plt.axes([0.05, 0.4, 0.2, 0.15], facecolor='lightgray')
    radio = RadioButtons(ax_radio, list(metrics.keys()))

    def update_plot(label):
        column, label_text = metrics[label]
        line.set_ydata(df[column])
        ax.set_ylabel(label_text)
        ax.set_title(f"Progress of {label_text}")
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw_idle()

    radio.on_clicked(update_plot)
    plt.show()

# --- Application menu ---
def menu():
    while True:
        print("\n=== Weight Tracker ===")
        print("1. Register a new entry")
        print("2. View progress graph")
        print("3. Delete entry by date")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register_entry()
        elif choice == "2":
            show_interactive_plot()
        elif choice == "3":
            date = input("Enter the date to delete (YYYY-MM-DD): ")
            delete_entry_by_date(date)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# --- Run app ---
if __name__ == "__main__":
    menu()