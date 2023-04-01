import textwrap

def wrap(string, max_width):
    wrapper=textwrap.TextWrapper(max_width)
    line=wrapper.fill(text=string)
    return line

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)