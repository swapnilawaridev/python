import keyword
w=["for","three","lambda","while","number","global","string"]
for i in range (len(w)):
     if keyword.iskeyword(w[i]):
        print(w[i],"keyword in python")
     else:
        print(w[i],"not keyword in python")
