# SIMBL Weightlifting Program

This is a GUI-based weightlifting and nutrition program calculator built with Python's `tkinter` library. It helps users estimate their lean body mass, suggested daily caloric intake, protein intake, and provides a customized workout plan based on user inputs.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Notes](#notes)

## Project Overview
The SIMBL Weightlifting Program is designed to assist users in planning their nutrition and workout routines based on their body metrics. The program calculates recommended daily calories and protein intake based on the user's lean body mass and displays a workout plan depending on the chosen strength route (e.g., Strongman) and a specified day of the month.

The graphical interface is implemented using `tkinter`, making the tool user-friendly and accessible for users without programming experience.

## Features
- **Lean Body Mass Calculation**: Computes lean body mass using the formula:
  \[
  \text{Lean Body Mass} = \text{Body Weight} \times (1 - \frac{\text{Body Fat Percentage}}{100})
  \]
- **Caloric Intake Suggestion**: Recommends a daily caloric range based on lean body mass.
- **Protein Intake Suggestion**: Suggests the ideal daily protein intake range based on lean body mass.
- **Customized Workout Plans**: Offers strength training workout routines based on the user's chosen route and day of the month.
- **Fullscreen Toggle**: Runs in fullscreen mode with the ability to exit using the `X` button or pressing the `Escape` key.

## Dependencies
- Python 3.x
- `tkinter` library (included with standard Python installations)

## Usage
To use this program, follow these steps:

1. **Input Body Metrics**:
   - Enter body weight (in lbs).
   - Enter body fat percentage.
   - Enter height (in inches).
   - Enter age.

2. **Select a Strength Route**:
   - Choose from "Strongman," "Powerlifting," or "Bodybuilding" using the dropdown menu.

3. **Calculate Metrics**:
   - Click the **Calculate** button to see your Lean Body Mass, suggested daily caloric intake, and protein intake ranges.

4. **Get a Workout Plan**:
   - Enter the day of the month (1-30) for which you want a workout plan.
   - Click the **Show Workout Plan** button to display a recommended workout for that day.

5. **Exit Fullscreen Mode**:
   - To exit fullscreen, click the `X` button in the top-right corner or press the `Escape` key.

## Notes
- This program assumes the user is using Imperial units (pounds for weight and inches for height).
- The workout routines are designed for those following a specific strength route, with sample workouts provided for Strongman training.
- The caloric intake is calculated with a multiplier of 20 per unit of lean body mass and is designed to provide a general range for fitness goals.
- Adjust the `norse` font style if not available on your system, or modify the font settings for compatibility.
