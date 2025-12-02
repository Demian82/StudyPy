def fileIO(fileName):
    with open(fileName, 'r') as f:
        content = f.read()
    content = content.strip()
    tokens = content.split('\n')
    
    return tokens

def input_stats(fileName):
    content = fileIO(fileName)
    count = 0
    total = 0
    line_chars = []
    longest_line = 0
    longest_char = 0
    avg = 0

    for line in content:
        count +=1
        chars = len(line)
        line_chars.append(chars)
        print(f'Line {count} has {chars} chars')
    
    longest_char = max(line_chars)

    for c in line_chars:
        total += c
    
    avg = total / len(line_chars)

    print(f'{len(line_chars)} lines; longest = {longest_char}, average = {avg:.1f}')
    

input_stats("input_stats/carroll.txt")