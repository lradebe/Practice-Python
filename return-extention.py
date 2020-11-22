def return_extension(filename):
    """This function takes a filename given by user and returns its extention"""

    extension = filename.split(".")
    print("The file name is :", filename)
    print(f"\nThe extension is : {repr(extension[-1])}")

return_extension("Hello_world!.py")
