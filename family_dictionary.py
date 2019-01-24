# Define a dictionary that contains information about several members of your family.

my_family = {
  'sister': {
      'name': 'Blondie',
      'age': 47
  },
  'mother': {
      'name': 'Mom',
      'age': 70
  },
  'father': {
      'name': 'Dad',
      'age': 70
  },
  'wife': {
      'name': 'Cutieface',
      'age': 43
  }
}

# Using a dictionary comprehension, produce output that looks like the following example.
# Krista is my sister and is 42 years old
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)


for k, v in my_family.items():
  print(f"{v['name']} is my {k} and is {v['age']} years old")

