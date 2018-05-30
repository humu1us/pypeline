class VarDrawer:
    def __init__(self):
        self._container = {}

    def set_var(self, name, value):
        self._container[name] = value

    def get_var(self, name):
        return self._container.get(name)

    def delete_var(self, name):
        del self._container[name]
