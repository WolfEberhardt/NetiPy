def check_lang(func):
    def wrapper():
        import locale
        if locale.getlocale()[0] == "en_US":
            func()
        else:
            return False 
    return wrapper

def get_lang():
    import locale
    return locale.getdefaultlocale()[0]
