import textwrap

def wrap(string, max_width):
    x=len(string)//max_width
    #print(x)
    d=[]
    for i in range(x+1):
        d.append( str(string[0+(i*max_width):(max_width*(i+1))]))    
    return d 
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    x=len(string)//max_width
    for i in range(x+1):
        print(result[i])
