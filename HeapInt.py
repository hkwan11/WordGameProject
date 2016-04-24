'''
 A class for heap elements with integer keys and handles.
 The handle is an integer initialized to zero, and the key
 is initialized to an argument.

 Objects put into your heap with handles must have a key and a handle,
 and methods getHandle(), setHandle(), getKey(), and setKey().
'''

class HeapInt:

    def __init__(self, inInt):
        self.handle = 0;
        self.key = inInt

    def __repr__(self):
        return 'key: ' + str(self.getKey()) + '; handle: ' + str(self.getHandle()) 

    def getKey(self):
        return self.key

    def setHandle(self, inHandle):
        self.handle = inHandle

    def setKey(self, inInt):
        self.key = inInt

    def getHandle(self):
        return self.handle


