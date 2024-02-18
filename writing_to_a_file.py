# DAY 7: Writing to a File:
# Create a simple script that asks the user for their name, then writes it to a file called "user_info.txt."

# ========= PSEUDO CODE =========
# - Code for 'open'
file = open('user_info.txt', 'w')

# - Variable for asking the user's name
asking_user = input("Input Your Name:")

# - Code for displaying the inputted information
file.write(asking_user)

# - Code for closing the file
file.close()