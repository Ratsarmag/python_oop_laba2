class Store:

    def __init__(self):
        self.data = {}

    def set(self, key_path: str, value: dict) -> None:
        keys = key_path.split('.')
        tmp = self.data
        for key in keys[:-1]:
            if key not in tmp:
                tmp[key] = {}
            tmp = tmp[key]
        tmp[keys[-1]] = value

    def get(self, key_path: str) -> dict:
        keys = key_path.split('.')
        tmp = self.data
        for key in keys:
            if key not in tmp:
                return None
            tmp = tmp[key]
        return tmp

    def update(self, key_path: str, updated_value: dict) -> None: 
        keys = key_path.split('.')
        tmp = self.data
        for key in keys[:-1]:
            if key not in tmp:
                return None
            tmp = tmp[key]
        tmp[keys[-1]] = updated_value

    def delete(self, key_path: str) -> None:
        keys = key_path.split('.')
        tmp = self.data
        for key in keys[:-1]:
            if key not in tmp:
                return None
        tmp = tmp[key]
        del tmp[keys[-1]]

store = Store()
store.set('key',{"a": 1, "b" : 2, "c": 3})

res = store.get('key')
print(res)

res = store.get('key.a')
print(res)

res = store.get('key.b')
print(res)

store.update("key.a", 5)
print(store.get("key.a"))

store.delete("key.a")
print(store.get("key.a"))