'''
A function to calculate the area of a land (acers), given its length & width (feets)
'''
def calculate_area_acres(length=None, width=None):
    if not length or not width:
        return 'No input provided'
    
    acres = (length * 1.0 * width ) / 43560
    return acres
