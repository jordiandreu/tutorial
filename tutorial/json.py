import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# Convert to json
def run_dump_to_json():
    personJSON = json.dumps(person, indent=4, sort_keys=True)
    print(personJSON)

    with open("person.json", "w") as f:
        json.dump(person, f, indent=4)

    new_person = json.loads(personJSON)
    print(new_person)

    with open("person.json", "r") as f:
        new_person = json.load(f,)
        print(new_person)

def run_user():
    class User:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    user = User("Max", 27)

    # Serialize an object to JSON

    # Option 1
    def encode_user(o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        else:
            raise TypeError('Object if not serializable')

    userJSON = json.dumps(user, default=encode_user)
    print(userJSON)

    # Option 2
    from json import JSONEncoder

    class UserEncoder(JSONEncoder):
        def default(self, o):
            if isinstance(o, User):
                return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
            return JSONEncoder.default(self, o)

    userJSON = json.dumps(user, cls=UserEncoder)
    print(userJSON)

    # Option 3
    userJSON = UserEncoder().encode(user)
    print(userJSON)

    # Create object from JSON
    # Doing this just recovers a dictionary
#    user = json.loads(userJSON)
#    print(type(user))

    # Option 1
    def decode_user(dct):
        if User.__name__ in dct:
            return User(name=dct["name"], age=dct["age"])
        return dct

    user = json.loads(userJSON, object_hook=decode_user)
    print(type(user))
    print(user.name)

    # Option 2
    from json import JSONDecoder

    class UserDecoder(JSONDecoder):
        def decode(self, dct):
            print(type(dct), "***")
            if "User" in dct:
                return User(name=dct[0], age=dct[1])
            return JSONDecoder.decode(self, dct)

    user = json.loads(userJSON, cls=UserDecoder)
    print("Option 2")
    print(type(user))
    print(user.name)

    # Option 3
    print("Option 3")
    user = UserDecoder().decode(userJSON)
    print(type(user))
    print(user.age)

