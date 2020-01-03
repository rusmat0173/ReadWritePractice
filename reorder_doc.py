""" Idea is to reverse my original Python blog file (in MSWord)
    and change it to a txt file that I can reformat in MSWord

    N.B. I have changed the file to write to, so that you don;t overwrite!

 """
with open("Python blog.txt", "r") as f:
    all_text = f.readlines()

temp_last = len(all_text) - 1
i = len(all_text) - 1
for line in all_text[::-1]:
    if "Blog number" in line:
        # print(i, line)
        temp_first = i
        temp_dump = (all_text[temp_first:temp_last])
        print(temp_dump)
        with open("foo.txt", "a") as g:
            for line in temp_dump:
                g.writelines(line)
        temp_last = i-1
    i -= 1

