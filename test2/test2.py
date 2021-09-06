#Copyright 2021 Asink Inc

import os
for entry in os.scandir('.'):
    if entry.is_file():
        print(entry.name)
