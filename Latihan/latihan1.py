def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        return eval_operator(operator, tree(left_operand), tree(right_operand))


def eval_operator(operator, left_operand, right_operand):
    if operator == '+':
        return add(left_operand, right_operand)
    elif operator == '-':
        return minus(left_operand, right_operand)
    elif operator == '*':
        return mult(left_operand, right_operand)
    elif operator == '/':
        return div(left_operand, right_operand)


# Fungsi penjumlahan
def add(left_operand, right_operand):
    return left_operand + right_operand


# Fungsi pengurangan
def minus(left_operand, right_operand):
    return left_operand - right_operand


# Fungsi perkalian
def mult(left_operand, right_operand):
    return left_operand * right_operand


# Fungsi pembagian
def div(left_operand, right_operand):
    if right_operand == 0:
        return "Tidak bisa dibagi oleh 0"
    return left_operand / right_operand


expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))
result = tree(expression_tree)

print("Hasil evaluasi pohon ekspresi: ", result)