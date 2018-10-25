import json


class PodSpec(object):
    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __init__(self, filename):
        with open(filename, 'r') as f:
            json_dict = json.load(f)
            for k, v in json_dict.items():
                if _typeof(v, 'dict'):
                    self[k] = iterate_object(v)
                else:
                    self[k] = v


class PodSpecChild(object):
    def __init__(self):
        self._keys = []

    def keys(self):
        return self._keys

    def __setitem__(self, key, value):
        if key not in self.__dict__:
            self._keys.append(key)
            setattr(self, key, value)


def _typeof(o, repr):
    return type(o).__name__ == repr


def iterate_object(obj):
    if _typeof(obj, 'dict'):
        obj2 = PodSpecChild()
        for k, v in obj.items():
            obj2[k] = iterate_object(v)
        return obj2
    else:
        return obj


if __name__ == '__main__':
    podspec = PodSpec('podspec.json')
    for k in podspec.__dict__.keys():
        if _typeof(getattr(podspec, k), 'PodSpecChild'):
            print(getattr(podspec, k).keys())

