# Calculator

This is a simple calculator made out of python. More features are to be added as the calculator contiues to be under development.

***Prerquisites***
Python 3

***Featrures***

*   Add
    *   Takes two numbers of any value and prints the sum
    *   Inputs for operator
        *   `add`
        *   `+`
*   Subtract
    *   Takes two numbers of any value and prints the difference
    *   Inputs for operator
        *   `subtract`
        *   `-`
        *   `minus`
*   Multiply
    *   Takes two numbers of any value and prints the product
    *   Inputs for operator
        *   `multiply`
        *   `*`
        *   `times`
        *   `time`
*   Exponent
    *   Takes the first number and raises it to the second number and prints the power
    *   Inputs for operator
        *   `exponent`
        *   `^`
*   Root
    *   Takes the first number and roots it by the second number and prints the answer
    *   Inputs for operator
        *   `root`
*   Factorials
    *   Takes the factorial of a number and prints the product
    *   Inputs for operator
        *   `factorial`
        *   `!`
*   Logarithm
    *   Only works for perfect logarithms. The first number is the base and the second number is the subscript.
    *   Inputs for operator
        *   `log`
*   Solver
    *   Solver solves for an unknown variable. The first input is the coefficient of x. The second input is the number the shift in x. The third input is the what the entire equation is equal to. The final inpu is the operator that is afftects x from the shift.
    *   Inputs for opertaor
        *   `solveX`
    *  *Examples*  
        
        In this case the user is trying to create the solve for x in 2x - 44 = 33.  
        After each colon there the program asks for a user input.
            
        ```
            What operator should be used: solveX
            coefficient of x: 2
            integer: 44
            answer: 33
            opertaor: -
        ```
        
        The program repeats the equation made and gives the correct value of x to satisfy the equation.

        ```
            2.0x - 44.0 = 33.0
            38.5 