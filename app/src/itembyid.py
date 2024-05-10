# to call the item by the id from the csv file
from ..ui.mainbill import AddItem
from ..globals import GLOBAL


class Out:
    def __init__(self):
        def output():
            ai=AddItem()
            id=ai.in_ids.get()
            print(id)
        GLOBAL['id']=self
