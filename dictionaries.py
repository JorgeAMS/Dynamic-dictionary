import random

name=""
possible_names=["Jorge","Armando","Paula","Maria","Alejandra","Andrea"]
my_dictionary= {}
previous_names=[]

array1=[]
array2=[]
array3=[]

i=0


while i < 5:
    name_selected=possible_names[random.randrange(6)]
    #print(name_selected)

    if name != name_selected:
        if name_selected in previous_names:
            array1.clear()
            array2.clear()
            array3.clear()
            get_array = my_dictionary.get(name_selected)
            print(f"Diccionary: {my_dictionary}")
            print()
            print(f"Actual directionary array: {get_array}")
            print()
            array1 = get_array[0]
            array2 = get_array[1]
            array3 = get_array[2]
            array1.append(random.randrange(154,216,1))
            array2.append(random.randrange(456,875,1))
            array3.append(random.randrange(0,5,1))
            arrays_dictionary=[array1,array2,array3]
            du = {name_selected:arrays_dictionary}
            my_dictionary.update(du)
        else:
            previous_names.append(name_selected)
            array1.clear()
            array2.clear()
            array3.clear()
            array1.append(random.randrange(154,216,1))
            array2.append(random.randrange(456,875,1))
            array3.append(random.randrange(0,5,1))
            arrays_dictionary=[array1,array2,array3]

            my_dictionary[name_selected]=arrays_dictionary
            print(f"first time of : {my_dictionary}")
            my_dictionary.update()
            #du = {name_selected:arrays_dictionary}
            #my_dictionary.update(du)
            #arrays_dictionary.clear()
            #du.clear()
        
        name=name_selected
    else:
        array1.append(random.randrange(154,216,1))
        array2.append(random.randrange(456,875,1))
        array3.append(random.randrange(0,5,1))
        arrays_dictionary=[array1,array2,array3]
        my_dictionary.update({name_selected:arrays_dictionary})
    i+=1
    #print(f"{name_selected}, Array1: {array1}, Array2: {array2}, Array3: {array3}")
    print()
    print(f"It emptys here?: {my_dictionary}")
    print()

print()
print(previous_names)
print()

"""
personal_info = { 'age':19, 'lastname':"Morales", 'zip_code':111611, 'email':"jamorales516@icloud.com", 'city':"Bogota" }


print(personal_info)
"""



#my_dictionary= {name:arrays_dictionary}