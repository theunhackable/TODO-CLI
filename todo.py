# Let me take in Command Line(CLI) Arguments using sys module.
# Import the required modules.
# "sys" is used to take arguments from CLI
# "os" is used to attach full path of the file with the file name
# "datetime"  module have "date class" which have "today()" method, returns date in "yyyy-mm-dd" format

import sys
import os
from datetime import date

# Globals

TODO = os.path.join(os.getcwd(), 'todo.txt')    # full path of todo.txt.
DONE = os.path.join(os.getcwd(), 'done.txt')    # full path of done.txt.
# USAGE consists of help menu.
USAGE = """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics
"""
        
# "help()" function prints the "USAGE".

def help():
    print(USAGE)

# "add(item)" function adds item(string) to "todo.txt" file and print acknowledgement.

def add(item):
    with open(TODO, 'r') as file:                        # File opened in read mode.
        todo = file.readlines()                          # File is read into "todo list".
    todo.append(item + '\n')                             # Appends item to "todo" list.
    with open(TODO, 'w') as file:                        # Changes written to "todo.txt".
        file.writelines(todo)                              
    print(f'Added todo: "{item}"')                       #  Prints acknowledgement. 

# "ls()" prints the todo list in reverse order.  

def ls():
    with open(TODO,'r') as file:                         # File opened in read mode.
        todo = file.readlines()                          # File is read into "todo list".
    if todo == []:                                       # If todo list is empty then there will be no pending todos.
        print('There are no pending todos!')
    else:                                                # Else prints the todo list in reverse order.
        range_todo = len(todo) - 1
        for i in range(range_todo, -1, -1):
            print(f'[{i + 1}] {todo[i]}', end='')        # As each item contains new line character, end is used to skip '\n' from print 

# "delete(number)" function deletes the item from todo list according to "item number". 

def delete(number):
    todo = []    
    with open(TODO, 'r') as file:                         # File opened in read mode.                        
        todo = file.readlines()                           # File is read into "todo list".
    if number > len(todo) or number < 1:                  # If given number is out of range print acknowledgement.
        print(f'Error: todo #{number} does not exist. Nothing deleted.')
    else:                                                 # Else skip writing the line according to number given, into "todo.txt".
        with open(TODO,'w') as file:
            for i in range(len(todo)):
                if i == number - 1:
                    continue
                file.write(todo[i])
        print(f'Deleted todo #{number}')                  # Prints acknowledgement.

# "done(number)" function remove given line from "todo.txt" and appends it to "done.txt".

def done(number):
    with open(TODO, 'r') as file:                         # File opened in read mode.                   
        todo = file.readlines()                           # File is read into "todo list".
    if number > len(todo) or number < 1:                  # If given number is out of range print acknowledgement.
        print(f'Error: todo #{number} does not exist.')
    else:                                                 # Else skip writing the line according to number given and store it in "done".
        with open(TODO,'w') as file:
            for i in range(len(todo)):
                if i == number - 1:
                    done = todo[i]
                    continue
                file.write(todo[i])

        with open(DONE,'a+') as file:                   # open "done.txt" and append done to it in given format
            file.write(f'x {date.today()} {done}')

        print(f'Marked todo #{number} as done.')
    
# "report()" function prints report if number of tasks todo and number of tasks done

def report():
    with open(TODO, 'r') as file:                         #  Read "todo.txt" and "done.txt" and count lines in both.
        todo = file.readlines()
    with open(DONE, 'r') as file:
        done = file.readlines()

    print(f'{date.today()} Pending : {len(todo)} Completed : {len(done)}')

 
def main():
    # Take two CLI arguments into argument1 and argument2.
    # Note: Take first CLI argument into "argument1" and the second CLI argument is taken according to the first argument inorder to avoid error      
    # There is chance of getting no CLI arguments so exception should be handled
    # According to arguments write if else-if statements.
    # There are 6 cases and 1 default case
    # "try - except" block is used to know whether the commant line contain required arguments 
    argument1, argument2 = None, None # Declared arguments just to remove ambiguity
    try:  
        argument1 = sys.argv[1]
    except IndexError:
        help()
    # For every 2 argument commands "try except" block is there to check the argument is given or not
    
    # add
    
    if argument1 == 'add':
        try:  
            argument2 = sys.argv[2]
            add(argument2)
        except IndexError:
                print("Error: Missing todo string. Nothing added!")
    # ls
    
    elif argument1 == 'ls':
        ls()
    # done
    
    elif argument1 == 'done':
        try:  
            argument2 = sys.argv[2]
            done(int(argument2))
        except IndexError:
                print("Error: Missing NUMBER for marking todo as done.")
    # del
    
    elif argument1 == 'del':
        try:  
            argument2 = sys.argv[2]
            delete(int(argument2))
        except IndexError:
                print("Error: Missing NUMBER for deleting todo.")
    # help
    
    elif argument1 == 'help':
        help()
    
    # report
    
    elif argument1 == 'report':
        report()
    
    # default
    
    else:
        print("Error")

if __name__ == "__main__":    
    # To make sure that "todo.txt" and "done.txt", open and close the files.
    # This will create file if they are not created. 
    # If files already exists then there will be no loss of data because fies are opened in append mode(a)
    file = open(TODO,'a')
    file.close()
    file = open(DONE,'a')
    file.close()
    main()
    