# seek(), tell() and other functions

with open('fie.txt','r') as f:
     print(type(f))
     f.seek(10)  # move to the 10th byte in the file
     print(f.tell())
     data=f.read(5)  # read next 5 bytes
     print(data)
