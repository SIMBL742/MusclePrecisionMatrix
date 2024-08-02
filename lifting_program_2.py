import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

def calculate_lean_body_mass(body_weight, body_fat_percentage):
    return body_weight * (1 - body_fat_percentage / 100)

def suggest_protein_intake(lean_body_mass):
    min_protein = lean_body_mass * 0.7
    max_protein = lean_body_mass * 1.0
    return min_protein, max_protein

def print_workout(day_number):
    if day_number % 2 == 1:
        return (
            "\nLeg Day Workout:\n"
            "1. Squats - 4 sets of 8-12 reps\n"
            "2. Lunges - 3 sets of 10-15 reps per leg\n"
            "3. Leg Press - 3 sets of 10-15 reps\n"
            "4. Leg Curls - 3 sets of 12-15 reps\n"
            "5. Calf Raises - 4 sets of 15-20 reps\n"
        )
    else:
        return (
            "\nChest Day Workout:\n"
            "1. Bench Press - 4 sets of 8-12 reps\n"
            "2. Incline Dumbbell Press - 3 sets of 8-12 reps\n"
            "3. Chest Flyes - 3 sets of 10-15 reps\n"
            "4. Push-Ups - 3 sets to failure\n"
            "5. Tricep Dips - 4 sets of 8-12 reps\n"
        )

def get_input_and_calculate():
    try:
        body_weight = float(body_weight_entry.get())
        body_fat = float(body_fat_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        experience_level = experience_level_var.get()
        
        lean_body_mass = calculate_lean_body_mass(body_weight, body_fat)
        min_protein, max_protein = suggest_protein_intake(lean_body_mass)

        lean_body_mass_label.config(text=f"Lean Body Mass: {lean_body_mass:.2f} {weight_unit}")
        protein_intake_label.config(text=f"Suggested daily protein intake: {min_protein:.2f} - {max_protein:.2f} grams")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight, body fat, height, and age.")

def show_workout_plan():
    try:
        day = int(day_entry.get())
        if day < 1 or day > 30:
            raise ValueError

        workout_plan = print_workout(day)
        workout_label.config(text=workout_plan)
        
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid day (1-30).")

app = tk.Tk()
app.title("SIMBL Weightlifting Program")

# Set a background color
app.configure(bg="#2c3e50")

# Create a custom font
title_font = tkfont.Font(family="Norse", size=24, weight="bold")
label_font = tkfont.Font(family="Norse", size=14)
button_font = tkfont.Font(family="Norse", size=14, weight="bold")

# Add a title label
title_label = tk.Label(app, text="Customized Program", font=title_font, fg="#ecf0f1", bg="#2c3e50")
title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

weight_unit = "kg"  # Assume metric for simplicity
height_unit = "cm"

# Input labels and fields with custom styling
tk.Label(app, text="Body Weight (kg):", font=label_font, fg="#ecf0f1", bg="#2c3e50").grid(row=1, column=0, sticky="e", padx=10, pady=5)
body_weight_entry = tk.Entry(app, bg="#34495e", fg="#ecf0f1", font=label_font)
body_weight_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(app, text="Body Fat Percentage (%):", font=label_font, fg="#ecf0f1", bg="#2c3e50").grid(row=2, column=0, sticky="e", padx=10, pady=5)
body_fat_entry = tk.Entry(app, bg="#34495e", fg="#ecf0f1", font=label_font)
body_fat_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(app, text=f"Height ({height_unit}):", font=label_font, fg="#ecf0f1", bg="#2c3e50").grid(row=3, column=0, sticky="e", padx=10, pady=5)
height_entry = tk.Entry(app, bg="#34495e", fg="#ecf0f1", font=label_font)
height_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(app, text="Age:", font=label_font, fg="#ecf0f1", bg="#2c3e50").grid(row=4, column=0, sticky="e", padx=10, pady=5)
age_entry = tk.Entry(app, bg="#34495e", fg="#ecf0f1", font=label_font)
age_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(app, text="Experience Level:", font=label_font, fg="#ecf0f1", bg="#2c3e50").grid(row=5, column=0, sticky="e", padx=10, pady=5)
experience_level_var = tk.StringVar()
experience_level_var.set("Beginner")
experience_menu = tk.OptionMenu(app, experience_level_var, "Beginner", "Intermediate", "Advanced")
experience_menu.config(bg="white", fg="black", font=label_font)

# Configure the menu part of the OptionMenu
menu = app.nametowidget(experience_menu.menuname)
menu.config(bg="white", fg="black")

experience_menu.grid(row=5, column=1, padx=10, pady=5)

tk.Button(app, text="Calculate", command=get_input_and_calculate, font=button_font, bg="white", fg="black", activebackground="#dcdcdc", activeforeground="black").grid(row=6,
column=0, columnspan=2, pady=(20, 10))

lean_body_mass_label = tk.Label(app, text="Lean Body Mass: ", font=label_font, fg="#ecf0f1", bg="#2c3e50")
lean_body_mass_label.grid(row=7, column=0, columnspan=2, pady=5)

protein_intake_label = tk.Label(app, text="Suggested daily protein intake: ", font=label_font, fg="#ecf0f1", bg="#2c3e50")
protein_intake_label.grid(row=8, column=0, columnspan=2, pady=5)

tk.Label(app, text="Enter day number (1-30) for workout plan:", font=label_font, fg="#ecf0f1", bg="#2c3e50").grid(row=9, column=0, sticky="e", padx=10, pady=5)
day_entry = tk.Entry(app, bg="#34495e", fg="#ecf0f1", font=label_font)
day_entry.grid(row=9, column=1, padx=10, pady=5)

tk.Button(app, text="Show Workout Plan", command=show_workout_plan, font=button_font, bg="white", fg="black", activebackground="#dcdcdc", activeforeground="black").grid(row=10,
column=0, columnspan=2, pady=(20, 10))

workout_label = tk.Label(app, text="", font=label_font, fg="#ecf0f1", bg="#2c3e50")
workout_label.grid(row=11, column=0, columnspan=2, pady=(10, 20))

app.mainloop()
