OPERATORS = ('+', '-', '*', '/', '(', ')')

class Calculator:
    def conver_operand_to_number_and_append(self, operand: str, parsed_list: list) -> int|float:
        """
        Converts string literal to number and appends it to parsed_list
        :param operand: Operand as string to be converted:
        """
        operand = operand.replace(',', '.')
        if not operand:
            return

        if '.' in operand:
            operand = float(operand)
        else:
            operand = int(operand)
        parsed_list.append(operand)
        
        return 
    
    def preparse_expression(self, expression: str) -> list:
        """
        Preparses expression provided as string into iterable list.
        :param expression: expression to be calculated
        :returns parsed_list: expression represented as list of operands and operators.
        """
        parsed_list = []
        operand = ''
        for char in expression:
            if char in OPERATORS:
                self.conver_operand_to_number_and_append(operand, parsed_list)
                operand = ''
                parsed_list.append(char)
                continue
            elif char == '=':
                self.conver_operand_to_number_and_append(operand, parsed_list)
                operand = None
                break
            operand += char

        if operand:
            self.conver_operand_to_number_and_append(operand, parsed_list)
            
        return parsed_list
    
    def parenthesis_parser(self, parsed_expression: list) -> list:
        """
        Parses expression in order to reduce subexpressions in parenthesis
        :param parsed_expression: List of operands and operators
        :param reduced_expression: Expression in form of list without parenthesis subexpressions
        """
        
        last_open_parenthesis_idx = None
        
        for idx, element in enumerate(parsed_expression):
            if element == '(':
                last_open_parenthesis_idx = idx
            elif element == ')':
                idx_1 = last_open_parenthesis_idx
                parsed_expression[idx_1:idx+1] = [self.calculate_expression(parsed_expression[idx_1+1:idx])]
                break
        
        if last_open_parenthesis_idx:
            return self.parenthesis_parser(parsed_expression)
        else:
            return parsed_expression

    def calculate_expression(self, expression: list) -> int:
        """
        Calculates simple expression and returns it as a number:
        :param sub_expression: Subexpression to be calculated
        :returns: Result of subexpression
        """

        expression = self.multiply_and_divide(expression)
        expression = self.add_and_subtract(expression)
        return expression[0]
    
    def multiply_and_divide(self, expression: list):
        for idx, operand in enumerate(expression):
            if operand == '*':
                expression[idx-1:idx+2] = [expression[idx-1]*expression[idx+1]]
                expression = self.multiply_and_divide(expression)
            elif operand == '/':
                expression[idx-1:idx+2] = [expression[idx-1]/expression[idx+1]]
                expression = self.multiply_and_divide(expression)
        
        return expression
    
    def add_and_subtract(self, expression: list):
        """
        Performs all necessary addition and subtraction operations:
        """
        for idx, operand in enumerate(expression):
            if operand == '+':
                expression[idx-1:idx+2] = [expression[idx-1]+expression[idx+1]]
                expression = self.add_and_subtract(expression)
            elif operand == '-':
                expression[idx-1:idx+2] = [expression[idx-1]-expression[idx+1]]
                expression = self.add_and_subtract(expression)

        return expression
    
    def calculate(self, expression):
        """
        Calculates given expression.
        :param expression: Given expression
        :returns: Result of expression
        """

        list_parsed_exp = self.preparse_expression(expression)
        calc_parenthesis = self.parenthesis_parser(list_parsed_exp)
        calc_mult_div = self.multiply_and_divide(calc_parenthesis)
        calc_add_sub = self.add_and_subtract(calc_mult_div)

        return calc_add_sub[0]



    


            


