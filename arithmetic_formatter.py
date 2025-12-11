def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    top_lines = []
    bottom_lines = []
    dash_lines = []
    answer_lines = []

    for problem in problems:
        num1,operator,num2 = problem.split()
        if len(problem.split()) != 3:
            return "Error: Invalid format."
        if operator not in ['+' , '-']:
            return "Error: Operator must be '+' or '-'."
        if not (num1 and num2).isdigit:
            return "Error: Numbers must only contain digits."
        if len(num1 and num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        width = max(len(num1),len(num2)) + 2
        formatted_top = num1.rjust(width)
        formtted_bottom = operator + ' ' + num2.rjust(width - 2)
        formtted_dashes = '_' * width

        if operator ==  '+':
            result = str(int(num1) +int(num2))
        else:
            result = str(int(num1) - int(num2))
        formatted_answer = result.rjust(width)

        top_lines.append(formatted_top)
        bottom_lines.append(formtted_bottom)
        dash_lines.append(formtted_dashes)

        if show_answers :
            answer_lines.appens(formatted_answer)
    arranged = '    '.join(top_lines) + '\n' + \
               '    '.join(bottom_lines) + '\n' + \
               '    '.join(dash_lines) + '\n' 
    if show_answers:
        arranged += '\n' + '    '.join(answer_lines)

    return arranged

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')