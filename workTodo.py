from TimeManager import TimeManager
from TimeManager import Todo


td = Todo()
manager = TimeManager("tombustanBocugu.p", td)

"""t = manager.add()
manager.writeFile(t)"""
manager.list()
