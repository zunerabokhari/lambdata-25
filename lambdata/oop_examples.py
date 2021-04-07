"""Module 2 OOP Examples"""


class BareMinimumClass:
    pass

class Complex:
    '''
    this is a Complex class that has a real and imaginary attribute
    '''
    def __init__(self, real_part, imag_part):
        '''
        Constructor for Complex Numbers.
        '''
        self.r = real_part #Complex_Object.r == real_part
        self.i = imag_part #Complex_Object.i == imag_part

    def add(self, other_complex):
        '''
        Adds two Complex objects together!
        '''
        self.r += other_complex.r
        self.i += other_complex.i 

    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)

    

class SocialMediaUser:
    def __init__(self, name, location, upvotes=0, secondary_upvotes=1):
        self.name = name 
        self.location = location
        self.upvotes = upvotes 
        self.secondary_upvotes = secondary_upvotes
        self.total_upvotes = self.upvotes + self.secondary_upvotes

    def receive_upvotes (self, num_upvotes):
        self.upvotes += int(num_upvotes)
    
    def is_popular(self):
        return self.total_upvotes > 100 
    




 #this makes it so that everything below will only print on import if the main name of the file is typed out (python oop_examples.py) 
    #but if you dont type the main name then it wont print on import (import lambdata.oop_examples)
    #so we put all the code that we dont want to run when we import something under this condition

if __name__ == '__main__':  
    #Complex_num_1_object.r =  3
    #Complex_num_1_object.i = -5

    Complex_num_1_object = Complex(
        real_part=3,
        imag_part=-5)

    #Complex_num_2_object.r = 2
    #Complex_num_2_object.i = 6

    Complex_num_2_object = Complex(
        real_part=2,
        imag_part=6)

    Complex_num_1_object.add(Complex_num_2_object)
    print(Complex_num_1_object.r, Complex_num_1_object.i) 






