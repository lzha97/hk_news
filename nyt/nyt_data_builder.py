import json

phl, abst, ldpg, mhl, snip = [], [], [], [], [] 

res = {} 

with open('nyt_print_headlines.txt', 'r') as rfile: 
    phl = rfile.readlines()

with open('nyt_abstracts.txt', 'r') as rfile: 
    abst = rfile.readlines() 

with open('nyt_lead_paragraphs.txt', 'r') as rfile: 
    ldpg = rfile.readlines()

with open('nyt_main_headlines.txt', 'r') as rfile: 
    mhl = rfile.readlines()

with open('nyt_snippets.txt', 'r') as rfile: 
    snip = rfile.readlines() 

if len(phl) != len(abst) != len(ldpg) != len(mhl) != len(snip): 
    print("ERROR")
    
else: 
    for i in range(len(phl)): 
        parts = [phl, abst, ldpg, mhl, snip]
        part_names = ['print_head_lines', 'abstracts', 'lead_paragraphs', 'main_head_lines', 'snippets']
        for idx in range(len(parts)): 
            part = parts[idx]
            line = part[i].split(' . ')
            key = line[0]
            if len(line) > 1:
                name = part_names[idx]
                content = line[1]
                if key not in res: 
                    res[key] = {name:content}
                else: 
                    if content not in res[key]: 
                        res[key][name] = content

with open("parsed_nyt_data.json", 'w+') as wfile: 
    wfile.write(json.dumps(res, indent=4))


