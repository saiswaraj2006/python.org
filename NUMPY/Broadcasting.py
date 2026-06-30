#stretching the shape of an smaller array when performing the operations on bigger array
'''
RULES:
1. If shape are equal ,they're compatible.
2. If one is 1,it can be stretched to match the other.
3. If shapes are different and not 1 or equal->error.'''
#real life example is changing the brightness of the image while editing
import numpy as np
image=np.array([[200,150],
                [100,250]])
brightness=image+50
#above the broadcasting is used because for adding the 50 a scalar it should create a matrix in (2,2) then adds
print(brightness)
