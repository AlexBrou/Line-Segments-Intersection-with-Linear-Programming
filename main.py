from pulp import LpProblem, lpSum, LpMinimize, LpVariable, LpInteger, LpStatus, value


def main(l1, l2, segments=False, printResult=True):

    prob = LpProblem("Line Segments intersection", LpMinimize)

    xLeftBorder, xRightBorder = None, None
    if segments:
        xLeftBorder = max([l1[2], l2[2]])
        xRightBorder = min([l1[3], l2[3]])

    x = LpVariable("x",
                   xLeftBorder,
                   xRightBorder,
                   )

    y = LpVariable("y",
                   None,
                   None,
                   )

    prob += 0, "arbitrary objective"

    prob += x*l1[0] + l1[1] == x*l2[0] + l2[1]

    prob += (y - l1[1])/l1[0] == (y - l2[1])/l2[0]

    prob.solve()

    if printResult:
        print("Status:", LpStatus[prob.status])

        if LpStatus[prob.status] == "Optimal":
            return x.value(), y.value()

    return None


if __name__ == "__main__":
    l1 = (1, 1, 1, 9)  # coef, z , minX , maxX
    l2 = (0.5, 2, 3, 6)  # coef, z , minX, maxX
    result = main(l1, l2)  # considering the input to be lines
    print("RESULT: ", result)
    # considering the input to be line segments
    result = main(l1, l2, segments=True)
    print("RESULT: ", result)
