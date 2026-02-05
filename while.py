"""

some while loops

"""

keep_going = True
while keep_going:
    print("This is the song that never ends. \n It just goes on and on my friend")
    print("Somebody started singing it not knowing what it was")
    print("and they'll just go on singing it forever just because. ")

    somebody_stop_me = input("Keep going? y/n:   ")
    if somebody_stop_me == "y" or somebody_stop_me == "Y":
        keep_going = True
    else:
        keep_going = False
