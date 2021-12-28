'''
A function to calculate the bmi of a person given weight and height
'''
def calculate_bmi(weight, height):    
    bmi = 703 * weight / (height)**2
    return bmi
