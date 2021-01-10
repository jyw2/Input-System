import time

class CMD:
    """Class that holds the CMD pattern to search for in the input stream
    and the CMD priority. Each Special move has an associated CMD class"""
    def __init__(self, targetCmd, priority):
       self.targetCmd = targetCmd
       self.priority = priority

    def get_targetCmd(self):
        return self.targetCmd

    def get_priority(self):
        return self.priority


class Input_stream:
    """holds the inputs in memory for reading.
    a None value means no input"""

    def __init__(self):
        self.stream = [None]*10
        self.beg = 1
        self.end = 0
    
    def get_stream(self):
        return self.stream
        
    def add_input(self,input):
        """adds an input to the array list and shifts the
        beg and end one index to the right; triggered on user
        input"""

        self.stream[self.beg] = input
        
        "checks if the beg or end needs to wrap back around the array"
        if(self.beg == len(self.stream)-1):
            self.beg = 0
            self.end += 1
        elif(self.end == len(self.stream)-1):
            self.beg += 1
            self.end = 0
        else:
            self.beg += 1
            self.end += 1

    def push_stream(self):
        """adds a None and pushes the stream. if all elements
        in the stream are None, does nothing. Will be used to
        time out the stream over a second or so"""

        for input in (self.stream):
            if not (input == None):
                break
            return
        
        self.add_input(None)





if __name__ == "__main__":

    "Testing for adding input to the stream"
    inputStream = Input_stream()
    for x in range(10):
        print(str(inputStream.get_stream()))
        inputStream.add_input(0)
    print(str(inputStream.get_stream()))
    inputStream.add_input(1)
    print(inputStream.get_stream())
    inputStream.push_stream()
    print(inputStream.get_stream())




    