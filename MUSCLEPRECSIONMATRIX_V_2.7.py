import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

def calculate_caloric_intake(lean_body_mass):
    return lean_body_mass * 20

def suggest_caloric_intake(daily_caloric_intake):
    min_calories = daily_caloric_intake * 0.7
    max_calories = daily_caloric_intake * 1.0
    return min_calories, max_calories

def calculate_lean_body_mass(body_weight, body_fat_percentage):
    return body_weight * (1 - body_fat_percentage / 100)

def suggest_protein_intake(lean_body_mass):
    min_protein = lean_body_mass * 0.7
    max_protein = lean_body_mass * 1.0
    return min_protein, max_protein

def print_workout(strength_route, day_number):
    if strength_route == "Strongman":
        if day_number == 1:
            return (
                "\nLeg Day Workout:\n"
                "\n"
                "1. Hack Squats - 3 sets of 8-12 reps\n"
                "\n"
                "2. Lunges - 3 sets of 10-15 reps per leg\n"
                "\n"
                "3. Leg Press - 3 sets of 10-15 reps\n"
                "\n"
                "4. Leg Curls - 3 sets of 12-15 reps\n"
                "\n"
                "5. Calf Raises - 4 sets of 15-20 reps\n")
        if day_number == 2:
            return (
                "\nChest Day Workout:\n"
                "1. Bench Press - 4 sets of 8-12 reps\n"
                "2. Incline Dumbbell Press - 3 sets of 8-12 reps\n"
                "3. Chest Flyes - 3 sets of 10-15 reps\n"
                "4. Push-Ups - 3 sets to failure\n"
                "5. Tricep Dips - 4 sets of 8-12 reps\n")

