import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print(os.path.dirname(__file__))
print(os.path.join(os.path.dirname(__file__), '..'))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))))

import ottg
