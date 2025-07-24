def rangeResolver(part,customDelimeters):
    part = part.strip()
    for delimeter in customDelimeters:
        if delimeter in part:
            start, end = part.split(delimeter)
            start = int(start)
            end = int(end)
            return list(range(start, end + 1))
    else:
        return [int(part)]

    
    

def expander(s,customDelimeters):
    result = []
    s = s.strip()
    parts = s.split(',')
    
    for part in parts:
        if(part != ''):
            result.extend(rangeResolver(part,customDelimeters))
    return result

input_str = "3-1,5,7~9,,  "
output = expander(input_str,['-','~'])
print(output)