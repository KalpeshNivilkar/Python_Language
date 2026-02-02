my_dict = {
    "name":"kalpesh",
    "age": 22,
    "add":"Pune",
    "family":{
        "father":"subhash",
        "mother":"kashi",
        "brother":"adi",
        "sister":"ashu"

    }
}
# to print dict 
print(my_dict)
# to get all data in list 
print(list(my_dict))
# to get only keys 
print(my_dict.keys())
# to get only values 
print(my_dict.values())
# use of get method 
print(my_dict.get("family"))
# to update dict 
my_dict.update({"name":"rashi"})
print(my_dict)

