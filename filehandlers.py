def process_text(filename):
    lines = """
    1. I am honestly glad to be doing power learn project
    2. I am a lady who is so inlove with tech
    3. File handling is one thing I love so much
    4. So good to be alive in an era where tech is just a thing
    5. Well lokking forward to completing my PLP Course
    """
    try:
        with open(filename, "w") as file:
            file.writelines(lines)
            print("Lines written sussefully")
    except FileNotFoundError:
        print("File was not saved successfully")
    finally:
        file.close()

def read_contents(filename):
    contents = []
    try:
        with open(filename, "r") as obFile:
            for line in obFile:
                contents = obFile.read().split()
            for ps , con in enumerate(contents):
                contents[ps] = con.upper()
            counted = len(contents)
    except FileNotFoundError:
        print("File was not found")
    finally:
        obFile.close()

    return contents, counted

def save_out_put(filename, output_file , contents):
    try:
        file = open(output_file , "w")
        file.write("Capitilized Content \n")
        for i in contents:
            file.write(i + " ")
        file.write(" \n")
        print("Line written successfully ! \n")
        file.write("Word count \n__")
        file.write(str(len(contents)))
    except FileExistsError:
        print("File exists !")
    finally:
        file.close()

def main():
    filename = "input.txt"
    output_file = "output.txt"
    procesee = process_text(filename)
    contents = read_contents(filename)[0]
    save_out_put(filename , output_file , contents)

if __name__ == "__main__":
    main()
