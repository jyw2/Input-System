import time

class CMD:
    """Class that holds the CMD pattern to search for in the input stream
    and the CMD priority. Each Special move has an associated CMD class"""
    def __init__(self, targetCmd, priority):
       self.targetCmd = targetCmd
       self.priority = priority

    def get_targetCmd(sekf):
        return self.targetCmd

    def get_priority(self):
        return self.priority


class Input_stream:
    """holds the inputs in memory for reading.
    a null value means no input"""

    def __init__(self):
        self.stream = [null]*10
        self.beg = 1
        self.end = 0
        
    def add_input(self,input):
        """adds an input to the array list and shifts the
        beg and end one index to the right; triggered on user
        input"""

        self.stream[self.beg] = input
        
        "checks if the beg or end needs to wrap back around the array"
        if(beg == len(self.stream)):
            beg = 0
            end += 1
        elif(end == len(self.stream)):
            beg += 1
            end = 0
        else:
            beg += 1
            end += 1



if __name__ == "__main__":
    inputStream = Input_stream()
    print(inputStream)


    