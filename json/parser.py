import json


class PodSpec(object):
    def __setitem__(self, key, value):
        setattr(self, key, value)


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


def get_pod_spec():
    result = PodSpec()
    with open('podspec.json', 'r') as f:
        json_dict = json.load(f)
        for k, v in json_dict.items():
            if _typeof(v, 'dict'):
                result[k] = iterate_object(v)
            else:
                result[k] = v
    return result


if __name__ == '__main__':
    podspec = get_pod_spec()
    for k in podspec.__dict__.keys():
        if _typeof(getattr(podspec, k), 'PodSpecChild'):
            print(getattr(podspec, k).keys())


