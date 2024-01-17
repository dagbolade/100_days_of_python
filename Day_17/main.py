# creating my very first class
class User:
    # creating the constructor method which means that every time an object is created from this class,
    # the constructor method will be called

    def __init__(self, user_id, username):
        # attributes
        self.id = user_id
        self.username = username
        # adding a default value to an attribute
        self.followers = 0
        self.following = 0

    # methods
    def follow(self, user):
        # the user we are following gets one more follower
        user.followers += 1
        # when we follow a user, we get one more following
        self.following += 1


# creating an object from the User class and passing in the arguments or parameters
user_1 = User("001", "david")
user_2 = User("002", "titi")

print(user_1.id,user_1.username)
print(user_2.id,user_2.username)

# calling the follow method
user_1.follow(user_2)
user_2.follow(user_1)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)