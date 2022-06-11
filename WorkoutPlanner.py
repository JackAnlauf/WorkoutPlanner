##WorkoutPlanner Project 

# =============================================================================
# 
# Goals:
#     -Maintain excel spreadsheet through python (edit and view)
#       -Excel/Python Integration
#        -openpyxl?? what other necessary libraries 
#     -Clean user experience 
#     -can graph data for user
#     -maintains information about user
#     -very interactive with user
#     -etc
# =============================================================================

# =============================================================================
# Example:
#     Bob is a new user. He opens the program and tells it he is new. Bob enters
#     information about himself like age, sex, experience,injuries, etc. Next, he is asked
#     (if applicable) his lifting/athletic records (for example, his best ever 
#     benchpress is 200 pounds), his goals (250 pounds), his most recent lifting 
#     records (maxed out at 180 pounds for 4 reps 2 weeks ago). These are questions
#     for the important and fundamental exercises that are maintained in the database
#     He is then asked what his availability is (like how consistant he can go to gym)
#     what kind of equipment he has (like a full gym or nothing at all) and what 
#     kind of split he can do (the program describes different kinds, for example,
#     a PPL is Push, Pull, Legs, which is a split that focuses on those kinds of lifts
#     that particular day). Lets say bob has a knee problem, maybe this program can 
#     account for this is the recommended exercises. Its time to go to gym for bob. 
#     He opens the program (enters info about the day like type of gym, energy, 
#     preferred kind of lift (like maybe he wants to do push exercises today) etc)
#     the program looks at his data in the spreadsheet, calcualtes the weight x reps
#     for each exercises, and gives them to bob. Bob then writes them down in a little
#     paper notecard (that we designed) and writes his workout on it.
#     After the workout, he tells the program how he did and felt about the exercises.
#     This is recorded in the database for next time. If all is good, say he did the 
#     appropraite reps at a certain weight, next time the weight will be increased 
#     by a "standard increment" like 5 more pounds depending on the kind of exercise. 
#     Bob is interested in his progress. The program can graph his overall results 
#     for a given exercise over time as well as predict it out into the future. 
# =============================================================================
    

# =============================================================================
# Subprograms: (more to come)
#     Initial user info program.
#         -demographics
#         -lifting records and goals 
#     Exercises program.
#         -accounts for each exercises differences, strength curves, increments
#         required equipment, injury risk, etc. 
#     Preworkout questionaire program
#         -Asks about energy, gym type, muscles, etc
#         -adjusts things accordingly
#     Workout Printout
#         -Prints warmup exercises, workout, postworkout
#         -Warmup is standard for now
#          -Workout depends on 
#              a) the split day(i.e. push day)
#              b) the weight,sets,reps for each. This depends on 
#                    i) the strength of the exercise (heavy weights or light)
#                    ii) the previous lift for the user
#                    iii) the goal of the user
#                    iv) the energy of the user 
#              c) the equipment of the user (full gym, bench, pullup bar, etc)
#                    
#
#     Post Workout equestionaire
#         -successful/notsuccessful at "x" exercise
#         -possible factors why why not
#     Standard Increment program
#         -if a previous exercise was successful, consider increasing the weight by (x)
#         next week, or decreasing if complete failure, account for energy level
#     Future prediction program
#         -considers various factors and previous data, and predicts future gains
#         -expresses through graph and print
# =============================================================================
    
# =============================================================================
# To Do List:
#     -Get a more concrete writeup of program
#     -Learn how Excel interacts with Python
#     -How to graph
# 
# 
# =============================================================================



print("Ready to work!")



# =============================================================================
# Simpler version?
#     A program that tracks your lifting data, analyzes it, recommends 
#     (in terms of numbers) reps/sets if trajectory of data is decelerating (i.e
#     your progress for a given exercise is slowing down, maybe it recommends
#     xyz?), known as "hitting a plateu". it tracks data, goal, personal record
#     
# 
# 
#     programs:
#         
#         
#         create user personal database
#             create users own database according to a template?
#         add exercises  
#             program that adds exercise with data to the excel spreadsheet
#             data:
#                 PR = personal record x number of reps
#                 Goal = goal x number of reps 
#                 Recent = most recent weight for reps
#                     this is added here once and updated to be max of 
#                     day 1, day 2 etc
#             
#                 
#         add data
#             to add a single bit of data, usually after a workout
#             ex: 
#                 bench press
#                 day 1 weight
#                 day 1 reps
#             remind user that weight could be body weight x reps (or time)
#             because some exercises are bodyweight for time
#                 
#         data analysis 
#             analyzes data (for a specific exercise)to find: 
#                 best fitted line(growth rate?), projections, 
#                 if certain growth rate, recommend recommendation:
#                 requies atleast x datapoints
#                 
#         recommendation 
#             activated at request, calculates alternative sets,reps,weight for 
#             exercise. It also adds a new exercise that is named "'exercise'alt" 
#             or somehting like that
#             reps/sets determined by old exercise recent data
#             (like take the last three and average it and reduce by 30% and 
#              increase reps )
#             continue to track this alt exercise from then on until indicated
#             otherwise by user
# 
# =============================================================================

# =============================================================================
# Below is just some practice with pandas
# but it could lead to actual code who knows
# =============================================================================
import pandas as pd

import numpy as np


data = (pd.read_excel("WorkoutPlannerdata.xlsx", sheet_name="Sheet1"))

print(data)



#creates a new row, each key is a column name and the value is the new row 
#value, if a key is not given, it defaults to NaN
#x = "Day " + str(len(data.index)-1)
#new_row = {"Records":x}
#data = data.append(new_row,ignore_index = True)


#or to edit a row... (in this case the last row)
#data.loc[len(data.index)-1] = {"Records":x, "benchpress": 250, "squat":350,
                               #"deadlift":450, "row": 150}





#creates a column with default values of 0 for each row index 
#data = data.assign(row=([0]*(len(data.index))))
#data = data.assign(row=[150,180,140,145])





#finds a specifc data point row x column and can be changed
#data.loc[0,"deadlift"] =200
#print(data["squat"].min())




#shows a column of data with non zero data points starting at Day 1
#e = "deadlift"
#q = ((data[e].dropna(how="any"))[2:])
#print (q)




#shows the next day that data will be added to for a given workout
#from this you can find index of that row for necessary calculations/additions
#y = [i for i in q]
#print (y)
#f = len(y)+1
#print("day {} is the next day to add data for {}".format(f,e))





















# if filename is same as og file name, it updates, else, creates a new file
#data.to_excel("workoutPlannerdata.xlsx",index = False)






#notes
#as of now, the way i have this working is each column of exercises are strictly
#independent of the others. So when you want to analyze an exercise, you
#isolate the column and do some methods to turn it into data.
#Each exercise data point is associated with a "day 1, day 2 etc" but this 
#is not linear, should probably rename it. BUt the way i see it, each  "day 1"
#for benchpress is not the literal same day or session for squats. Just because
#they share a row doesnt mean anything. So a day 1 and a day 2 for bench could
# be 3 days but it could be 10 days for a squat.

#I have it this way at the moment because this is the best understanding of
#pandas syntax at the moment. 







