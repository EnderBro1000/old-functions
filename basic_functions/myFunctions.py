def printMatrix(mat):
    out = ""
    for idxi, i in enumerate(mat):
        for idxj, j in enumerate(i):
            out += f"{mat[idxi][idxj]} "
        out += "\n"
    print(out)