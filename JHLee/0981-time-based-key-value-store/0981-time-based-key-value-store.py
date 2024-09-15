class TimeMap(object):

    def __init__(self):
        self.store = defaultdict(list)


    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.store[key].append([key, value, timestamp])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        lst = self.store[key]
        lp, rp = 0, len(lst) -  1
        while lp < rp:
            mid = lp + ((rp - lp) // 2)
            if lst[mid][-1] == timestamp:
                return lst[mid][1]
            elif lst[mid][-1] < timestamp:
                if mid < len(lst) and lst[mid + 1][-1] > timestamp:
                    return lst[mid][1]
                lp = mid + 1
            else:
                rp = mid - 1
        if lst[lp][-1] <= timestamp:
            return lst[lp][1]
        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)