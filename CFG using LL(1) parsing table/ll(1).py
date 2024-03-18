#FAHAD KHAN RAJ
#20101250


#Defining the Parsing Table
parse = {
    ("E", "id"): ["T", "E'"],
    ("E", "("): ["T", "E'"],
    ("E", ")"): ["ε"],
    ("E'", "+"): ["+", "T", "E'"],
    ("E'", "*"): ["ε"],
    ("E'", ")"): ["ε"],
    ("E'", "$"): ["ε"],
    ("T", "id"): ["F", "T'"],
    ("T", "+"): ["synch"],
    ("T", "("): ["F", "T'"],
    ("T", ")"): ["synch"],
    ("T", "$"): ["synch"],
    ("T'", "+"): ["ε"],
    ("T'", "*"): ["*", "F", "T'"],
    ("T'", ")"): ["ε"],
    ("T'", "$"): ["ε"],
    ("F", "id"): ["id"],
    ("F", "+"): ["synch"],
    ("F", "*"): ["synch"],
    ("F", "("): ["(", "E", ")"],
    ("F", ")"): ["synch"],
    ("F", "$"): ["synch"],
}

#Given input is id+id*id
#Augmented version is id+id*id$ 
#You can take the input as sample = input() and then taking the values to form an array
#I made a sample input to check the code faster

sample = ['id','+','id','*','id','$']

count = 0
index = 0


var_stack = ['$', 'E']
action = ["ACTION:  "]

output = " " #Generating the output file blank as of now. Eventually the output will be added as string.


while var_stack:
    above_the_stack = var_stack[-1]   #This var will store the top variable of the stack  
    row_of_inputColumn = sample[index] #To Get the current symbol from the input string
    


    print(f'STACK:   {"".join(var_stack[0:])}')
    print(f'INPUT:   {" ".join(sample[index:])}')

    instructions = parse.get((above_the_stack, row_of_inputColumn))
#print("---> Production: ", instructions)

    if instructions == ["synch"]:
          var_stack
          output = "M[" + above_the_stack + "," + row_of_inputColumn + "]=synch.Hence pop from stack."




    # Check if the stack top is a lowercase letter or a special symbol

    elif above_the_stack in ['+', '*', '(', ')', '$'] or above_the_stack.islower():

        if above_the_stack == row_of_inputColumn: # If they match, pop the stack and move input pointer
            var_stack.pop() 
            output = 'ACTION: Match' + row_of_inputColumn

            index += 1
        else: # If not, there's a terminal mismatch
              var_stack.pop()
              output = 'Error: terminal mismatch. Expected '+ above_the_stack+', got '+ row_of_inputColumn    

    else: # Non-terminal symbol, expand using production instruction rules
        instructions = parse.get((above_the_stack, row_of_inputColumn))
        if instructions is not None:
           if instructions == ['ε']:  # Output action for epsilon (empty production)

                var_stack.pop()
                output = f'ACTION: Output {above_the_stack} -> {instructions}'


           else:   # Output action for non-empty production
                var_stack.pop()
                output = f'ACTION: Output {above_the_stack} -> {instructions}'


                for i in reversed(instructions): #i refers to each symbol
                    if i != '':
                        var_stack.append(i) # Push symbols onto the stack in reverse order
        else:  # Empty entry in the parsing table, skip the input symbol
            index+=1
            output = "M[ "+ above_the_stack + "," + row_of_inputColumn + "]=blank.Hence, skipped "+ row_of_inputColumn

    action.append(output)
    print(action[count]) # Print the current action
    count +=1
    print()

# Check whether parsing is not having any synch error or not

sample_count = len(sample)
stack_count = len(var_stack)

if index == sample_count and stack_count == 0:
    print('Accepted')
else:
    print('Rejected')