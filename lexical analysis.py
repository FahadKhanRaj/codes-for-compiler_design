

keywords=['int', 'float', 'if', 'else', 'True', 'False', 'None', 'and', 'or', 'not', 'in',  'class', 'with', 'as', 'break', 'case', 'const', 'continue', 'case', 'char', 'struct', 'double', 'float', 'public', 'static', 'main', 'if', 'else', 'void']

math_operators=['+', '-', '=', "+=", "-=", "*=", "/=", "%=", "*", "/", "=", "%", "++", "--"]

logical_operators=["<", ">", "<=", ">=", "==", "!", "&&", "||"]

numerical_values=['1','2','3','4','5','6','7','8','9', '0']

others=[',',';','(',')','{','}']


file = open("input.txt")
tokens = file.read().split()
file.close()

#print("----->", tokens)

#these are the empty lists that will contain the final output by matching with the sample output
final_keywords=[]
final_math=[]
final_logical=[]
final_numberical=[]
final_identifier=[]
final_others=[]



#starts here
for i in range(len(tokens)):
    
    #keyword identifying
    #for checking if first token is matching with the keywords
    if tokens[i] in keywords:
        if tokens[i] not in  final_keywords:
            final_keywords.append(tokens[i])
    

    #logical operator identifying
    #for checking if first token is matching with the logical operator
    elif tokens[i] in logical_operators:
        if tokens[i] not in  final_logical:
            final_logical.append(tokens[i])


    #math operator identifying
    #for checking if first token is matching with the math operator
    elif tokens[i] in math_operators:
        if tokens[i] not in  final_math:
            final_math.append(tokens[i])
    
#now others and identifier needs to be handled differently

    #identifying identifiers
    #using builtin function, i can detect whether it is an identifier or not 
    elif tokens[i][0:-1].isalpha():
            #print('------->', tokens[i][0:-1])
            final_identifier.append(tokens[i][0:-1])  #it can also work if i put positive 1. minus use korechi to match with others
            identifier_duplicate_rmv = set(final_identifier) 

    elif tokens[i][-1] in others:                               #others er khetre ulta dik theke ashte hoyeche.
        if tokens[i][-1] not in  final_others: #because others carries exceptional endings. 
            final_others.append(tokens[i][-1])
        
        if len(tokens[i])>1: #for checking if all the tokens are checked. jodi single character thake tahole sheta numerical e hobena.

            #if numerical_values
            if tokens[i][0] in numerical_values:

                if tokens[i][0:-1] not in final_numberical:
                    final_numberical.append(tokens[i][0:-1])
            

            #another way to detect identifier. I am using the other one. but this one also works.
            #else it must be an identifier
            #else:
                #if  tokens[i][0:-1] not in  final_identifier:
                    #final_identifier.append(tokens[i][0:-1])



print("Keywords: " + ", ".join(final_keywords))


print("Identifiers: ", end = '')
identifier_duplicate_rmv = sorted(identifier_duplicate_rmv)
print(*identifier_duplicate_rmv, sep = ", ")

print("Math Operators: " + ", ".join(final_math))

print("Logical Operators: " + ", ".join(final_logical))

print("Numerical Values: " + ", ".join(final_numberical))

print("Others: ", end = '')
print(*final_others, sep = " ")