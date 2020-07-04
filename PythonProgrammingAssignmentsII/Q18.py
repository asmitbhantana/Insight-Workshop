"""
18. Find a package in the Python standard library for dealing with
JSON. Import the library module and inspect the attributes of the
module. Use the help function to learn more about how to use the
module. Serialize a dictionary mapping 'name' to your name and 'age'
to your age, to a JSON string. Deserialize the JSON back into
Python.
"""

import json

usr_dict = {"name": "Asmit Bhantana", "age": "22"}


# encoding json

# custom way
class NameAndAgeEncoder(json.JSONEncoder):
    def default(self, my_dict):
        return f"'name':'{my_dict['name']},'age':'{my_dict['age']}'"


usr_encoded_string = json.dumps(usr_dict, cls=NameAndAgeEncoder)
print("Encoding user string my way\n",usr_encoded_string)

# default way
print("Encoding user string default way\n",json.dumps(usr_dict))

# decoding json

# default way
my_decoder = json.JSONDecoder()
usr_decoded_string = my_decoder.decode(s=usr_encoded_string)
print("Decoding my string default way\n",usr_decoded_string)


# custom way
def decode_user_name_and_age(usr_encoded_string):
     usr_encoded_string['__custom__'] = True
     return usr_encoded_string


usr_decoded_string = json.loads(usr_encoded_string, object_hook=decode_user_name_and_age)
print("Decoding my string custom way\n",usr_decoded_string)
