def main():
    s = "dracula"
    for i in range(len(s)):
        a = s[0]
        b = s[1:]
        s = b + a
    
    print(s)


main()