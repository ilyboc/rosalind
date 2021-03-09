with open("GC--Input.fasta", "r") as f:
    lines = f.readlines()
    lines.append(">dummy")
    id = ""
    max_GC_content_entry = {'id': '', 'GC_Content': 0}
    for line in lines:
        line = line.rstrip()
        if(line[0] == ">"):
            if string_len != 0:
                GC_content = GC_count*100 / string_len
                if GC_content >= max_GC_content_entry['GC_Content']:
                    max_GC_content_entry['id'] = id
                    max_GC_content_entry['GC_Content'] = GC_content
            id = line[1:]
            GC_count = 0
            GC_content = 0
            string_len = 0
        else:
            for pair in line:
                string_len += 1
                if pair == "G" or pair == "C":
                    GC_count += 1
    lines.pop()
    print(max_GC_content_entry['id'])
    print(round(max_GC_content_entry['GC_Content'],6))