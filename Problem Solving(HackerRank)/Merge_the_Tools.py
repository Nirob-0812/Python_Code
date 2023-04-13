from collections import OrderedDict
def merge_the_tools(string,k):
    merge=[]
    for i in range(0,len(string),k):
        merge.append(string[i:i+k])

    for i in merge:
        print("".join(OrderedDict.fromkeys(i).keys()))
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)