def get_initials():
    fullname= input ("What is your full name?")
    initials = ("")
    names = fullname.split()
    for name in names:
        initials = initials + name[0]
    return initials.upper()
