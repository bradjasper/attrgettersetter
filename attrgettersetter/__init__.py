# Attrgetter is borrwed heavily from default Python version
def attrgetter(*items):
    def resolve_attr(obj, attr, default=None):
        for name in attr.split("."):
            obj = getattr(obj, name, default)
        return obj

    if len(items) == 1:
        attr = items[0]
        def g(obj, default=None):
            return resolve_attr(obj, attr, default)
    else:
        def g(obj, default=None):
            return tuple(resolve_attr(obj, attr, default) for attr in items)
    return g

# Attrsetter uses similar foundation
def attrsetter(*items):

    def resolve_attr(obj, attr):
        attrs = attr.split(".")
        head = attrs[:-1]
        tail = attrs[-1]

        for name in head:
            obj = getattr(obj, name)
        return obj, tail

    def g(obj, val):
        for attr in items:
            resolved_obj, resolved_attr = resolve_attr(obj, attr)
            setattr(resolved_obj, resolved_attr, val)
    return g



