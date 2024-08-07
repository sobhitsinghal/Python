def add_polynomials(poly1, poly2):
    # Finding the maximum degree of the two polynomials
    degree = max(len(poly1), len(poly2))

    # Initializing result array  with zeros
    result = [0] * (degree + 1)

    # Adding corresponding terms of polynomials
    for i in range(len(poly1)):
        result[i] += poly1[i]

    for i in range(len(poly2)):
        result[i] += poly2[i]

    return result


# Given polynomials: 5 + 10x^2 + 6x^3 and 1 + 2x + 3x^2
poly1 = [5, 0, 10, 6]
poly2 = [1, 2, 3]

result = add_polynomials(poly1, poly2)

print("Resultant Polynomial Coefficients:", result)