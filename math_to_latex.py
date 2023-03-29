import re
import sympy


def read_math_expressions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    expressions = [line.strip() for line in lines if line.strip()]
    return expressions


def parse_expression_and_comment(expression):
    if '#' in expression:
        expr, comment = expression.split('#', 1)
        return expr.strip(), comment.strip()
    else:
        return expression.strip(), ""

def process_expression(expr):
    x = sympy.Symbol('x')
    y = sympy.Function('y')(x)
    y_prime = y.diff(x)
    y_partial_x = y.diff(x)
    integral_y = sympy.integrate(y, x)
    processed_expr = {
        'y': y,
        'y_prime': y_prime,
        'y_partial_x': y_partial_x,
        'integral_y': integral_y
    }.get(expr, None)

    if processed_expr is None:
        raise ValueError(f"Expression '{expr}' is not recognized")

    return processed_expr


def convert_to_latex(expressions):
    latex_expressions = []
    for expression in expressions:
        try:
            expr, comment = parse_expression_and_comment(expression)
            # Replace '^' with '**' for Sympy compatibility
            expr = expr.replace('^', '**')
            # Insert explicit multiplication between a number and a variable
            expr = re.sub(r'(\d)([a-zA-Z\(])', r'\1*\2', expr)

            sympy_expr = process_expression(expr.split('=')[0].strip())
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
