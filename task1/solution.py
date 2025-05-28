def strict(func):
    annotations = func.__annotations__
    arg_annotations = {
        key: value for key, value in annotations.items() if key != 'return'
    }
    arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]

    def wrapper(*args, **kwargs):
        bound_arguments = {}
        # Обработка позиционных аргументов
        for i, arg in enumerate(args):
            if i < len(arg_names):
                bound_arguments[arg_names[i]] = arg
        # Обработка ключевых аргументов
        for key, value in kwargs.items():
            bound_arguments[key] = value
        
        # Проверка типов
        for param, param_type in arg_annotations.items():
            if param in bound_arguments:
                value = bound_arguments[param]
                if not isinstance(value, param_type):
                    raise TypeError(
                        f"Аргумент '{param}' должен быть типа {param_type.__name__}"
                    )
        
        
        return func(*args, **kwargs)
    
    return wrapper