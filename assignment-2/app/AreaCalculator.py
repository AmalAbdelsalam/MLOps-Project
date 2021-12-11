'''
A function to calculate the area of a land (acers), given its length & width (feets)
'''
def calculate_area_acres(length, width):    
    acres = (length * 1.0 * width ) / 43560
    return acres
