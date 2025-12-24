def brandInput(): 
    Brand = input("Insert car brand: ")
    if Brand.isnumeric() or Brand in "":
        print ("Invalid input, please enter a valid car brand.")
    elif Brand == "Ford":
        print ("BASED!") 
    return Brand
        

def modelInput():
    Model = input("Insert car model: ") 
    if Model.isnumeric() or Model in "":
        print ("Invalid input, please enter a valid car model.")
    return Model
     

def main():
    print ("Program starting.")
    brand = brandInput()
    model = modelInput()
    print (f"Car brand is {brand} and the model is {model}.")
    return None

if __name__ == "__main__":
    main()
    print ("Program ending.")
