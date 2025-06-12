from zusatzdateien.zusatz import substract_keys, bulkInsert, add_keys, print_key, print_val

dict = {"key1": 123, "key2":345, "Index":5}

dict["Add"] = 6

print (dict)

name = input('What is your name?\n')


dict = {"key1": 123, "key2":345, "Index":5}

dict.update ({"Add" : 6})

print (dict)

dict = {"key1": 123, "key2":345, "Index":5}

dict2 = {"Add" : 6}

adddict = add_keys(dict, dict2)

print (adddict)

print_key(adddict)

print_val(adddict)

f=5.5

print(f)

s= "Wert"

print(s)

print(s + str(f))

test = ["Test0", "Test2", "Test3"]

print (test)
print (test[1])

test.insert(1, "Test1")

print (test)
print (test[1])


a=1
b=1

if a==b:
    print("true")

a=None
b=None

if a==b:
    print("true : None")


a=1
b=None

if a==b:
    print("true : None1")