import os

# print os.path.realpath(__file__)
# print os.path.dirname(__file__)
# print os.path.basename(__file__)
# print os.listdir("blog")
# print os.path.dirname("blog")

for root, dirs, files in os.walk('blog'):
    for file in files:
        print('{}/{}',root, file)
    # print(root)
    # # print(dirs)
    # print(files)