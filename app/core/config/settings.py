from dataclasses import dataclass


@dataclass
class Settings:

    debug = True

    environment = "development"

    model_version = "v6"

    api_version = "v1"

    enable_cache = True

    enable_monitoring = True

    enable_logging = True


settings = Settings()