def get_input_and_calculate():
    try:
        body_weight = float(body_weight_entry.get())
        body_fat = float(body_fat_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        
        lean_body_mass = calculate_lean_body_mass(body_weight, body_fat)
        daily_caloric_intake = calculate_caloric_intake(lean_body_mass)
        min_calories, max_calories = suggest_caloric_intake(daily_caloric_intake)
        min_protein, max_protein = suggest_protein_intake(lean_body_mass)

        calorie_intake_label.config(text=f"Suggested Daily Calories: {min_calories:.2f} - {max_calories:.2f} kcal")
        lean_body_mass_label.config(text=f"Lean Body Mass: {lean_body_mass:.2f} {weight_unit}")
        protein_intake_label.config(text=f"Suggested daily protein intake: {min_protein:.2f} - {max_protein:.2f} grams")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight, body fat, height, and age.")

def show_workout_plan():
    try:
        day = int(day_entry.get())
        if day < 1 or day > 30:
            raise ValueError

        strength_route = strength_route_var.get()
        workout_plan = print_workout(strength_route, day)
        workout_label.config(text=workout_plan)
        
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid day (1-30).")

def exit_fullscreen():
    app.attributes('-fullscreen', False)
    app.destroy()

app = tk.Tk()
app.attributes('-fullscreen', True)
app.title("SIMBL Weightlifting Program")

def toggle_fullscreen(event=None): 
    app.attributes("-fullscreen", not app.attributes("-fullscreen"))
app.bind("<Escape>", toggle_fullscreen)

# Set a background color
app.configure(bg="#C0C0C0")

# Create a custom font
title_font = tkfont.Font(family="Norse", size=30, weight="bold")
label_font = tkfont.Font(family="Norse", size=15)
button_font = tkfont.Font(family="Norse", size=15, weight="bold")
workout_font = tkfont.Font(family="Norse", size=25, weight="bold")
exit_font = tkfont.Font(family="Norse", size=25, weight="bold")

# Add a title label
title_label = tk.Label(app, text="Customized Program", font=title_font, fg="#ecf0f1", bg="#C0C0C0")
title_label.place(x=100, y=50)

weight_unit = "lb"  # Freedom Unit Metric
height_unit = "in"
calorie_unit = "kcal"

# Input labels and fields with custom styling
tk.Label(app, text=f"Body Weight ({weight_unit}):", font=label_font, fg="#ecf0f1", bg="#C0C0C0").place(x=100, y=150)
body_weight_entry = tk.Entry(app, bg="#C0C0C0", fg="#ecf0f1", font=label_font)
body_weight_entry.place(x=300, y=150)

tk.Label(app, text="Body Fat Percentage (%):", font=label_font, fg="#ecf0f1", bg="#C0C0C0").place(x=100, y=200)
body_fat_entry = tk.Entry(app, bg="#C0C0C0", fg="#ecf0f1", font=label_font)
body_fat_entry.place(x=300, y=200)

tk.Label(app, text=f"Height ({height_unit}):", font=label_font, fg="#ecf0f1", bg="#C0C0C0").place(x=100, y=250)
height_entry = tk.Entry(app, bg="#C0C0C0", fg="#ecf0f1", font=label_font)
height_entry.place(x=300, y=250)

tk.Label(app, text="Age:", font=label_font, fg="#ecf0f1", bg="#C0C0C0").place(x=100, y=300)
age_entry = tk.Entry(app, bg="#C0C0C0", fg="#ecf0f1", font=label_font)
age_entry.place(x=300, y=300)

tk.Label(app, text="Strength Route:", font=label_font, fg="#ecf0f1", bg="#C0C0C0").place(x=100, y=350)
strength_route_var = tk.StringVar()
strength_route_var.set("Options")
route_menu = tk.OptionMenu(app, strength_route_var, "Strongman", "Powerlifting", "Bodybuilding")
route_menu.config(bg="white", fg="black", font=label_font)
menu = app.nametowidget(route_menu.menuname)
menu.config(bg="white", fg="black")
route_menu.place(x=300, y=345)

#Calculating min and max of different body metrics
tk.Button(app, text="Calculate", command=get_input_and_calculate, font=button_font, bg="white", fg="black", activebackground="#dcdcdc", activeforeground="black").place(x=100, y=400)

lean_body_mass_label = tk.Label(app, text="Lean Body Mass: ", font=label_font, fg="#ecf0f1", bg="#C0C0C0")
lean_body_mass_label.place(x=100, y=460)

protein_intake_label = tk.Label(app, text="Suggested daily protein intake: ", font=label_font, fg="#ecf0f1", bg="#C0C0C0")
protein_intake_label.place(x=100, y=510)

calorie_intake_label = tk.Label(app, text="Suggested Daily Calorie intake: ", font=label_font, fg="#ecf0f1", bg="#C0C0C0")
calorie_intake_label.place(x=100, y=560)

tk.Label(app, text="Enter day number (1-30) for workout plan:", font=label_font, fg="#ecf0f1", bg="#C0C0C0").place(x=100, y=620)
day_entry = tk.Entry(app, bg="#C0C0C0", fg="#ecf0f1", font=label_font)
day_entry.place(x=400, y=620)

tk.Button(app, text="Show Workout Plan", command=show_workout_plan, font=button_font, bg="white", fg="black", activebackground="#dcdcdc", activeforeground="black").place(x=106, y=680)

#Enter daily intakes
tk.Label(app, text="Todays Protein Intake:", font=label_font, fg="#ecf0f1", bg="#C0C0C0").place(x=500, y=150)
protein_entry = tk.Entry(app, bg="#C0C0C0", fg="#ecf0f1", font=label_font)
protein_entry.place(x=710, y=150)

tk.Label(app, text="Todays Calorie Intake:", font=label_font, fg="#ecf0f1", bg="#C0C0C0").place(x=500, y=200)
calorie_entry = tk.Entry(app, bg="#C0C0C0", fg="#ecf0f1", font=label_font)
calorie_entry.place(x=710, y=200)

tk.Label(app, text="Todays Fat Intake:", font=label_font, fg="#ecf0f1", bg="#C0C0C0").place(x=500, y=250)
fat_entry = tk.Entry(app, bg="#C0C0C0", fg="#ecf0f1", font=label_font)
fat_entry.place(x=710, y=250)

tk.Label(app, text="Todays Carb Intake:", font=label_font, fg="#ecf0f1", bg="#C0C0C0").place(x=500, y=300)
carb_entry = tk.Entry(app, bg="#C0C0C0", fg="#ecf0f1", font=label_font)
carb_entry.place(x=710, y=300)

workout_label = tk.Label(app, text="", font=workout_font, fg="#ecf0f1", bg="#C0C0C0")
workout_label.place(x=800, y=95)

exit_button = tk.Button(app, text="X", command=exit_fullscreen, font=exit_font, bg="black", fg="white")
exit_button.place(relx=0.99, rely=0.01, anchor="ne")

app.mainloop()