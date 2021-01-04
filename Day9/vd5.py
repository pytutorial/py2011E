# vd5
# mô phỏng mxh
class Person:
    def __init__(self, name):
        self.name = name
        self.friendList = []
        self.requestList = []        

    def __repr__(self): return self.name

    def sendRequest(self, person):
        if self not in person.requestList:
            person.requestList.append(self)
        
    def acceptRequest(self, person):
        if person in self.requestList:
            self.requestList.remove(person)
            self.friendList.append(person)
            person.friendList.append(self)
    
    def isFriend(self, person):
        return self in person.friendList
    
    def isFriendOfFriend(self, person):
        for p in self.friendList:
            if p.isFriend(person):
                return True
        return False
    
    def getCommonFriendList(self, person):
        pass
    
a = Person('A'); b=Person('b'); c = Person('C'); d = Person('D')
a.sendRequest(b); b.acceptRequest(a)
b.sendRequest(c); c.acceptRequest(b)
print(b.friendList)                         # ['A', 'C']
print(a.isFriend(c))                        # False
print(a.isFriendOfFriend(c))                # True
print(a.isFriendOfFriend(d))                # False



        
