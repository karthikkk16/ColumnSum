def ColumnSum(matrix,row,column):
    res=[]
    for i in range(column):
        sum=0
        for j in range(row):
            sum+=matrix[j][i]
        res.append(sum)
    return res

matrix=[]
row=int(input("Enter number of rows : "))
column=int(input("Enter number of columns : "))
for i in range(row):
    matrix.append(list(map(int,input().split())))

print(ColumnSum(matrix,row,column))