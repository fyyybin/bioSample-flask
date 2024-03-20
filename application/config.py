class BaseConfig:
    """ 基本的配置类
    """
    SYSTEM_VERSION = '0.1'
    TOKEN_SECRET = 'sdjf08435jldfnx'
    pass


class DevConfig(BaseConfig):
    """ 用于开发的配置类
    """
    DB_HOST = '127.0.0.1'
    DB_PORT = 27017
    JENA_HOST = '127.0.0.1'
    JENA_PORT = 3030
    TOKEN_EXPIRE = 30 * 60          # token超期30分钟
    TOKEN_CHECK = True


class RunConfig(BaseConfig):
    """ 用于正式运行的配置类
    """
    DB_HOST = '127.0.0.1'
    DB_PORT = 27017
    JENA_HOST = '127.0.0.1'
    JENA_PORT = 3030
    TOKEN_EXPIRE = 24 * 60 * 60     # token超期1天
    TOKEN_CHECK = True


config = {
    'dev': DevConfig,
    'run': RunConfig
}
