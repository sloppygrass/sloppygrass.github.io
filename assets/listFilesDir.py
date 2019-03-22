import os
root_dir = "./articles"
file_set = set()
directory_set= set()

for dir_, _, files in os.walk(root_dir):
    if os.path.relpath(dir_, root_dir) != ".":
      directory_set.add(os.path.relpath(dir_, root_dir))
    for file_name in files:
        rel_dir = os.path.relpath(dir_, root_dir)
        rel_file = rel_dir + "\\\\" + file_name
        file_set.add(rel_file)

f = open("files_list.json", "w")
f.write("{\"categories\" : [ \"")
f.write("\",\"".join(str(s) for s in directory_set))
f.write("\"],")
f.write("\"files\" : [\"")
f.write("\",\"".join(str(s) for s in file_set))
f.write("\"]")
f.write("}")
