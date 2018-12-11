import json
import os

from wings_sanic import application, settings, views

# -----------  dev settings -------------
dev_settings = {
    'BLUEPRINTS': [
        'api.api'
    ],

    'DEFAULT_CONTEXT': {
        'response_shape': views.ResponseShapeCodeDataMsg
    },

    'SWAGGER': {
        'info': {
            "version": os.environ.get('PROJECT_VERSION', '1.0.0'),
            "title": 'Sample API',
            "description": 'sample for wings-sanic',
            "termsOfService": None,
            "contact": {
                "email": "songtao@klicen.com"
            },
            "license": {
                "email": None,
                "url": None
            }
        },
        'schemes': ['http']
    },
    'DEBUG': True,
    'HTTP_PORT': 8080,
    'CORS': True
}
settings.load(**dev_settings)

# ----------- use config that is from environ to cover dev_settings ----------
config_json = os.environ.get('CONFIG', '')
if config_json:
    try:
        conf = json.loads(config_json)
        if conf and isinstance(conf, dict):
            settings.load(**conf)
    except:
        pass

# --------------------- main -----------------
if __name__ == '__main__':
    application.start()
