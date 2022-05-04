print("Open Calculator \nChoose the following Options:\n\n A. ARITHMATICH OPERATORS \n B. LOGICAL OPERATORS\n")
menu1 = input("Enter Your Option: ")
if(menu1 == 'A' or menu1 == 'a'):
    print("\n************************************************************************")
    print("\n --------:ARITHMATIC OPERATION:--------")
    print("\n1. ADDITION\n2. SUBRTACTION\n3. MULTIPLICATION\n4. DIVISION\n")
    sub_menu1 = int(input("Enter Your Option: "))
    operand1 = int(input("\nEnter the First Operand: "))
    operand2 = int(input("\nEnter the Second Operand: "))
    if(sub_menu1 == 1):
        result = operand1+operand2
        print('\n\n RESULT\n',operand1, '+', operand2, 'is: ', result)
    elif(sub_menu1 == 2):
        result = operand1-operand2
        print('\n\n RESULT\n',operand1, '-', operand2, 'is: ', result)
    elif(sub_menu1 == 3):
        result = operand1*operand2
        print('\n\n RESULT\n',operand1, '*', operand2, 'is: ', result)
    elif(sub_menu1 == 4):
        result = operand1/operand2
        print('\n\n RESULT\n',operand1, '/', operand2, 'is: ', result)
    else:
        print("\n\n You have Choosen the Wrong Option")
if(menu1 == 'B' or menu1 == 'b'):
    print("\n************************************************************************")
    print("\n --------:LOGICAL OPERATION:--------")
    print("\n1. AND\n2. OR\n3. NOT\n")
    sub_menu2 = int(input("Enter Your Option: "))
    input1 = int(input("\nEnter the First Input: "))
    input2 = int(input("\nEnter the Second Input: "))
    print("\n")
    if(input1 == 0 or input1 == 1):
        if(input2 == 0 or input2 ==1):
            if(sub_menu2 == 1):
                result = input1 and input2
                print('\n\n RESULT\n',input1, 'AND', input2, 'is: ', result)
            elif(sub_menu2 == 2):
                result = input1 or input2
                print('\n\n RESULT\n',input1, 'OR', input2, 'is: ', result)
            elif(sub_menu2 == 3):
                result1 = not input1
                result2 = not input2
                print('\n\n RESULT\nInverse of',input1, 'is: ', result1, '\nInverse of', input2, 'is: ', result2)
            else:
                print("You have choosen a Wrong Option")
    
    else:
        print("\nChoose Input in 0 or 1")
        
    
