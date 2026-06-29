Python_Book = 145.45
AI_Book = 200.50
Data_Science_Book = 300.75
## first ans 
Total_Price = Python_Book + AI_Book + Data_Science_Book
print(" Total price of three books:", Total_Price)

# ans 2
Average_Price = Total_Price / 3
print(" Average price of each book:", Average_Price)

# ans 3
Python_AI_Total = Python_Book + AI_Book
print(" Price of Python Book and AI Book:", Python_AI_Total)

# ans 4
Most_Expensive = max(Python_Book, AI_Book, Data_Science_Book)
Least_Expensive = min(Python_Book, AI_Book, Data_Science_Book)
Price_Difference = Most_Expensive - Least_Expensive
print(" Difference between most and least expensive book:", Price_Difference)

### note for me-- we can use max func to find out max value 
### same as we can use min func to find out min value
