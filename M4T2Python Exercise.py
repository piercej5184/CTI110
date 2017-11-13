# CTI 110
# M4T2
# Pierce
# 10/2


def main():


    #ask user for string
    tag = input("Enter tag?")

    #give example of use
    #p = "<p> is the paragraph tag."
    if tag == "p" :
        print("<p> is the paragraph tag.")
        print("Example of use: <p>text</p>")
    elif tag == "h1" :
        print("<h1> is the font size tag.")
        print("Example of use: <h1>text</h1>")
    elif tag == "b" :
        print("<b> is the bold tag.")
        print("Example of use: <b>text</b>")
    elif tag == "div" :
        print("<div> is the division or a section tag.")
        print("Example of use: <div style='color:#FFFFFF'>text</div>")
    else:
        print('tag not found')

    #else print ('tag not found')
    #print("the tag is", tag)

main()
