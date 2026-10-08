class MemorySink:
 def __init__(self):self.events=[]
 def emit(self,event):self.events.append(event);return event
