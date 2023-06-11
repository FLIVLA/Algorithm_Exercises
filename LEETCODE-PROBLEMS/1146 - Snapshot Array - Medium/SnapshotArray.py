class SnapshotArray(object):
    
    def __init__(self, length):
        self.arr = [0 for _ in range(length)]
        self.ids = []
    
    def set(self, index, val):
        self.arr[index] = val
    
    def snap(self):
        snap = self.arr[:]
        self.ids.append(snap)
        return len(self.ids) - 1
    
    def get(self, index, snap_id):
        return self.ids[snap_id][index]

class SnapshotArray_2(object):
    def __init__(self, length):
        self.length = length
        self.arr = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0
    
    def set(self, index, val):
        if self.arr[index][-1][0] == self.snap_id:
            self.arr[index][-1] = (self.snap_id, val)
        else:
            self.arr[index].append((self.snap_id, val))
    
    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1
    
    def get(self, index, snap_id):
        if snap_id >= self.snap_id:
            snap_id = self.snap_id - 1
        values = self.arr[index]
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] == snap_id:
                return values[mid][1]
            elif values[mid][0] < snap_id:
                left = mid + 1
            else:
                right = mid - 1
        return values[right][1] if right >= 0 else 0
    

sa = SnapshotArray_2(9)
sa.set(0, 15)
sa.snap()
sa.set(0, 6)
print(sa.get(0, 0))