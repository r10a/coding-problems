def rotate_matrix(mat):
    N = len(mat)

    for r in range(0, N//2): # half of the number of rows
        for c in range(r, N-r-1): # number of swaps: number of elements in each row - 1
            temp = mat[r][c] # perform 4-way swap
            
            mat[r][c] = mat[N-1-c][r]
            
            mat[N-1-c][r] = mat[N-1-r][N-1-c]
            
            mat[N-1-r][N-1-c] = mat[c][N-1-r]
            
            mat[c][N-1-r] = temp
            
    return mat
