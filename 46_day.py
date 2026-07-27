# os modules

import  os
# for i in range(1,47):
#      os.mkdir(f"data/{i+1}_day")

for i in range(1,100):
     os.rename(f"data/{i+1}_day",f"data/saurabh{i+1}")

# import shutil

# for i in range(48, 101):
#     shutil.rmtree(f"{i}_day.py", ignore_errors=True)