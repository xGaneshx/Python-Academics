def fruits(fruitno):
    switcher ={
        0:"apple",
        1:"orange",
        2:"banana"
    }
    
    return switcher.get(fruitno,"invalid fruit")
print(fruits(0))

