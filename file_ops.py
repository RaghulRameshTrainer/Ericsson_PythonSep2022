"""
mode:
====
r -> read -> to open the file in read mode to read the file. Will get the FileNotFoundError
            if file does not exists.
w -write -> Open to file to write. IF the file is there it will clean up the content of the file
            and start writing as a new file. IF the file is not there then it will create
            and write into it
a - append -> Append mode. if the file exists then it will continue to write along with existing
            content. if the file is not there , it will create and write into it
r+ -> read and write -> Read the file content and start writing into it.
w+ -> write and read -> write and read

READ:
====
read(), readline(), readlines()

WRITE:
=====
write(), writelines()
"""

# with open("days.txt","r") as fo:
#     #print(fo.read())
#     # print(fo.readline(),end='')
#     # print(fo.readline())
#     print(fo.readlines())

# with open("tech.txt","w") as obj:
#     #obj.write("PYTHON")
#     obj.writelines(["PYTHON\n","SPARK\n","JAVA\n","TABLEAU\n","MONGO"])

# with open("tech.txt","a") as fo:
#     fo.writelines(["\nORACLE\n","AIML\n","CLOUD"])

# with open("newtech.txt","a") as fo:
#     fo.writelines(["ORACLE\n","AIML\n","CLOUD"])

# with open("tech.txt","r+") as fo:
#     print(fo.read())
#     fo.write("\n===============END OF THE LINE================")

# with open("tech.txt","r+") as fo:
#     fo.write("ERICSSON")
#     print(fo.read())

with open("tech.txt","w+") as fo:
    fo.writelines(["India\n","Europe\n","Australia\n","Canada\n","China\n","Rushya"])
    fo.seek(0,0)
    print(fo.read())