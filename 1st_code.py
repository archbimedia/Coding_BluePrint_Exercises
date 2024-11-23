# Assignment 1 fulfilled
print('Hello World')

# This is the begin of my code. It presents a greeting.
# Concepts used here: print, string value and new line denotation.
print('Hello, welcome to ArchBiMedia Consult!\n')

# Over here I set a variable called "name" to request input from user using the "input" function.
# The "input" function prints the value parsed to it, in this case the string "What is your name?" then request for feedback or input from the user.
# Concepts used here: Variable and  input function
name = input('What is your name?\n')

# Here I Created a string called "services". Services contains a number of strings that denotes the services that ArchBiMedia Consult offers.
# Concepts used: Variables, new line with \n denotation  new line denotation with triple double quotation ("""), Input function
services = '''\n1 - Research Topic Development
2 - Proposal Development
3 - Data Collection
4 - Data Analysis
5 - Report Writing
6 - References management
7 - Full suite of services

Please select the corresponding number ...\n'''

order = ((input('Hello ' + name + ', how may we be of service to you today?' + services + '\n')))

# Over here, the reponse from the initial prompt has been used along with "if statement" to determine price stored in a variable "price" depending on the input from the client previous response.
# Concepts use: if statement, variable
if order == '1':
    price = '150'
if order == '2':
    price = '750'
if order == '3':
    price = '1500'
if order == '4':
    price = '750'
if order == '5':
    price = '550'
if order == '6':
    price = '750'
if order == '7':
    price = '2500'

# Over here the cost of service order is made known to the user using the print function and the "if statement" from previous line of code.
# Concepts used: print, variable and new line spacing for aesthetics.
print('\nHere is the cost of selected service GHs ' + price + '\n\n\n')

# Over here, the response from the "input funtion" was stored as the variable "Confirmation" which requested from the user a confirmation to proceed with the statement 
Confirmation = (input('Would you like to proceed with the order? (y/n)\n'))

if Confirmation == 'y':
    print('\nGreat ' + name + '! Your order is being processed at the moment!\n\n100% Done!\n\nYour order has been confirmed successfully\n\nHave a great day ' + name)
if Confirmation == 'n':
    print('It is unfortunate ' + name + ' that your order was cancelled! I will be here for your next order when you are ready!\n\nHave a nice day ' + name + '!')