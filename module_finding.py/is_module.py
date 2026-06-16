import importlib
import importlib.util

# 1. Safely check if a module exists using find_spec()
# This stops your script from crashing if a library is missing
module_name = "math"
spec = importlib.util.find_spec(module_name)

if spec is not None:
    print(f" Success: Found the module blueprint for '{module_name}'!")
    
    # 2. Programmatically load it using import_module()
    # This is identical to running: import math
    my_math = importlib.import_module(module_name)
    print(f"Square root of 81: {my_math.sqrt(81)}") # Output: 9.0
else:
    print(f" Error: Could not find '{module_name}' anywhere.")

# 3. Handle live file updates using invalidate_caches()
# Run this if your code generates new script files on the fly
importlib.invalidate_caches()
print(" Finder cache cleared! Python can now see newly created files.")
'''output=
 Success: Found the module blueprint for 'math'!
Square root of 81: 9.0
 Finder cache cleared! Python can now see newly created files.
 '''

