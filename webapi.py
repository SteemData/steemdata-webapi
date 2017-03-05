import os

from eve import Eve
from eve_docs import eve_docs
from flask_bootstrap import Bootstrap

# init Eve
app = Eve(settings='settings.py')

# init Eve-Docs
Bootstrap(app)
app.register_blueprint(eve_docs, url_prefix='/docs')

if __name__ == '__main__':
    app.run(host=os.getenv('FLASK_HOST', '127.0.0.1'),
            debug=not os.getenv('PRODUCTION', False))
