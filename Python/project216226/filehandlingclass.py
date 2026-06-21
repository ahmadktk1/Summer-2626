import json
class File:
    def __init__(self,):
        pass
    def savefile(filename,extension,data):
        """
        __Summary__:
            This file saves data in given file 
        Parameter:
            filename:
                    filename + extension e.g data.json , journel.txt
            data:
                    the data you want to save in file
        """
        if extension.lower() == "json":
            with open(f"{filename}.{extension}","w") as f:
                data = json.dumps(data)
                f.write(data)
        else:
            with open(f"{filename}.{extension}",'w') as f:
                f.write(data)
        return "File Saved Successfully"

    def loadfile(filename,extension):
        """
        __Summary__:
            This file load data from given file and store it in variable
        Parameters:
            filename:
                fiel name + its extension
        """
        with open(f"{filename}.{extension}", 'r') as f:
            if extension == "json":
                data = json.load(f)
            else:
                data = f.read()
        return data
