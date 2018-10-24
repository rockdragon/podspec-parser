import json


class PodSpec(object):
    def __setitem__(self, key, value):
        setattr(self, key, value)


class PureObject(object):
    def __setitem__(self, key, value):
        setattr(self, key, value)


def _typeof(o, repr):
    return type(o).__name__ == repr


def iterate_object(obj):
    if _typeof(obj, 'dict'):
        obj2 = PureObject()
        for k, v in obj.items():
            obj2[k] = iterate_object(v)
    else:
        return obj


def main():
    with open('podspec.json', 'r') as f:
        json_dict = json.load(f)
        result = PodSpec()
        for k, v in json_dict.items():
            if _typeof(v, 'dict'):
                result[k] = iterate_object(v)
            else:
                result[k] = v

            print(k, v, type(v))

        print(dir(result))


if __name__ == '__main__':
    main()
