wining_number=int(input("Enter number here:"))
gused_number=int(input("Enter gussed number:"))
if gused_number==wining_number:
    print("YOU WIN !!!!")
if gused_number!=wining_number:
    if gused_number<wining_number:
        print("too low")
    if gused_number>wining_number:
        print("too high")
    else:
        print("error")
                