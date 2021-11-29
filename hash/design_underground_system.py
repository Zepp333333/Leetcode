class UndergroundSystem:

    def __init__(self):
        self.starts = {}
        self.ends = {}
        self.trips = {}



    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.starts[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = self.starts[id]
        if (start[0], stationName) not in self.trips:
            self.trips[start[0], stationName] = []
        self.trips[start[0], stationName].append(t - start[1])
        self.starts[id].pop()

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.trips[startStation, endStation]
        return sum(times) / len(times)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


p1 = ["checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
p2 = [[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
a1 = [None,None,None,None,None,None,14.00000,11.00000,None,11.00000,None,12.00000]


obj = UndergroundSystem()

for f, p, a in (zip(p1, p2, a1)):
    funct = obj.__getattribute__(f)
    res = funct(*p)
    print(res)
    assert res == a

p1 = ["checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"]
p2 = [[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]
a1 = [None,None,5.00000,None,None,5.50000,None,None,6.66667]


obj = UndergroundSystem()

for f, p, a in (zip(p1, p2, a1)):
    funct = obj.__getattribute__(f)
    res = funct(*p)
    print(res)
    assert res == a
