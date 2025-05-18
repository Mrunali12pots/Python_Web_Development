

import sys
import os
projectroot = os.path.join(os.path.dirname(__file__),'..')
print(projectroot)
sys.path.insert(0, projectroot)
print(sys.path)