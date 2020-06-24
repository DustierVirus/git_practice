def show_result(matrix):
    print('The result is: ')
    for ro in matrix:
        print(' '.join(str(elem) for elem in ro))


def matrix_n_by_n_determinant(nb_rows, nb_cols, matrix):
    if nb_rows != nb_cols:
        return 'ERROR'
    else:
        if nb_rows == 1:
            return matrix[0][0]
        if nb_rows == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            determinant = 0
            for i in range(nb_rows):
                minor = [[matrix[_][j] for j in range(nb_cols) if j != i] for _ in range(1, nb_rows)]
                determinant += matrix[0][i] * matrix_n_by_n_determinant(nb_rows - 1, nb_cols - 1, minor) * (-1)**(1+i+1)
            return determinant


def sum_(a, b, matrix_1, m, n, matrix_2):
    if a == m and b == n:
        for i in range(a):
            for j in range(b):
                matrix_1[i][j] += matrix_2[i][j]
        return matrix_1
    else:
        print('ERROR')


def mult_constant(a, b, matrix_1, constant):
    for i in range(a):
        for j in range(b):
            matrix_1[i][j] *= constant
    return matrix_1


def mult(a, b, matrix_1, m, n, matrix_2):
    if b != m:
        print('ERROR')
    else:
        lst_intermediate_values = []
        lst_values = []
        matrix_3 = [[int(k) for k in range(n)] for i in range(a)]
        for times in range(a):
            for col in range(n):
                for row in range(m):
                    lst_intermediate_values.append(matrix_1[times][row] * matrix_2[row][col])
                lst_values.append(sum(lst_intermediate_values))
                lst_intermediate_values = []
        q = 0
        for row in range(a):
            for col in range(n):
                matrix_3[row][col] = lst_values[q]
                q += 1
        return matrix_3


def main_diagonal(a, b, matrix_1):
    matrix_2 = [[float(k) for k in range(a)] for i in range(b)]
    for i in range(a):
        for j in range(b):
            matrix_2[j][i] = matrix_1[i][j]
    return matrix_2


def side_diagonal(a, b, matrix_1):
    matrix_2 = [[int(k) for k in range(a)] for i in range(b)]
    for i in range(a):
        for j in range(b):
            matrix_2[b-(j+1)][a-(i+1)] = matrix_1[i][j]
    return matrix_2


def vertical_line(a, b, matrix_1):
    matrix_2 = [[int(k) for k in range(b)] for i in range(a)]
    for i in range(a):
        for j in range(b):
            matrix_2[i][j] = matrix_1[i][b-int((j+1))]
    return matrix_2


def horizontal_line(a, b, matrix):
    matrix_2 = [[int(k) for k in range(b)] for i in range(a)]
    for i in range(a):
        for j in range(b):
            matrix_2[i][j] = matrix_1[a-int((i+1))][j]
    return matrix_2


def get_cofactrix(nb_rows, nb_cols, matrix):
    q = 0
    lst_cofactors = []
    cofactrix = [[int(k) for k in range(nb_cols)] for j in range(nb_rows)]
    if nb_rows == 1:
        return matrix
    if nb_rows == 2:
        matrix = [[matrix[1][1], -matrix[1][0]], [-matrix[0][1], matrix[0][0]]]
        return matrix
    else:
        for k in range(nb_rows):
            for i in range(nb_cols):
                minor = [[matrix[_][j] for j in range(nb_cols) if j != i] for _ in range(nb_rows) if _ != k]
                cofactor = matrix_n_by_n_determinant(nb_rows-1, nb_cols-1, minor) * (-1) ** (k+1+i+1)
                lst_cofactors.append(cofactor)
        for row in range(nb_rows):
            for col in range(nb_cols):
                cofactrix[row][col] = lst_cofactors[q]
                q += 1
        return cofactrix


def get_inverse(a, b, matrix_1):
    if a != b:
        return 'ERROR'
    elif matrix_n_by_n_determinant(a, b, matrix_1) == 0:
        return 'ERROR'
    else:
        return mult_constant(a, b, main_diagonal(a, b, get_cofactrix(a, b, matrix_1)), matrix_n_by_n_determinant(a, b, matrix_1)**(-1))


print('1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose Matrix\n'
      '5. Calculate a determinant\n6. Inverse matrix\n0. Exit')
option = input('Your choice: ')
while option != '0':

    if option == '1':       # SUM
        a, b = [int(k) for k in input('Enter matrix size: ').split()]
        matrix_1 = [[float(k) for k in input('Enter matrix: ').split()] for r in range(a)]
        m, n = [int(k) for k in input('Enter matrix size: ').split()]
        matrix_2 = [[float(k) for k in input('Enter matrix: ').split()] for r in range(m)]
        print(show_result(sum_(a, b, matrix_1, m, n, matrix_2)))

    elif option == '2':     # MULTIPLICATION BY CONSTANT
        a, b = [int(k) for k in input('Enter matrix size: ').split()]
        matrix_1 = [[float(k) for k in input('Enter matrix: ').split()] for r in range(a)]
        constant = float(input('Enter constant: '))
        print(show_result(mult_constant(a, b, matrix_1, constant)))

    elif option == '3':     # MULTIPLICATION BY MATRICES
        a, b = [int(k) for k in input('Enter matrix size: ').split()]
        matrix_1 = [[float(k) for k in input('Enter matrix: ').split()] for r in range(a)]
        m, n = [int(k) for k in input('Enter matrix size: ').split()]
        matrix_2 = [[float(k) for k in input('Enter matrix: ').split()] for r in range(m)]
        print(show_result(mult(a, b, matrix_1, m. n, matrix_2)))

    elif option == '4':         # TRANSPOSITION
        print('1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line')
        choice = input(' Your choice: ')

        if choice == '1':     # MAIN DIAGONAL
            a, b = [int(k) for k in input('Enter matrix size: ').split()]
            matrix_1 = [[float(k) for k in input('Enter matrix: ').split()] for r in range(a)]
            print(show_result(main_diagonal(a, b, matrix_1)))

        elif choice == '2':       # SIDE DIAGONAL
            a, b = [int(k) for k in input('Enter matrix size: ').split()]
            matrix_1 = [[float(k) for k in input('Enter matrix: ').split()] for r in range(a)]
            print(show_result(side_diagonal(a, b, matrix_1)))

        elif choice == '3':       # VERTICAL LINE
            a, b = [int(k) for k in input('Enter matrix size: ').split()]
            matrix_1 = [[float(k) for k in input('Enter matrix: ').split()] for r in range(a)]
            print(show_result(vertical_line(a, b, matrix_1)))

        elif choice == '4':       # HORIZONTAL LINE
            a, b = [int(k) for k in input('Enter matrix size: ').split()]
            matrix_1 = [[float(k) for k in input('Enter matrix: ').split()] for r in range(a)]
            print(show_result(horizontal_line(a, b, matrix_1)))

    elif option == '5':
        a, b = [int(k) for k in input('Enter matrix size: ').split()]
        matrix_1 = [[float(k) for k in input('Enter matrix: ').split()] for r in range(a)]
        print(matrix_n_by_n_determinant(a, b, matrix_1))

    elif option == '6':
        a, b = [int(k) for k in input('Enter matrix size: ').split()]
        matrix_1 = [[float(k) for k in input('Enter matrix: ').split()] for r in range(a)]
        print(show_result(get_inverse(a, b, matrix_1)))

    else:
        print('Invalid Input')

    option = input('Your choice: ')
