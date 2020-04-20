text_str = "Hello, World!"
print(type(text_str))
print ( "'" + text_str + "' is a STRING ? " + str(isinstance(text_str, str)) )
print("-"*50)

numeric_int = 20
print(type(numeric_int))
print ("'" + str(numeric_int) + "' is a INTERGER ? " +str(isinstance(numeric_int, int)))
print("-"*50)

numeric_float = 20.6
print(type(numeric_float))
print ("'" + str(numeric_float) + "' is a FLOAT ? " +str(isinstance(numeric_float, float)))
print("-"*50)

numeric_complex = 1j
print(type(numeric_complex))
print ("'" + str(numeric_complex) + "' is a COMPLEX ? " +str(isinstance(numeric_complex, complex)))
print("-"*50)

sequence_list = ["apple", "banana", "cherry"]
print(type(sequence_list))
print ("'" + str(sequence_list) + "' is a LIST ? " +str(isinstance(sequence_list, list)))
print("-"*50)

sequence_tuple = ("apple", "banana", "cherry")
print(type(sequence_tuple))
print ("'" + str(sequence_tuple) + "' is a TUPLE ? " +str(isinstance(sequence_tuple, tuple)))
print("-"*50)

sequence_range = range(6)
print(type(sequence_range))
print ("'" + str(sequence_range) + "' is a RANGE ? " +str(isinstance(sequence_range, range)))
print("-"*50)


mapping_dict = {"name" : "John", "age" : 36}
print(type(mapping_dict))
print ("'" + str(mapping_dict) + "' is a DICTORARY ? " +str(isinstance(mapping_dict, dict)))
print("-"*50)

set_set = {"apple", "banana", "cherry"}
print(type(set_set))
print ("'" + str(set_set) + "' is a SET ? " +str(isinstance(set_set, set)))
print("-"*50)


set_frozenset = frozenset({"apple", "banana", "cherry"})
print(type(set_frozenset))
print ("'" + str(set_frozenset) + "' is a FROZEN SET ? " +str(isinstance(set_frozenset, frozenset)))
print("-"*50)


boolean_bool = True
print(type(boolean_bool))
print ("'" + str(boolean_bool) + "' is a BOOLEAN ? " +str(isinstance(boolean_bool, bool)))
print("-"*50)


binary_bytes = b"Hello"
print(type(binary_bytes))
print ("'" + str(binary_bytes) + "' is a BYTES ? " +str(isinstance(binary_bytes, bytes)))
print("-"*50)

binary_byteararry = bytearray(5)
print(type(binary_byteararry))
print ("'" + str(binary_byteararry) + "' is a BYTE ARRAY ? " +str(isinstance(binary_byteararry, bytearray)))
print("-"*50)

binary_memoryview = memoryview(bytes(5))
print(type(binary_memoryview))
print ("'" + str(binary_memoryview) + "' is a MEMORY VIEW ? " +str(isinstance(binary_memoryview, memoryview)))
print("-"*50)