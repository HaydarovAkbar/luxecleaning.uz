from decouple import config

ENV_NAME = config("ENV_NAME", default="local")

if ENV_NAME == "local":
    from .local import *
elif ENV_NAME == "prod":
    from .prod import *
else:
    from .base import *