strs = "1234123"

i = 0
j = len(strs) - 1
count_dict = {}
for _ in strs:
    if _ not in count_dict:
        while(i < j):
            count = 0
            if strs[i] != strs[j]:
                j -= 1
            else:
                count += 1
        
        count_dict[strs[i]] = count
        i += 1
        
    