class Biography:
    # instantiation with full biography
    def __init__(self, name = "", birth = "", address = "", bio = ""):
        self.name = name
        self.birth = birth
        self.address = address
        self.bio = bio
        
    
    def incomplete(self):
        blank = ""
        if self.name == blank or self.birth == blank or self.address == blank or self.bio == blank:
            return True

    def createBio(self):
        print("Please enter your")
        self.name = input("Name: ")
        self.birth = input("Date of Birth: ")
        self.address = input("Address: ")
        self.bio = input("Bio: ")

    def printBio(self):
        if self.incomplete():
            print("Bio is incomplete")
        else:
            print("{}'s bio:\n\tDate of birth: {}\n\tAddress: {}\n\tBio: {}".format(self.name, self.birth, self.address, self.bio))


input("Would you like to make a new bio?")
newBio = Biography()
# newBio.createBio()
newBio.printBio()