def sanitize_data(dirty_list,clean_list):
    while dirty_list:
        a=dirty_list.pop()
        a=a.strip()
        a=a.lower()
        clean_list.append(a)
raw_tags = ["  bEnCh pReSs  ", "sQuAtS", "  dEaDlIfT  "]
clean_tags = []
sanitize_data(raw_tags[:],clean_tags)
print(raw_tags)
print(clean_tags)