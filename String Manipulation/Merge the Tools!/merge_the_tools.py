def merge_the_tools(string, k):
    size = len(string)
    t = ""
    for i in range(0, size, k):
        t = string[i:i+k]
        u = ""
        for j in t:
            if j not in u:
                u += j
        print(u)
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
