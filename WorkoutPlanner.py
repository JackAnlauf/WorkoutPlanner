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
#         -lifting records
#     Split program.
#         this program contains different types of splits (PPL, totalbody,etc)
#         accounts for availability 
#     Exercises program.
#         -accounts for each exercises differences, strength curves, increments
#         required equipment, injury risk, etc. 
#     Preworkout questionaire program
#         -Asks about energy, gym type, split, etc
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
#     -Figure out github
#     -Get a more concrete writeup of program
#     -Learn how Excel interacts with Python
#     -How to graph
#     -Create simple test cases for "Bob"
#     -lots to do
# 
# 
# =============================================================================


print("Hello world")

print("Hello there")


print("Git practice number 1")

print("Edit from github")


print("Edit from github 2")


print ("merge statement 1")

print("I think im on branch A, so this should be seen only in bracnh A")


print("I think im on main branch, so this and 'Ithink im on branchA' should be here ")