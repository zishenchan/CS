'''
object-oriented programming, use data and function encapsulate into objects

only when you create instances of this object, you access those data and functions

by using 'class' you can define any type of object, and create attibutes which are data belong to this object

class is a particular type of objects

class be like the blueprint of house, it contains windows, floors, etc. these are attributes 

'''


class beach: # we define a class 'beach', type of object i.e. -Beijing beach, -sydney beach...
    location = 'Sydney' # thoes are attributes of this class, i.e. 'beach'-location -view -popularity -weather...
    # on underneath definition 

# creat instance of object
sydney_beach = beach() # this variable 'sydney_beach' is belonged to class beach, and is assigned by class beach
print(sydney_beach.location) # we output this variable, and one particular attribute of this variable which is belonged to class

# we typcally not use default attributes assigned to object, we do initialization
class desktop:
    # all the instance of this type of objects, refer to instance 'self'.
    def __initi__(self,location): # usually need 'self' as first parameter, pretend doesn't exist
        self.location = location
        # first location is attributes of class 'desktop', second location is assigned through parameter 
        # second 'location' parameter is assigned by function call 'czs'

czs_desktop = desktop('czs')
other_desktop = desktop('other')
print(czs_desktop.location,other_desktop.location) # print the object czs_desktop's location
    


        


