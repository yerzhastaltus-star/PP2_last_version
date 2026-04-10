from configparser import ConfigParser

def load_config(filename = "database.ini", section = "postgresql"):
    parser = ConfigParser()
    config = {}
    parser.read(filename)
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    
    else:
        raise Exception() 
    return config


if __name__ == "__main__":
    config = load_config()
    print(config)