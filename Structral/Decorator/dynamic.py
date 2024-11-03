from typing import Any


class FileWithLogging:
    def __init__(self, file):
        self.file = file

    def writelines(self, strings):
        self.file.writelines(strings)
        print(f'wrote {len(strings)} lines')

    def __getattr__(self, item):
        return getattr(self.__dict__['file'], item)

    def __setattr__(self, key: str, value: Any) -> None:
        if key == 'file':
            self.__dict__[key] = value
        else:
            setattr(self.__dict__['file'], key)

    def __delattr__(self, item: str) -> None:
        delattr(self.__dict__['file'], item)


if __name__ == '__main__':
    file = FileWithLogging(open('temp.txt', 'w'))
    file.writelines(['hello', 'world'])
    file.write('\nHi, how are you?')

    file.close()
