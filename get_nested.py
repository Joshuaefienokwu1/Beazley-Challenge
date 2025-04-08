def get_nested_value(obj, key_path):
    keys = key_path.split('/')
    current = obj
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None  
    return current

obj1 = {"a": {"b": {"c": "d"}}}
print(get_nested_value(obj1, "a/b/c")) 

obj2 = {"x": {"y": {"z": "a"}}}
print(get_nested_value(obj2, "x/y/z"))  
