#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python Desktop application using Tkinter to calculate BMI
Author: Reshma
"""

# importing tkinter
import tkinter as tk

class BmiCalculator:
    def __init__(self):
        self.root = tk.Tk()
        # Dimension of the application
        self.root.geometry("400x530")
        # Title of the desktop app
        self.root.title("BMI Calculator v.1")
        # Background color of the application root
        self.root.config(bg="#ccffff")
        #variables
        self.weight_var = tk.StringVar()
        self.height_var = tk.StringVar()
        # label
        self.label1 = tk.Label(self.root,text="Enter your height in cm",font=("Arial",16),bg="#ccffff")
        self.label1.pack(pady=27)
        # Getting height using Entry
        self.heightEntry = tk.Entry(self.root,textvariable=self.height_var,width=15,font=("Arial",16),bd=3)
        self.heightEntry.pack(pady=10)
        # label
        self.label2 = tk.Label(self.root, text="Enter your weight in kg", font=("Arial", 16),bg="#ccffff")
        self.label2.pack(pady=10)
        # Getting weight using Entry
        self.weightEntry = tk.Entry(self.root,textvariable=self.weight_var,width=15, font=("Arial", 16),bd=3)
        self.weightEntry.pack(pady=20)
        # Button to calculate BMI
        self.button = tk.Button(self.root,text="Calculate BMI",font=("Times New Roman",16),bg="black",fg="white",command=self.findBMI)
        self.button.pack(padx=30,pady=20)
        # label to display the calculated BMI
        self.bmiLabel = tk.Label(self.root,font=("Tahoma",15),bg="#ccffff")
        self.bmiLabel.pack(pady=7)
        # label to display BMI result
        self.result = tk.Label(self.root,font=("Tahoma",17),text="",height=2,width=36,bg="#ccffff")
        self.result.pack(padx=30,pady=5)
        self.root.mainloop()
      
    # Function to calculate BMI based on inputted height and weight
    def findBMI(self):
        weight = self.weight_var.get()
        height = self.height_var.get()
        # When the height and weight are empty or filled with space
        if weight=="" or weight.isspace() or height=="" or height.isspace():
            self.result.config(text="Height and Weight cannot be empty",bg="brown",fg="white",font=("Tahoma",15))
        # when height and weight are input properly as numbers
        elif weight.isdecimal() and height.isdecimal():
            # converted height in centimetre to metre
            heightMetre = float(height)/100
            # calculating bmi
            bmi = float("{:.2f}".format(float(weight)/heightMetre/heightMetre))
            # Displaying bmi through label 'bmiLabel'
            self.bmiLabel.config(text=f"BMI is {bmi}")
            # Category of BMI result
            if bmi<15:
                self.result.config(text="Very severely underweight",bg="purple",fg="white",font=("Georgia"))
            elif bmi>=15 and bmi<16:
                self.result.config(text="Severely underweight", bg="blue", fg="white",font=("Georgia"))
            elif bmi>=16 and bmi<18.5:
                self.result.config(text="Underweight", bg="#3377ff", fg="black",font=("Georgia",18))
            elif bmi>=18.5 and bmi<=24.9:
                self.result.config(text="Healthy", bg="green", fg="white",font=("Georgia",20))
            elif bmi>=25 and bmi<=29.9:
                self.result.config(text="Overweight", bg="yellow", fg="black",font=("Georgia",20))
            elif bmi>=30 and bmi<40:
                self.result.config(text="Obese", bg="orange", fg="black",font=("Georgia",20))
            elif bmi>=40:
                self.result.config(text="Extremely Obese", bg="red", fg="white",font=("Cambria",23))
        else:
            # When the entered input in height and weight fiels is not numbers
            self.result.config(text="Enter numbers only please",bg="red",font=("Arial",18))
# object created for the class 'BmiCalculator'
BmiCalculator()
