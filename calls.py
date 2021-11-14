class Calls:
    _time = 0
    _src = 0
    _dest = 0
    _invalid = 0
    _id = 0
    def __init__(self, arr):
        try:
            self._time = float (arr[1])
            self._src =  int (arr[2])
            self._dest = int (arr[3])
            self._invalid = arr[4]
            self._id = int(arr[5])
            if (self._src < self._dest):
                self._type = 1
            else:
                self._type = -1
        except:
            print("Invalid call, size out of boundaries")

    def __str__(self):
        return f""

    @property
    def src(self):
        return self._src

    @property
    def dest(self):
        return self._dest


