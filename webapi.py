import os
from contextlib import suppress

from eve import Eve

app = Eve(settings='settings.py')

if __name__ == '__main__':
    app.run(host=os.getenv('FLASK_HOST', '127.0.0.1'),
            debug=not os.getenv('PRODUCTION', False))
