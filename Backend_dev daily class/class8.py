## 2D list 
book_self=[
    ["book1","book2","book3"],
    ["book4","book5","book6"],
    ["book7","book8","book9"]
]
total_row=len(book_self)
total_column=len(book_self[0])
print(book_self)
print(total_row)
print(total_column)
print(book_self[1][1])
 ## nested loop 
for i in range(total_row):
    for j in range(total_column):
        print(book_self[i][j])

        