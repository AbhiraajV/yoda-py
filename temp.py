def rangeResolver(part):
    if '-' in part:
        start, end = part.split('-')
        start = int(start)
        end = int(end)
        return list(range(start, end + 1))
    else:
        return [int(part)]

    
    

def expander(s):
    result = []
    parts = s.split(',')
    
    for part in parts:
        result.extend(rangeResolver(part))
    return result

input_str = "1-3,5,7-9"
output = expander(input_str)
print(output)