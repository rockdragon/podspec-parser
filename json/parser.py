import json


def is_typeof(o, repr):
    return type(o).__name__ == repr


class PodSpec(object):
    def __setitem__(self, key, value):
        if key not in self.__dict__:
            self._keys.append(key)
            setattr(self, key, value)

    def __init__(self, filename):
        self._keys = []
        with open(filename, 'r') as f:
            json_dict = json.load(f)
            for k, v in json_dict.items():
                if is_typeof(v, 'dict'):
                    self[k] = self.iterate_object(v)
                else:
                    self[k] = v

    def iterate_object(self, obj):
        if is_typeof(obj, 'dict'):
            obj2 = PodSpecChild()
            for k, v in obj.items():
                obj2[k] = self.iterate_object(v)
            return obj2
        else:
            return obj

    def keys(self):
        return self._keys


class PodSpecChild(object):
    def __setitem__(self, key, value):
        if key not in self.__dict__:
            self._keys.append(key)
            setattr(self, key, value)

    def __init__(self):
        self._keys = []

    def keys(self):
        return self._keys



if __name__ == '__main__':
    podspec = PodSpec('podspec.json')
    for k in podspec.__dict__.keys():
        if is_typeof(getattr(podspec, k), 'PodSpecChild'):
            print(getattr(podspec, k).keys())
