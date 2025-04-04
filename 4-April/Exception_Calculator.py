def calculator(a, b, operator):
    """
    Performs a calculation based on the given operator.
    
    :param a: First number (int/float)
    :param b: Second number (int/float)
    :param operator: String representing an operation (+, -, *, /, %, **)
    :return: Computed result or error message
    """
    try:
        if operator=="+":
            return a+b
        if operator=="-":
            return a-b
        if operator=="*":
            return a*b
        if operator=="/":
            return a/b
        if operator=="%":
            return a%b
        if operator=="**":
            return a**b
    

    except ZeroDivisionError as e:
        print("Error",e)
    except ValueError as e:
        print("Error",e)
    except TypeError as e:
        print("Error",e)
    except Exception as e:
        print("Error",e)

    else:
        print("no error")

# Example Usage:
print(calculator(10, 0, "/"))  # Should return: "Error: Division by zero"
print(calculator(10, "five", "+"))  # Should return: "Error: Invalid input type"
print(calculator(10, 5, "$"))  # Should return: "Error: Unsupported operator"
