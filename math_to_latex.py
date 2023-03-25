import re
import sympy


def read_math_expressions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    expressions = [line.strip() for line in lines if line.strip()]
    return expressions
def parse_expression_and_comment(expression):
    parts = expression.split('#')
    expr = parts[0].strip()
    comment = parts[1].strip() if len(parts) > 1 else ''
    return expr, comment

def convert_to_latex(expressions):
    latex_expressions = []
    for expression in expressions:
        try:
            expr, comment = parse_expression_and_comment(expression)
            # Replace '^' with '**' for Sympy compatibility
            expr = expr.replace('^', '**')
            # Insert explicit multiplication between a number and a variable
            expr = re.sub(r'(\d)([a-zA-Z\(])', r'\1*\2', expr)
            # Replace derivatives, partial derivatives, and integrals with proper syntax
            expr = (
                expr.replace("partial", "diff")
                .replace("prime", "'")
                .replace("integrate", "Integral")
            )
            if '=' in expr:
                lhs, rhs = expr.split('=')
                if '(' in lhs and ')' in lhs:
                    # Handle function definition
                    func_var, arg = lhs.split('(')
                    arg = arg.strip(')')
                    sympy_func = sympy.Function(func_var)(sympy.Symbol(arg))
                    sympy_rhs = sympy.sympify(rhs)
                    sympy_expr = sympy.Eq(sympy_func, sympy_rhs)
                else:
                    # Handle equations
                    sympy_expr = sympy.Eq(sympy.sympify(lhs), sympy.sympify(rhs))
            else:
                # Handle expressions
                sympy_expr = sympy.sympify(expr)
            latex_code = sympy.latex(sympy_expr)
            latex_code = latex_code.replace('log', 'ln')  # Replace 'log' with 'ln'
            latex_expressions.append(latex_code)
        except Exception as e:
            print(f"Error converting expression '{expression}': {str(e)}")
    return latex_expressions



def create_markdown(latex_expressions, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for latex_expr in latex_expressions:
            file.write(f'$$\n{latex_expr}\n$$\n\n')

def main(input_file='expressions.txt', output_file='output.md'):
    expressions = read_math_expressions(input_file)
    latex_expressions = convert_to_latex(expressions)
    create_markdown(latex_expressions, output_file)

if __name__ == "__main__":
    main()
