class Signal:
    def __init__(self):
        self.listners = []
        
    def connect(self, func):
        self.listners.append(func)

    def emit(self, *args, **kwargs):
        for func in self.listners:
            func(*args, **kwargs)

#this will be for updating gui not transfering outside data!